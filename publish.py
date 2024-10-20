import json
import paho.mqtt.publish as publish

broker_address = "broker.hivemq.com"
port = 1883
topic = "sensor/data"

data = {
    "id": 11,
    "packet_no": 126,
    "temperature": 30,
    "humidity": 60,
    "tds": 1100,
    "ph": 5.0
}

payload = json.dumps(data)

publish.single(topic, payload, hostname=broker_address, port=port)
print("Data published successfully")