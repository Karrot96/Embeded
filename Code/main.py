import CommInternet
import Json
import time
import Sensor

#call relevant functions to set up wifi connection
CommInternet.DisableAp()
CommInternet.ConnectWifi()
text = input("enter 'd' to debug: ")
    if text = 'd'
        debug
    else
    #send data at periodic intervals
        while True:
            #if Sensor.fog() == True:
            Json.send()
            time.sleep(20)
