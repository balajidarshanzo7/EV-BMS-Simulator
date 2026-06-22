# EV-BMS-Simulator 🔋🚗

An Electric Vehicle Battery Management System (EV-BMS) Simulator developed using Python, Tkinter, ESP32, and sensor-based battery monitoring.

## Features

* Real-time Battery Monitoring
* Battery Percentage Estimation
* Voltage Monitoring
* Temperature Monitoring
* Battery Health Prediction
* Charge & Discharge Cycle Tracking
* Driving Range Estimation
* Safety Monitoring
* CSV Data Logging
* Battery Performance Visualization
* ESP32 Integration

---

## Technologies Used

* Python
* Tkinter
* ESP32
* PySerial
* CSV
* Matplotlib

---

## System Architecture

ESP32 Sensors
↓
Serial Communication
↓
Python Battery Management System
↓
Tkinter Dashboard
↓
CSV Data Logging
↓
Graph Visualization

---

## Dashboard Output

### Dashboard at 95% Battery

![Dashboard95](dashboard%20at%20battery%2095%25.png)

### Dashboard at 25% Battery

![Dashboard25](dashboard%20at%20battery%2025%25.png)

---

## Battery Performance Graph

![Graph](battery%20vs%20time%20graph.png)

---

## Hardware Setup

![Hardware1](hardware%20\(1\).jpeg)

![Hardware2](hardware%20\(2\).jpeg)

---

## Project Structure

```text
EV-BMS-Simulator
│
├── battery.py
├── gui.py
├── main.py
├── graph.py
├── battery_log.csv
├── README.md
│
├── dashboard at battery 95%.png
├── dashboard at battery 25%.png
├── battery vs time graph.png
├── hardware (1).jpeg
└── hardware (2).jpeg
```

---

## How to Run

### Install Dependencies

```bash
pip install pyserial pandas matplotlib
```

### Run Dashboard

```bash
python gui.py
```

### Run Graph Visualization

```bash
python graph.py
```

---

## Functionalities Implemented

* Battery Percentage Tracking
* Voltage Monitoring
* Temperature Monitoring
* Battery Health Prediction
* Charge/Discharge Simulation
* Range Calculation
* Data Logging to CSV
* Graph-Based Analysis
* ESP32 Communication

---

## Author

**Balaji Darshan**

Electronics and Communication Engineering (ECE)

---

## Project Status

✅ Completed Python EV-BMS Simulator

✅ Dashboard Interface

✅ Battery Analytics

✅ Data Logging

✅ Graph Visualization

✅ ESP32 Hardware Integration
