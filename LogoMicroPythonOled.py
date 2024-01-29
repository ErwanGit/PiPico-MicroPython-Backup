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

oled.fill(0)
oled.fill_rect(0, 0, 32, 32, 1)
oled.fill_rect(2, 2, 28, 28, 0)
oled.vline(9, 8, 22, 1)
oled.vline(16, 2, 22, 1)
oled.vline(23, 8, 22, 1)
oled.fill_rect(26, 24, 2, 4, 1)
oled.text("MicroPython", 40, 0, 1)
oled.text("SSD1306", 40, 12, 1)
oled.text("OLED 128x64", 40, 24, 1)
oled.show()

while True:
    oled.invert(1)
    time.sleep(1)
    oled.invert(0)
    time.sleep(1)

