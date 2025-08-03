import csv
import json
from azure.eventhub import EventHubConsumerClient

EVENT_HUB_CONNECTION_STR = "Endpoint=sb://ihsuprodswitzerlandnorthres002dednamespace.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=Lrd/3pL9Jeava+EsQzg5sO7YTZ8K3EzSkAIoTOZTfXo=;EntityPath=iothub-ehub-rkiot-55265579-aecd39394f"
EVENT_HUB_NAME = "iothub-ehub-rkiot-55265579-aecd39394f"

CSV_FILE = "traffic_log.csv"
FIELDNAMES = ["timestamp", "device", "vehicleCount", "energy"]

# Track total energy consumption
device_energy = {}

def on_event(partition_context, event):
    try:
        data = json.loads(event.body_as_str(encoding='UTF-8'))
        device = data.get("device")
        energy = float(data.get("energy", 0))

        # Aggregate energy per device
        device_energy[device] = device_energy.get(device, 0) + energy

        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({
                "timestamp": data.get("timestamp"),
                "device": device,
                "vehicleCount": data.get("vehicleCount"),
                "energy": energy
            })

        print(f"✅ {device} | Count: {data['vehicleCount']} | Energy: {energy}J | Total Device Energy: {round(device_energy[device], 2)}J")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    client = EventHubConsumerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR,
        consumer_group="$Default",
        eventhub_name=EVENT_HUB_NAME
    )
    print("📡 Listening to traffic sensor data...")
    with client:
        client.receive(on_event=on_event, starting_position="-1")