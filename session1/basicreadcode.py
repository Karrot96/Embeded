#import the necessary modules
from machine import Pin,I2C
#creates the port i2c
i2cPort=I2C(scl=Pin(5), sda=Pin(4), freq=100000)
#sensor is generating data of size 0xF3 bytes and writing it to memory address 0x40
#When we declare the address we should do it dynamically.
#I think this will fix the problem we are having
# http://docs.micropython.org/en/latest/wipy/library/machine.I2C.html
#Use the link of the i2c library.
#I think use of scan will be important
#Since list we can then just use the locations in list and dynamically allocate

address = i2cPort.scan()

i2cPort.writeto(address[0],bytearray([0xf3]))
#reads 2 bytes of data from address 0x40
data = i2cPort.readfrom(address[0],2)
#converts the data into an int
int.from_bytes(data,'big')
