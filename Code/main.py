import CommInternet
import Json
import time
import Sensor
def debug():
    debugJson = json.dumps({'name':'fog' , 'value':100 ,  'WindowFogged':True, 'RemoveFog': False})
    CommInternet.SendJson(debugJson)
#call relevant functions to set up wifi connection
CommInternet.DisableAp()
CommInternet.ConnectWifi()
text = input("enter 'd' to debug: ")
    if text = 'd'
        debug()
    else
    #send data at periodic intervals
        while True:
            #if Sensor.fog() == True:
            Json.send()
            time.sleep(20)
