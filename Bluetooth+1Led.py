import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
bluetooth = machine.UART(0,9600)

while True:
    if bluetooth.any():
        message = bluetooth.read().decode('utf-8')
        print(message, message == '1')
        if (message == '1'):
            led_onboard.value(1)
        elif (message == '0'):
            led_onboard.value(0)