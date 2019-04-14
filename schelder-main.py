import time
import network
import urandom

dier = ['mensen', 'chiwawa', 'bulldog' ,'snoekbaars', 'zalm', 'spinnen', 'zeemeerminen','bokken', 'geiten', 'schapen', 'wolven', 'konijnen', 'muizen','raven', 'vleermuis', 'ratten', 'kippen', 'vlooien', 'apen', 'neushoorn', 'eenhoorn', 'tijger', 'krokodilen', 'hagedissen']

onderdelen = ['staart', 'poot', 'vleugel', 'haar', 'long', 'hart', 'nagel', 'neus', 'oor', 'ziel', 'essentie', 'elleboog', 'hoorn', 'gal', 'lever', 'kieuw', 'schub', 'eelt', 'kwijl', 'bill', 'oorlel', 'wrat', 'nier', 'bot', 'slijm']

eenheden = ['gram', 'mespuntjes', 'snufjes', 'schepjes', 'korrels', 'blokjes', 'druppels', 'emmers', 'kilo', 'deciliter', 'mililiter', 'centiliter', 'theelepels', 'eetlepels', 'pollepels', 'emmers', 'vrachtwagens', 'bootladingen']


def composer():
	ssid = ""
	ssid += str(int(9 * (urandom.getrandbits(8) / 255)) + 2)
	ssid += ' ' + eenheden[int(len(eenheden) * (urandom.getrandbits(8) / 255)) - 1]
	ssid += ' ' + dier[int(len(dier) * (urandom.getrandbits(8) / 255)) - 1]
	ssid += ' ' + onderdelen[int(len(onderdelen) * (urandom.getrandbits(8) / 255)) - 1]
	return ssid


ap = network.WLAN(network.AP_IF)
ap.active(True)

while True:

    ap.config(essid=composer(), authmode=1)
    time.sleep(5)