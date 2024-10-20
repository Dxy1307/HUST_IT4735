import pika
import json

data_packet = {
    "id": 11,
    "packet_no": 126,
    "temperature": 30,
    "humidity": 60,
    "tds": 1100,
    "ph": 5.0
}

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

message = json.dumps(data_packet)
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f" [x] Sent {message}")
connection.close()