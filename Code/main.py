import CommInternet
from umqtt.simple import MQTTClient
import machine
from machine import Pin
import Json
import time
import Sensor
import subscribe
import ujson as json

def demist():
    p2 = Pin(2, Pin.OUT)
    while (Sensor.humidity() > 75):
        p2.off()    # pin is active low
        time.sleep(30000)
    if (Sensor.humidity() <= 75):
        p2.on()
        Json.send()
    else:
        demist()

def sub_cb(topic, msg):
    global x
    print("here")
    x = json.loads(msg)
    print((topic, x['RemoveFog']))

def Sub(server="localhost"):
    global x
    c = MQTTClient(machine.unique_id(), '192.168.0.10')
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"ESYS/netball")
    while True:
        # Non-blocking wait for message
        print("Waiting")
        c.check_msg()
        print("Waiting")
        if(x['RemoveFog'] == "true"):
            demist()
            x['RemoveFog'] = "false"
            c.disconnect()
            c.connect()
            c.subscribe(b"ESYS/netball")
        # Then need to sleep to avoid 100% CPU usage (in a real
        # app other useful actions would be performed instead)
        time.sleep(4)


def Main(server="localhost"):
    global x
    c = MQTTClient(machine.unique_id(), '192.168.0.10')
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"ESYS/netball")
    while True:
            # Non-blocking wait for message
            c.check_msg()
            if Sensor.fog():
                Json.send()
            if(x['RemoveFog'] == "true"):
                demist()
                x['RemoveFog'] = "false"
                c.disconnect()
                c.connect()
                c.subscribe(b"ESYS/netball")
            time.sleep(5)


    c.disconnect()

def demo():
    global x
    print("Temperature is: " + str(Sensor.temp()) + " Degrees")
    print("Humidity is: " +str(Sensor.humidity()) + "%")
    print("Setting humidity to 100.")
    demoJson = json.dumps({'name':'fog' , 'value':100 ,  'WindowFogged':True, 'RemoveFog': False})
    CommInternet.SendJson(demoJson)
    x = json.loads(demoJson)
    Sub()

#call relevant functions to set up wifi connection
global x
initialJson = json.dumps({'name':'fog' , 'value':-1 ,  'WindowFogged':False, 'RemoveFog': False})
x = json.loads(initialJson)
CommInternet.DisableAp()
CommInternet.ConnectWifi()
text = input("enter 'd' to demo: ")
if text == 'd':
    demo()
else:
#send data at periodic intervals
    Main()
