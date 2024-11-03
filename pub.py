import time
import paho.mqtt.client as mqtt

# Define the callback function for when a message is published
def on_publish(client, userdata, mid, properties=None):
    print("Message Published")

# Create a client instance
client = mqtt.Client()

# Assign the callback function
client.on_publish = on_publish

# Connect to the broker
broker = "127.0.0.1"
port = 1883
client.connect(broker, port, 60)

# Publish a message
topic = "test/topic"
message = "Hello MQTT"
client.publish(topic, message)

# Start the loop to process callbacks
client.loop_start()

# Stop the loop after a short delay 
#time.sleep(2)
#client.loop_stop()

# Why use msg.encode('utf-8') here
# MQTT is a binary based protocol where the control elements are binary bytes and not text strings.
# Topic names, Client ID, Usernames and Passwords are encoded as stream of bytes using UTF-8.
for x in range(0, 10000):
    msg = "message " + str(x + 1)
    info = client.publish(
        topic,
        payload=msg.encode('utf-8'),
        qos=0,
    )
    # Because published() is not synchronous,
    # it returns false while he is not aware of delivery that's why calling wait_for_publish() is mandatory.
    info.wait_for_publish()
    print(info.is_published())