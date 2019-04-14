import gc
import time

from filehelper import makefileifneed
from websettings import websettings

import network

from machine import Pin

gc.enable()

def connection(network_name, network_password):
    attempts = 0
    station = network.WLAN(network.STA_IF)
    station.active(True)
    neighborhood = list(map(lambda x: x[0], station.scan()))
    if not station.isconnected():
        print("Connecting to network...")
        
        station.connect(network_name, network_password)
        while not station.isconnected():
            print("Attempts: {}".format(attempts))
            attempts += 1
            time.sleep(5)
            if attempts > 3:
                print("abandon connection, back to accespoinmode to to page and set again !")
                accespointmode()

    print('Network Config:', station.ifconfig())
    return station, neighborhood

def on_message(mqttc, msg):
    from machine import reset
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    sleeptime = int(msg[-2:])
    message = msg[:-2]
    ap.config(essid=message.decode('ascii'), authmode=1)
    print(sleeptime*60)
    time.sleep(sleeptime*60)
    reset()


def accespointmode():
    from dnsquery import DNSQuery
    websets.setTemplate('set_ap.html')
    websets.setregexp(['networkname','password','mqaddress','mqname', 'mqpass'])
    websets.addTempVars({'ssid':'networkname','pass':'password','mqaddress':'mqaddress','mqname':'mqname','mqpass':'mqpass'})

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='temp_informer', authmode=1)


    dnss = DNSQuery(ap)

    while True:
        dnss.DNSQnA()
        websets.WEBQnA()
        time.sleep_ms(1000)

def clientmode(existing_config):
    from umqtt.simple import MQTTClient
    import machine
    import ujson

    neighborhood = connection(existing_config['networkname'],existing_config['password'])[1]

    if existing_config['mqname'] and existing_config['mqpass']:
        mqc = MQTTClient("informaer", existing_config['mqaddress'], user=existing_config['mqname'], password=existing_config['mqpass'])
    else:
        mqc = MQTTClient("informaer", existing_config['mqaddress'])
    
    mqc.connect()
    time.sleep(1)
    mqc.set_callback(on_message)
    mqc.publish('network/wireless',ujson.dumps(neighborhood) )

    time.sleep(1)

    mqc.subscribe("informer", 0)      
    while True:
        mqc.check_msg()
        time.sleep(1)


def captive_portal(websets):
    
    existing_config = websets.test_config() 

    if not existing_config:
        accespointmode()
    else:
        clientmode(existing_config)
             

websets = websettings()

clear = Pin(0)
if not clear.value():
	print("clearing settings !")
	websets.clear_settings()

captive_portal(websets)