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
    SendJson(data)
    time.sleep(1)
    subscribe(server="localhost")
    
    jsonify()
    send()
    
    time.sleep(300)
    
    
