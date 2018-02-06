#TO be the main code
import machine
import network
import Sensor
import CommInternet
import Json
import ujson as json
import time
import network
import subscribe

while True:
    CommInternet.DisableAp()
    Json.send()
    
    time.sleep(1)
    
    subscribe.sub_topic(server="localhost")
    
    time.sleep(300)
    
    
