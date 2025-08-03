import time
import threading
import json
import random
from azure.iot.device import IoTHubDeviceClient, Message

SEND_INTERVAL = 5  # seconds

# Replace with your actual IoT device connection strings
DEVICE_CONFIG = {
    "trafficSensor01": {
        "conn": "HostName=rkiot.azure-devices.net;DeviceId=trafficSensor01;SharedAccessKey=IydlWaaqJnVosu6Pd1HMzndzwthVyw4A0opXdCLRPEc="
    },
    "trafficSensor02": {
        "conn": "HostName=rkiot.azure-devices.net;DeviceId=trafficSensor02;SharedAccessKey=/Gbx9jDp4EmLAdlpaKkUW0TZml86EmPCxmGTW1Tlga8="
    },
    "trafficSensor03": {
        "conn": "HostName=rkiot.azure-devices.net;DeviceId=trafficSensor03;SharedAccessKey=aaatkBTNuY8BXzAU/bqYlp/05vsDr/dEwithMvrePK4="
    },
    "trafficSensor04": {
        "conn": "HostName=rkiot.azure-devices.net;DeviceId=trafficSensor04;SharedAccessKey=8l9+/Dgz+qMAeA/Eh+sYWoV78Kwd7h7SNSLoRZF9/k4="
    }
}

def send_vehicle_data(device_id, conn_str):
    client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    client.connect()
    print(f"[{device_id}] ✅ Connected")

    while True:
        vehicle_count = random.randint(0, 100)
        # Energy model: base + per-vehicle contribution
        energy_used = 0.05 + (0.001 * vehicle_count)

        payload = {
            "device": device_id,
            "vehicleCount": vehicle_count,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "energy": round(energy_used, 4)
        }

        message = Message(json.dumps(payload))
        message.content_type = "application/json"
        message.content_encoding = "utf-8"

        client.send_message(message)
        print(f"[{device_id}] 🚗 Sent: {payload}")
        time.sleep(SEND_INTERVAL)

if __name__ == "__main__":
    for device_id, conf in DEVICE_CONFIG.items():
        t = threading.Thread(target=send_vehicle_data, args=(device_id, conf["conn"]))
        t.daemon = True
        t.start()

    while True:
        time.sleep(10)