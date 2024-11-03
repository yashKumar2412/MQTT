import paho.mqtt.client as mqtt 

# Define the callback function for when a message is received
def on_message(client, userdata, msg):
    print(f"Received {msg.payload.decode()} on topic {msg.topic}")

# Define the callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic")

# Create a client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
broker = "127.0.0.1"
port = 1883
client.connect(broker, port, 60)

# Start the loop to process callbacks
client.loop_forever()