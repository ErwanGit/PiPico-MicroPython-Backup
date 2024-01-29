import machine
import utime

potentiometer = machine.ADC(26)
servo = machine.PWM(machine.Pin(16))
servo.freq(50)
button_0 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_90 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_180 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    print(button_0.value())
    if button_0.value():
        servo.duty_u16(1350)
        utime.sleep(2)
    elif button_90.value():
        servo.duty_u16(4350)
        utime.sleep(2)
    elif button_180.value():
        servo.duty_u16(8000)
        utime.sleep(2)
    else:
        rapport_cyclique = int(potentiometer.read_u16() * 190/1861 + 1309)
        servo.duty_u16(rapport_cyclique)
        utime.sleep_ms(100)
    
        print(" Rapport Cyclique de", rapport_cyclique,
              "/65535, ce qui correspond à une valeur décimale du signal du potentiometre de:",
              potentiometer.read_u16())
