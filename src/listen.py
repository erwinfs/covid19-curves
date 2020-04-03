import paho.mqtt.client as mqtt
import os

cmd = "./run"
MQTThost = "broker.stanford-clark.com"
MQTTport = 1885
MQTTkeepalive = 60
MQTTtopic = "UK/#"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTTtopic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # returned_value = os.system(cmd)  # returns the exit code in unix
    # print('Returned value:', returned_value)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTThost, MQTTport, MQTTkeepalive)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
