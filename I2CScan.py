import machine

sdaPin=machine.Pin(8)
sclPin=machine.Pin(9)

i2c=machine.I2C(0,sda=sdaPin, scl=sclPin,freq=400000)

print("Scanning I2C bus")
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C device !")
else:
    print("I2C devices found:", len(devices))
    
for device in devices:
    print("Decimal adress: ", device, "| Hexa adress: ", hex(device))