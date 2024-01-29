from machine import Pin
import utime
from dht import DHT11, InvalidChecksum

sensor = DHT11(Pin(15, Pin.OUT, Pin.PULL_DOWN))

while True:
    utime.sleep(5)
    t=(sensor.temperature)
    h=(sensor.humidity)
    print("Temperature : {}".format(t), "°C")
    print("Humidity : {}".format(h), ("%"))