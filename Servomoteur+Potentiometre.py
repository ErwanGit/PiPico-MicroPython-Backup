import machine
import utime

potentiometer = machine.ADC(26)
servo = machine.PWM(machine.Pin(16))
servo.freq(50)

while True:
    rapport_cyclique = int(potentiometer.read_u16() * 190/1861 + 1309)
    servo.duty_u16(rapport_cyclique)
    utime.sleep_ms(100)
    
    print(" Rapport Cyclique de", rapport_cyclique,
          "/65535, ce qui correspond à une valeur décimale du signal du potentiometre de:",
          potentiometer.read_u16())