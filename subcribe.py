import paho.mqtt.client as mqtt

broker_address = "broker.hivemq.com"
port = 1883

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        client.subscribe("sensor/data")
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode("utf-8")) + " on topic " + message.topic)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port)

client.loop_forever()