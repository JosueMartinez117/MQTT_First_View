import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with code result {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.username_pw_set("Josue", "clase2023")
client.will_set("josue/python_publisher","Python_Publisher")
client.connect("driver.cloudmqtt.com", 18591, 60)

for i in range(3):
    client.publish('josue/cuenta', payload=i, qos=0, retain=False)
    print(f"send {i} to josue/cuenta")
    time.sleep(1)

for i in range(3):
    client.publish('josue/retain', payload=(i**2), qos=0, retain=True)
    print(f"send {i} to josue/retain")
    time.sleep(1)
client.loop_forever()
