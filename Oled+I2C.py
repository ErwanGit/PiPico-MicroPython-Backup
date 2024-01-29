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

oled.text("Hello", 0, 0)
oled.text("World", 0, 10)
oled.text("My name is", 0, 20)
oled.text("Erwan", 0, 30)
oled.text("Welcome", 0, 40)
oled.text("1234567890ABCDEF", 0, 50)
oled.show()
time.sleep(5)

while True:
    oled.fill(0)
    oled.pixel(0,0,1)
    oled.pixel(64,32,1)
    oled.pixel(127,63,1)
    oled.show()
    time.sleep(1)
    
    oled.text("Salut le monde", 0,15,1)
    oled.show()
    time.sleep(1)
    for i in range(5):
        oled.invert(1)
        time.sleep(1)
        oled.invert(0)
        time.sleep(1)