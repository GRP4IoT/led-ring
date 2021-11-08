from time import sleep, sleep_ms, ticks_ms
from machine import Pin
import neopixel

# n = 12
 = 16

np = neopixel.NeoPixel(Pin(p), 12)

def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
        np.write()

def onone():
    np[0] = (255, 0, 0)
    np[3] = (125, 204, 223)
    np[7] = (120, 153, 23)
    np[10] = (255, 0, 153)
    np.write()

def low_power(np):
    n = np.n
    for i in range(4 * 12):
        for j in range(12):
            np[j] = (0, 0, 0)
        np[i % 12] = (255, 0, 0)
        np.write()
        ticks_ms(40)

onone()
sleep(1)
clear()
