from machine import Pin
import utime

dataPIN=Pin(18, Pin.OUT)
latchPIN=Pin(20, Pin.OUT)
clockPIN=Pin(21, Pin.OUT)

def shift_update(input, data, clock, latch):
    clock.value(0)
    latch.value(0)
    clock.value(1)
    
    for i in range(7, -1, -1):
        clock.value(0)
        data.value(int(input[i]))
        clock.value(1)
        
    clock.value(0)
    latch.value(1)
    clock.value(1)
    
while True:
    shift_update("11111111", dataPIN,clockPIN,latchPIN)
    utime.sleep(0.1)
    shift_update("01000000", dataPIN,clockPIN,latchPIN)
    utime.sleep(0.1)
    shift_update("00100000", dataPIN,clockPIN,latchPIN)
    utime.sleep(0.1)
    shift_update("00100000", dataPIN,clockPIN,latchPIN)
    utime.sleep(0.1)
    shift_update("01000000", dataPIN,clockPIN,latchPIN)
    utime.sleep(0.1)