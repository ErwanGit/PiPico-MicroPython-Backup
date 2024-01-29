import machine, utime

potentiometer = machine.ADC(26)
led = machine.PWM(machine.Pin(15))
led.freq(1000)

conversion_factor = 3.3 / (65535)

while True:
    voltage = round((potentiometer.read_u16() * conversion_factor),2)
    led.duty_u16(potentiometer.read_u16())
    print(voltage, " volts", potentiometer.read_u16())
    utime.sleep(1)