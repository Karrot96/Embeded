def demist():
    p2 = Pin(2, Pin.OUT)
    while (Sensor.humidity() > 75):
        p2.off()    # pin is active low
        time.sleep(30000)
    if (Sensor.humidity() <= 75):
        p2.on()
        Json.send()
    else:
        demist()
        
        
