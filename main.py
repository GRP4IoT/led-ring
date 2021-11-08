from time import sleep, sleep_ms, ticks_ms
from machine import Pin
import neopixel

n = 12
p = 16

np = neopixel.NeoPixel(Pin(p), 12)

def clear():
    for i in range(12):
        np[i] = (0, 0, 0)
        np.write()

def onone():
    np[0] = (255, 0, 0)
    np[3] = (125, 204, 223)
    np[7] = (120, 153, 23)
    np[10] = (255, 0, 153)
    np.write()

def low_power():
    for i in range(4 * n):
        for j in range(n):
            np[j] = (255, 0, 0)
        np[i] = (0, 0, 0)
        np.write()
        ticks_ms(40)

onone()
sleep(1)
clear()
