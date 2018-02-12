import CommInternet
import Json
import time

#call relevant functions to set up wifi connection
CommInternet.DisableAp()
CommInternet.ConnectWifi()

#send data at periodic intervals
while True:
    Json.send()
    time.sleep(20)
