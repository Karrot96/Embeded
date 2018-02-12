import Sensor
import CommInternet
import ujson as json

#convert data to json
def jsonify():
    return json.dumps({'name':'humid1' , 'value': Sensor.fog()})

#send json data using MQTT
def send():
    if Sensor.fog() == True:
        CommInternet.SendJson(jsonify())

print ('humidity: ', Sensor.humidity())
