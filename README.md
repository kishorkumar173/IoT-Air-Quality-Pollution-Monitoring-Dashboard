# 🌍 IoT-Based Air Quality & Pollution Monitoring Dashboard

## 📌 Project Overview

The **IoT-Based Air Quality & Pollution Monitoring Dashboard** is an industry-oriented environmental monitoring system designed to monitor air quality parameters in real time.

This project simulates environmental sensor readings and uploads them to a cloud dashboard using **ThingSpeak**, enabling real-time pollution tracking, AQI classification, alert monitoring, and environmental analysis.

The system measures:

* Air Quality Index (AQI)
* Pollution Level
* Temperature
* Humidity  
* Alert Status

This project was developed as an **IoT course project** with both **hardware-based architecture** and **virtual simulation implementation** for environments where physical hardware is unavailable.

---

## 🎯 Problem Statement

Air pollution is one of the major environmental and public health concerns worldwide.

Traditional pollution monitoring systems are:

* Expensive
* Limited to specific locations
* Difficult to deploy at scale

This project provides a **low-cost IoT-based solution** for:

* Real-time air quality monitoring
* Environmental condition tracking
* AQI estimation
* Pollution alerts
* Cloud-based visualization

---

## 🚀 Features

✅ Real-time Air Quality Monitoring

✅ Temperature & Humidity Monitoring

✅ AQI Classification

✅ Pollution Status Detection

✅ Alert Generation

✅ Cloud Dashboard Integration using ThingSpeak

✅ CSV Data Logging

✅ Environmental Trend Analysis

✅ Graph Generation

✅ Beginner-Friendly & Industry-Oriented

---

## 🏗️ System Architecture

```text
Virtual Sensors / IoT Sensors
(MQ135 + DHT11)

          ↓

Data Collection Layer
(Python Simulation / ESP32)

          ↓

AQI Classification
(Good / Moderate / Poor / Hazardous)

          ↓

ThingSpeak Cloud Dashboard

          ↓

Data Visualization
(Charts + Graphs)

          ↓

CSV Logging & Reports
```

---

## 🛠️ Technologies Used

### Programming Language

* Python 3.13

### IoT Platform

* ThingSpeak

### Libraries

* Pandas
* NumPy
* Matplotlib
* Requests
* Streamlit

### Hardware Components (Architecture)

* ESP32
* MQ135 Air Quality Sensor
* DHT11 Temperature & Humidity Sensor
* LED
* Buzzer

---

## 📂 Project Structure

```text
IoT-Air-Quality-Pollution-Monitoring-Dashboard/
│
├── arduino_code/
├── python_simulation/
├── dashboard/
├── data/
├── outputs/
├── images/
├── circuit_diagram/
├── reports/
├── docs/
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

### 2. Navigate to Project

```bash
cd IoT-Air-Quality-Pollution-Monitoring-Dashboard
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Run Main Simulation

```bash
python python_simulation/main.py
```

### Generate Graphs

```bash
python python_simulation/graph_generator.py
```

---

## ☁️ ThingSpeak Dashboard

The project integrates with **ThingSpeak Cloud IoT Platform** for real-time monitoring.

### Dashboard Fields

| Field   | Description      |
| ------- | ---------------- |
| Field 1 | Air Quality      |
| Field 2 | Temperature      |
| Field 3 | Humidity         |
| Field 4 | Pollution Status |
| Field 5 | Alert Status     |

---

## 📊 AQI Classification

| AQI Value | Status    |
| --------- | --------- |
| 0–150     | Good      |
| 151–300   | Moderate  |
| 301–500   | Poor      |
| 500+      | Hazardous |

---

## 📁 Outputs Generated

The system generates:

* Real-time sensor readings
* CSV logs
* Air quality graphs
* Temperature trend graphs
* Humidity trend graphs
* ThingSpeak dashboard visualization

---

## 📸 Screenshots

Include the following screenshots:

* Project Folder Structure
* Arduino IDE Setup
* Python Simulation Running
* ThingSpeak Dashboard
* Air Quality Graph
* Temperature Graph
* Humidity Graph
* CSV Log File
* Output Screenshots

---

## 🌍 Industry Relevance

This project has applications in:

* Smart Cities
* Environmental Monitoring
* Pollution Control Boards
* Hospitals
* Schools & Colleges
* Industrial Monitoring
* Smart Homes

---

## 🔮 Future Improvements

* Real Hardware Integration using ESP32
* MQTT-Based Communication
* Mobile Notifications
* AI-Based Pollution Prediction
* Mobile App Dashboard
* Sensor Expansion

---

## 🎓 Learning Outcomes

Through this project, I learned:

* IoT System Design
* Cloud Dashboard Integration
* Python-Based Simulation
* Environmental Data Analysis
* AQI Classification
* Real-Time Data Monitoring
* CSV Logging & Visualization
* GitHub Project Documentation

---

## 👨‍💻 Author

**Kishor Kumar L**

BE CSE (AIML)

IoT-Based Environmental Monitoring Project

---

## ⭐ If you found this project useful, consider giving it a star!
