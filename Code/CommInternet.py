from umqtt.simple import MQTTClient
import machine
import network


def DisableAp():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

def ConnectWifi():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('EEERover', 'exhibition')
        while not sta_if.isconnected():
            pass
    print ('Connected: ', sta_if.isconnected())
    print('network config:', sta_if.ifconfig())

def SendJson(data):
    CLIENT_ID = machine.unique_id()
    BROKER_ADDRESS =  '192.168.0.10'
    TOPIC = "ESYS/netball/"
    client = MQTTClient(CLIENT_ID,BROKER_ADDRESS)
    client.connect()
    client.publish(TOPIC,bytes(data,'utf-8'))
