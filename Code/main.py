#TO be the main code
import machine
import network
import Sensor
import CommInternet
import Json
import ujson as json
import time
import network

while True:
    DisableAp()
    ConnectWifi()
    if not sta_if.isconnected():
        print("not connected")
        exit()
    SendJson(data)
    time.sleep(1)
    subscribe(server="localhost")
    
    jsonify()
    send()
    
    print ('humidity: ', Sensor.humidity())
    
    time.sleep(300)
    
    
