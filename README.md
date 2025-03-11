# Remote Pressure Monitoring System

## Description
This application is a remote pressure monitoring system built using Dash. It visualizes pressure readings from multiple IoT sensors in real-time.This system have been developed for Pirelli Tire Company to monitor the pressure of their tire building machines in real-time with no wiring or infrastructure. The first of many steps to Industry 4.0 .
The project contains to sepearte process that have to run in parrallel, the ble_scan_stable.py(BLE communication for sensors) and the main.py(Dash app)

## Installation
To set up the project, ensure you have the following dependencies installed:
- Dash
- Pandas
- NumPy
- Plotly
- OpenPyXL

You can install the required packages using pip:
```bash
pip install dash pandas numpy plotly openpyxl
```

## Usage
Run the application using the following command:
```bash
python main.py
```
Open your web browser and navigate to `http://127.0.0.1:8050` to view the application.

## Features
- Real-time pressure monitoring from multiple sensors.
- Interactive gauges for each sensor.
- Graphical representation of sensor data over time.
- Dropdown menu to select specific sensors for display.

## Screenshot
![Screenshot Placeholder](On-site.png)

## License
This project is licensed under the MIT License.
