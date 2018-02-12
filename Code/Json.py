import Sensor
import CommInternet
import ujson as json

#convert data to json
def jsonify():
    return json.dumps({'name':'humid1' , 'value': Sensor.humidity()})

#send json data using MQTT
def send():
    CommInternet.SendJson(jsonify())

print ('humidity: ', Sensor.humidity())
