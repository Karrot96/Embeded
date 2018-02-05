import Sensor
import CommInternet
import json

def jsonify():
    return json.dumps({'name':'humid1' , 'value': Sensor.humidity()})

def send():
    CommInternet.SendJson(jsonify())

print ('humidity: ', Sensor.humidity())
