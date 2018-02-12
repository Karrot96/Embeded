
#import the necessary modules
from machine import I2C, Pin
import time

#creates the port i2c
i2cPort=I2C(scl=Pin(5), sda=Pin(4), freq=100000)
i2cPort.start()

#detects the address of the i2c device dynamically
address = i2cPort.scan()

#temp function not necessarily needed for application
def temp():
    i2cPort.writeto(address[0],bytearray([0xF3]))

    #wait for write
    time.sleep(0.020)

    #reads 2 bytes of data from address of i2c port
    tempRaw = i2cPort.readfrom(address[0], 2)

    #convert to integer
    tempInt = int.from_bytes(tempRaw,'big')

    #convert raw value to real world value
    temp = (175.72*tempInt/65536)-46.85

    print(temp)

def humidity():
    i2cPort.writeto(address[0],bytearray([0xE3]))

    #wait for write
    time.sleep(0.020)

    #reads 2 bytes of data from address of i2c port
    humidityRaw = i2cPort.readfrom(address[0], 2)

    #converts into an int
    humidityInt = int.from_bytes(humidityRaw,'big')

    #convert raw value to real world value
    humidity = ((125*humidityInt)/65536)-6
        
    print(str(humidity) + "%") 
    
    return humidity

def fog():
    if humidity == 100:
        fog = True
    else:
        fog = False
    
    return fog
