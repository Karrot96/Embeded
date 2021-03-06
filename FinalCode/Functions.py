import machine
from machine import I2C, Pin
from umqtt.simple import MQTTClient
import time
import ujson as json
import network

# replicates turning on demister by turning on onboard blue LED when demist necessary
def demist(i2cPort, address, Demo):
    p2 = Pin(2, Pin.OUT) #blue LED uses GPIO2 (pin 2)
    if Demo:
        p2.off() #note pin is active low
        time.sleep(5)
        if (humidity(i2cPort, address) <= 75): #check value of humidity to see if can stop demisting
            p2.on() # turn off demister
            send(i2cPort, address) #send new data
        else:
            demist(i2cPort, address, False) #otherwise continue to demist
    else:
        while (humidity(i2cPort, address) > 75): # case for when not demo-ing but checking level of humidity
            p2.off()    # pin is active low
            time.sleep(30)
        if (humidity(i2cPort, address) <= 75):
            p2.on()
            send(i2cPort, address)
        else:
            demist(i2cPort, address, Demo)

# take temperature reading
def temp(i2cPort, address):
    i2cPort.writeto(address[0],bytearray([0xF3]))

    #wait for write
    time.sleep(0.020)

    #reads 2 bytes of data from address of i2c port
    tempRaw = i2cPort.readfrom(address[0], 2)

    #convert to integer
    tempInt = int.from_bytes(tempRaw,'big')

    #convert raw value to real world value
    temp = (175.72*tempInt/65536)-46.85

    #print(temp)

    return temp

# take humidity reading
def humidity(i2cPort, address):
    i2cPort.writeto(address[0],bytearray([0xE3]))

    #wait for write
    time.sleep(0.020)

    #reads 2 bytes of data from address of i2c port
    humidityRaw = i2cPort.readfrom(address[0], 2)

    #converts into an int
    humidityInt = int.from_bytes(humidityRaw,'big')

    #convert raw value to real world value
    humidity = ((125*humidityInt)/65536)-6

    print(str(humidity) + "%")

    return humidity

# check for fog by seeing if humidity is at 100% (this is defined as the point where windscreen fog will occur from research)
def fog(i2cPort, address):
    print(str(humidity(i2cPort, address)) + "%")
    if (humidity(i2cPort, address) == 100):
        return True
    else:
        return False

#convert data to json
def jsonify(i2cPort, address):
    return json.dumps({'name':'fog' , 'value':humidity(i2cPort, address) ,  'WindowFogged':fog(i2cPort, address), 'RemoveFog': False})

#send json data using MQTT
def send(i2cPort, address):
    SendJson(jsonify(i2cPort, address))

#disable network
def DisableAp():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

#connect to wifi
def ConnectWifi():
    sta_if = network.WLAN(network.STA_IF)
    #check connection and if not connected, connect using username and password
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('EEERover', 'exhibition')
        while not sta_if.isconnected():
            pass
    print ('Connected: ', sta_if.isconnected())
    if not sta_if.isconnected():
        print('Not connected to network...')
    print('network config:', sta_if.ifconfig())

#send json data to MQTT
def SendJson(data):
    CLIENT_ID = machine.unique_id()
    #define IP
    BROKER_ADDRESS =  '192.168.0.10'
    #define topic to filter
    TOPIC = "ESYS/netball"
    client = MQTTClient(CLIENT_ID,BROKER_ADDRESS)
    client.connect()
    client.publish(TOPIC,bytes(data,'utf-8'))
    client.disconnect()
    print("Published")

#check wifi connection and return boolean
def CheckConnection():
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        return True
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('EEERover', 'exhibition')
        if not sta_if.isconnected():
            return False
