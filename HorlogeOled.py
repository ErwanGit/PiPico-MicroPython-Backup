import machine
import ssd1306
import time

sdaPin=machine.Pin(8)
sclPin=machine.Pin(9)

i2c=machine.I2C(0,sda=sdaPin, scl=sclPin,freq=400000)
WIDTH=128
HEIGHT=64
oled = ssd1306.SSD1306_I2C(WIDTH,HEIGHT,i2c)
oled.fill(0)

oled.text("Horloge digital", 0, 30)
oled.show()
time.sleep(5)

while True:
    oled.fill(0)
    t = time.localtime()
    
    oled.text('{}{}{}{}{}'.format(t[2], '/', t[1], '/', t[0]), 25, 0, 1)
    oled.hline(0,8,128,1)
    oled.text('{:2d}{}{:02d}{}'.format(t[3], 'h' if t[5] % 2 else ':', t[4], 'min' if t[5] % 2 else ' '), 40, 30, 1)
    oled.text('{:2d}{}'.format(t[5], 'sec'), 40, 50, 1)
    oled.show()
    time.sleep(2)
