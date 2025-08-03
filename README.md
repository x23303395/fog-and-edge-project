Simulated Traffic Sensor Data Pipeline with Azure IoT Hub, Event Hub, and Streamlit Visualization

📌 Overview
This project demonstrates a real-time, energy-aware traffic monitoring system using Azure IoT Hub, Event Hub, and a Streamlit dashboard.
The system simulates multiple traffic sensors sending vehicle count and energy usage data to Azure IoT Hub, processes it through Event Hub, and visualizes insights in real time.

🏗️ Architecture
Traffic Sensor Simulator: Python script emulating IoT traffic sensors generating vehicle count and energy metrics.

Azure IoT Hub: Cloud gateway for device management and secure telemetry ingestion.

Azure Event Hub: High-throughput event streaming service for decoupled data processing.

Event Listener: Consumes telemetry from Event Hub and stores it in a CSV file.

Streamlit Dashboard: Provides live visualization of traffic trends, energy usage, and alerts.


📂 Project Structure
bash
Copy
Edit
├── traffic_sensor_simulator.py   # Simulates traffic sensors sending data
├── event_listener.py             # Consumes data from Event Hub and stores in CSV
├── traffic_dashboard.py          # Streamlit dashboard for visualization
├── requirements.txt              # Python dependencies
├── traffic_architecture.png      # Architecture diagram
└── README.md                     # Project documentation
⚙️ Setup Instructions
1️⃣ Clone Repository
bash
Copy
Edit
git clone <repo-url>
cd <repo-folder>
2️⃣ Create Virtual Environment & Install Dependencies
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
3️⃣ Azure Setup
Create an Azure IoT Hub.

Register IoT devices and obtain their connection strings.

Configure an Azure Event Hub and route IoT Hub messages to it.

4️⃣ Run the Traffic Sensor Simulator
Update your IoT Hub device connection string(s) in traffic_sensor_simulator.py and start:

bash
Copy
Edit
python traffic_sensor_simulator.py
5️⃣ Run the Event Listener
Update the Event Hub connection string in event_listener.py and start:

bash
Copy
Edit
python event_listener.py
6️⃣ Launch the Dashboard
bash
Copy
Edit
streamlit run traffic_dashboard.py
Open the provided URL in your browser to view live analytics.

📊 Features
✅ Real-time traffic data simulation
✅ Azure IoT Hub and Event Hub integration
✅ Energy-aware analytics per device
✅ High-traffic alert detection
✅ Interactive Streamlit dashboard with KPIs and charts

📈 Metrics
Vehicle count per device and over time

Energy consumption trends

High-traffic alerts

Message distribution across devices

📜 License
This project is for academic purposes as part of the Fog and Edge Computing CA project.