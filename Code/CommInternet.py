from umqtt.simple import MQTTClient

client = MQTTClient(CLIENT_ID,BROKER_ADDRESS)
client.connect()
client.publish(TOPIC,bytes(data,'utf-8'))

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('EEERover', 'exhibition')

isconnected()
