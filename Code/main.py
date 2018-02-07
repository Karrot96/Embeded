#TO be the main code
import machine
import network
import Sensor
import CommInternet
<<<<<<< HEAD
import ujson as json
import time
import network


def DisableAp()
def ConnectWifi()
if not sta_if.isconnected():
    print("not connected")
    exit()
def SendJson(data)
=======
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
    
    
>>>>>>> 0a8ab7dab8fbbcf17eb95e3643e57a29e18ae4f4
