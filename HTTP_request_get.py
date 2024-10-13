import requests

url = 'https://api.thingspeak.com/channels/1529099/feeds.json?results=2'

response = requests.get(url)

if response.status_code == 200:
    print('Data received from ThingSpeak successfully.')

    data = response.json()
    feeds = data['feeds']

    if feeds:
        for i, feed in enumerate(feeds):
            temperature = feed['field1']
            humidity = feed['field2']
            print(f"Feed {i}: Temperature = {temperature}, Humidity = {humidity}")
    else:
        print('No feeds available.')
else:
    print('Error in receiving data from ThingSpeak.')

print("Nguyễn Đức Duy - 20210275")