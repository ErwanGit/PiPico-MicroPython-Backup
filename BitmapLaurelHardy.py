from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

LARGEUR_OLED=128
HAUTEUR_OLED=64

LARGEUR_IMAGE=102
HAUTEUR_IMAGE=64

NOM_FICHIER = 'LaurelHardy.pbm'

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)
oled = SSD1306_I2C(LARGEUR_OLED, HAUTEUR_OLED, i2c)

oled.fill(0)

with open(NOM_FICHIER, 'rb') as f:
    f.readline()
    f.readline()
    f.readline()
    data = bytearray(f.read())
fbuf = framebuf.FrameBuffer(data, LARGEUR_IMAGE, HAUTEUR_IMAGE, framebuf.MONO_HLSB)

oled.blit(fbuf, 15, 0)

oled.show()
print(data)

