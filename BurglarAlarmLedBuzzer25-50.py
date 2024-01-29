import machine, utime, _thread
sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

def buzzer_thread():
    for i in range(26):
        buzzer.toggle()
        utime.sleep(1)


def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("Alarm! Motion detected")
        _thread.start_new_thread(buzzer_thread, ())
        for i in range(50):
            led.toggle()
            utime.sleep(0.1)
            
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
    led.value(1)
    utime.sleep(2)
    led.value(0)
    utime.sleep(1)
    
