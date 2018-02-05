from umqtt.simple import MQTTClient

import network


CLIENT_ID = machine.unique_id()
BROKER_ADDRESS =  '192.168.0.10'
client = MQTTClient(CLIENT_ID,BROKER_ADDRESS)
client.connect()
client.publish(TOPIC,bytes(data,'utf-8'))

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('EEERover', 'exhibition')

sta_if.isconnected()
