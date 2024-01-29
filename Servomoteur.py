import machine
import utime

servo = machine.PWM(machine.Pin(16))
servo.freq(50)

while True:
    servo.duty_u16(1550)
    utime.sleep(3)
    servo.duty_u16(8000)
    utime.sleep(3)