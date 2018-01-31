#import the necessary modules
from machine import I2C, Pin
import time
#creates the port i2c
def temp():
    i2cPort=I2C(scl=Pin(5), sda=Pin(4), freq=100000)
    i2cPort.start()
    #sensor is generating data of size 0xF3 bytes and writing it to memory address 0x40
    #When we declare the address we should do it dynamically.
    #I think this will fix the problem we are having
    # http://docs.micropython.org/en/latest/wipy/library/machine.I2C.html
    #Use the link of the i2c library.
    #I think use of scan will be important
    #Since list we can then just use the locations in list and dynamically allocate

    address = i2cPort.scan()
    
    i2cPort.writeto(address[0],bytearray([0xF3]))
    
    #give time for write
    time.sleep(0.020)
    
    #reads 2 bytes of raw data from address as detected by i2c port
    tempRaw = i2cPort.readfrom(address[0], 2)
    
    #convert to integer
    tempInt = int.from_bytes(tempRaw,'big')
    
    #convert raw value to real world value
    temp = (175.72*tempInt/65536)-46.85
    
    print(temp)

def humidity():
    i2cPort=I2C(scl=Pin(5), sda=Pin(4), freq=100000)
    i2cPort.start()

    address = i2cPort.scan()
    
    i2cPort.writeto(address[0],bytearray([0xE3]))
    
    #give time for write
    time.sleep(0.020)
    
    #reads 2 bytes of raw data from address as detected by i2c port
    humidityRaw = i2cPort.readfrom(address[0], 2)
    
    #converts the data into an int
    humidityInt = int.from_bytes(humidityRaw,'big')
    
    #convert raw value to real world value
    humidity = ((125*humidityInt)/65536)-6
    
    print(str(humidity) + "%")

temp()
humidity()
