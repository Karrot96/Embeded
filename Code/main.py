#TO be the main code
import CommInternet
import Json
import time



CommInternet.DisableAp()
CommInternet.ConnectWifi()
#CommInternet.SendJson(data)

while True:
    Json.send()
    time.sleep(20)
