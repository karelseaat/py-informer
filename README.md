 # Py Informer
A MicroPython-based ESP32 project for creating access points with dynamic names.

## Overview
This repository contains the source code for a MicroPython project that creates access points (APs) on an ESP32 device. The AP name changes dynamically to provide some amusement, but the main purpose of this project is not to connect to the internet.

## Components
The project includes several files:

1. `lib/dnsquery.py` - Contains a DNS query class used by the access point to respond to DNS queries from clients.
2. `schelder-main.py` - Configures the ESP32 device to create an access point and changes its name randomly at regular intervals.
3. `main.py` - Main script that initializes the AP, establishes a connection to a WiFi network if configuration is provided, and handles MQTT client functionality.
4. `lib/filehelper.py` - Utility functions for managing files on the ESP32 device.
5. `websettings.py` - Class handling template generation, form parsing, and configuration file management for web-based settings interface.
6. `set_ap.html` - HTML template for the web-based settings interface.

## Usage
To use this project, follow these steps:

1. Flash the MicroPython firmware on your ESP32 device.
2. Copy all files from this repository to the root directory of your ESP32's file system.
3. Connect to the access point created by the ESP32 device and open a web browser to access the settings interface at `http://<access_point_name>`.
4. Configure your WiFi network details and MQTT broker information if needed.
5. Save the configuration, and the ESP32 will connect to your WiFi network and handle MQTT messages if configured.

## Notes
- The access point name changes randomly and may contain insults or nonsensical words for entertainment purposes.
- This project is intended for educational and personal use only. It does not provide any real networking functionality, as the AP created by this project does not connect to the internet.
- For more information on MicroPython, visit [micropython.org](https://micropython.org/).

## Contributing
Contributions are welcome! If you find a bug or have an idea for improvement, please open an issue or submit a pull request.