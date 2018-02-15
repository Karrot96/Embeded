from umqtt.simple import MQTTClient
import machine
from machine import Pin
import time
import ujson as json
import Functions

# set up the i2c port
i2cPort=I2C(scl=Pin(5), sda=Pin(4), freq=100000)
i2cPort.start()

# detects the address of the i2c device dynamically
address = i2cPort.scan()

# loads json to MQTT
def sub_cb(topic, msg):
    global x
    x = json.loads(msg)
    print((topic, x['RemoveFog']))

# read message from MQTT, used for demo purposes
def Sub(i2cPort, address):
    server="localhost",
    global x
    c = MQTTClient(machine.unique_id(), '192.168.0.10') #MQTTClient setup
    c.set_callback(sub_cb)
    c.connect() #connects to MQTTClient
    c.subscribe(b"ESYS/netball") #subscribes to correct topic
    while True:
        # Non-blocking wait for message
        c.check_msg()
        if(x['RemoveFog'] == "true"):
            Functions.demist(i2cPort, address, True) #if user wants to remove fog, turn on demister
            x['RemoveFog'] = "false" #reset 'RemoveFog'
            c.disconnect()
            c.connect() #reconnect to ensure new value of 'RemoveFog' is recognised
            c.subscribe(b"ESYS/netball")
        # Then need to sleep to avoid 100% CPU usage (in a real
        # app other useful actions would be performed instead)
        time.sleep(4)

# same function as above except fog value detected and sent as json
def Main(i2cPort, address):
    server="localhost"
    global x
    c = MQTTClient(machine.unique_id(), '192.168.0.10')
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"ESYS/netball")
    while True:
            # Non-blocking wait for message
            c.check_msg()
            if Functions.fog(i2cPort, address):
                Functions.send(i2cPort, address)
            if(x['RemoveFog'] == "true"):
                Functions.demist(i2cPort, address, False)
                x['RemoveFog'] = "false"
                c.disconnect()
                c.connect()
                c.subscribe(b"ESYS/netball")
            time.sleep(5)

    c.disconnect()

# demonstrates sensor reading values and sets humidity to 100 for demo purposes
def demo(i2cPort, address):
    global x
    print("Temperature is: " + str(Functions.temp(i2cPort, address)) + " Degrees")
    print("Humidity is: " +str(Functions.humidity(i2cPort, address)) + "%")
    print("Setting humidity to 100.")
    demoJson = json.dumps({'name':'fog' , 'value':100 ,  'WindowFogged':True, 'RemoveFog': False}) #override humidity reading to show demister works
    Functions.SendJson(demoJson) #send new Json to MQTT
    x = json.loads(demoJson)
    Sub(i2cPort, address) #react to reading

#call relevant functions to set up wifi connection
global x
initialJson = json.dumps({'name':'fog' , 'value':-1 ,  'WindowFogged':False, 'RemoveFog': False}) #initialise Json
x = json.loads(initialJson)
Functions.DisableAp()
Functions.ConnectWifi()
text = input("enter 'd' to demo: ") #enter demo mode
if text == 'd':
    demo(i2cPort, address)
else:
#send data at periodic intervals
    Main() #otherwise just take readings
