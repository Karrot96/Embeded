from umqtt.simple import MQTTClient
import machine
from machine import Pin
import time
import ujson as json
import Functions

i2cPort=I2C(scl=Pin(5), sda=Pin(4), freq=100000)
i2cPort.start()

#detects the address of the i2c device dynamically
address = i2cPort.scan()   

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
            Functions.demist(i2cPort, address)
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
            if Functions.fog(i2cPort,address):
                Functions.send()
            if(x['RemoveFog'] == "true"):
                Functions.demist(i2cPort, address)
                x['RemoveFog'] = "false"
                c.disconnect()
                c.connect()
                c.subscribe(b"ESYS/netball")
            time.sleep(5)

    c.disconnect()

def demo():
    global x
    print("Temperature is: " + str(Functions.temp(i2cPort, address)) + " Degrees")
    print("Humidity is: " +str(Functions.humidity(i2cPort, address)) + "%")
    print("Setting humidity to 100.")
    demoJson = json.dumps({'name':'fog' , 'value':100 ,  'WindowFogged':True, 'RemoveFog': False})
    Functions.SendJson(demoJson)
    x = json.loads(demoJson)
    Sub()

#call relevant functions to set up wifi connection
global x
initialJson = json.dumps({'name':'fog' , 'value':-1 ,  'WindowFogged':False, 'RemoveFog': False})
x = json.loads(initialJson)
Functions.DisableAp()
Functions.ConnectWifi()
text = input("enter 'd' to demo: ")
if text == 'd':
    demo()
else:
#send data at periodic intervals
    Main()
