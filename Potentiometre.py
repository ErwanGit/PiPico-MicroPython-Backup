import machine, utime

potentiometer = machine.ADC(26)

conversion_factor = 3.3 / (65535)

while True:
    voltage = round((potentiometer.read_u16() * conversion_factor), 2)
    print(potentiometer.read_u16())
    print(voltage)
    utime.sleep(0.5)