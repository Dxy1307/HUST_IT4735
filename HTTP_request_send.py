import requests
import json

api_key = 'M4ANO9SSNX1OCFLQ'
data = {
    "field1": 20,
    "field2": 33
}

headers = {
    'Content-Type': 'application/json'
}

url = f'https://api.thingspeak.com/update?api_key={api_key}'
response = requests.get(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print('Data sent to ThingSpeak successfully.')
else:
    print('Error in sending data to ThingSpeak.')

print("Nguyễn Đức Duy - 20210275")