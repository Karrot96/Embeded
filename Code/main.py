import CommInternet
import Json
import time
import Sensor

#call relevant functions to set up wifi connection
CommInternet.DisableAp()
print("Connected")
CommInternet.ConnectWifi()
<<<<<<< HEAD
print("Connected")

#send data at periodic intervals
while True:
    #if Sensor.fog() == True:
    Json.send()
    time.sleep(20)
=======
text = input("enter 'd' to debug: ")
    if text = 'd'
        debug
    else
    #send data at periodic intervals
        while True:
            #if Sensor.fog() == True:
            Json.send()
            time.sleep(20)
>>>>>>> 7f10631109ebd0da50af46a9a2924a50f72091d1
