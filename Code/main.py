import CommInternet
from umqtt.simple import MQTTClient
import machine
import Json
import time
import Sensor
import subscribe
import ujson as json

def demist():
    while (Sensor.humidity() > 75):
        p2 = Pin(2, Pin.OUT)
        p2.off()    # pin is active low
        time.sleep(30000)
    if (Sensor.humidity() <= 75):
        p2.on()
        Json.send()
    else:
        demist()

def sub_cb(topic, msg):
    global x
    x = json.loads(msg)
    print((topic, x['RemoveFog']))

def Sub(server="localhost"):
    global x
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
            if(x['RemoveFog'] == "true"):
                demist()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()
def Main(server="localhost"):
    global x
    c = MQTTClient(machine.unique_id(), '192.168.0.10')
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"ESYS/netball")
    while True:
            # Non-blocking wait for message
            c.check_msg()
            if(x['RemoveFog'] == "true"):
                demist()
            Json.send()
            time.sleep(5)


    c.disconnect()

def debug():
    print("Temperature is: " + str(Sensor.temp()) + " Degrees")
    print("Humidity is: " +str(Sensor.humidity()) + "%")
    print("Setting humidity to 100.")
    debugJson = json.dumps({'name':'fog' , 'value':100 ,  'WindowFogged':True, 'RemoveFog': False})
    CommInternet.SendJson(debugJson)
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
