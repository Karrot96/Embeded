import CommInternet
from umqtt.simple import MQTTClient
import machine
import Json
import time
import Sensor
import subscribe
import ujson as json
def sub_cb(topic, msg):
    x=json.loads(msg)
    print((topic, x['RemoveFog']))

def Sub(server="localhost"):
    c = MQTTClient(machine.unique_id(), '192.168.0.10')
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"ESYS/netball")
    while True:
        if False:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()
def Main(server="localhost"):
    c = MQTTClient(machine.unique_id(), '192.168.0.10')
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"ESYS/netball")
    while True:
            # Non-blocking wait for message
            c.check_msg()
            Json.send()
            time.sleep(5)


    c.disconnect()

def debug():
    debugJson = json.dumps({'name':'fog' , 'value':100 ,  'WindowFogged':True, 'RemoveFog': False})
    CommInternet.SendJson(debugJson)
    while True:
        Sub()
#call relevant functions to set up wifi connection
CommInternet.DisableAp()
CommInternet.ConnectWifi()
text = input("enter 'd' to debug: ")
if text == 'd':
    debug()
else:
#send data at periodic intervals
    Main()
