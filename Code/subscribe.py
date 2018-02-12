import time
import machine
from umqtt.simple import MQTTClient

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print(topic, msg)

def sub_topic(server="localhost"):
    client  = MQTTClient(machine.unique_id(), '192.168.0.10')
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(b"ESYS/netball")
    client.check_msg()
    client.disconnect()
