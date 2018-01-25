#import the necessary modules
from machine import Pin,I2C 
#creates the port i2c
i2cPort=I2C(scl=Pin(5), sda=Pin(4), freq=100000)
#sensor is generating data of size 0xF3 bytes and writing it to memory address 0x40
i2cPort.writeto(0x40,bytearray([0xf3]))
#reads 2 bytes of data from address 0x40
data = i2cPort.readfrom(0x40,2)
#converts the data into an int
int.from_bytes(data,'big')


