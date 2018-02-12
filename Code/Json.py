import Sensor
import CommInternet
import ujson as json

#convert data to json
def jsonify():
    return json.dumps({'name':'fog' , 'value':Sensor.humidity() ,  'WindowFogged':Sensor.fog(), 'RemoveFog': False})

#send json data using MQTT
def send():
    CommInternet.SendJson(jsonify())

#print ('humidity: ', Sensor.humidity())
