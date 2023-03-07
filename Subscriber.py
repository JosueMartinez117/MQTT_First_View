import paho.mqtt.client as mqtt

# The callback function of connection
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("$SYS/#")
    client.subscribe("josue/#")
    client.subscribe("josue/retain")

#The callback function for received message
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("Josue", "clase2023")
client.connect("driver.cloudmqtt.com", 18591, 60)
client.loop_forever()