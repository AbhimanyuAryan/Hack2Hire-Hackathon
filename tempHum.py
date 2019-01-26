import Adafruit_DHT as dht
import threading
import json

data = {}
data['dht22_data'] = [] 
print("Working file")

def add_and_print():
    print("Wait and Thread")
    threading.Timer(15.0, add_and_print).start()
    print("Reading Data")
    
    h,t = dht.read_retry(dht.DHT22, 4)

    print "Appending data"
    data['dht22_data'].append({
        'humidity': h,
        'temperature': t
    })

    with open('data_ht.json', 'w') as outfile:
        json.dump(data, outfile)

add_and_print()