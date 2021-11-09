from time import sleep, sleep_ms, ticks_ms
from machine import Pin
import neopixel

n = 12 # antallet af RGB lys på LEDringen
p = 16 # Den pin LED-ringen er tilsluttet

np = neopixel.NeoPixel(Pin(p), n)

# LED ringen bliver slukket
def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
        np.write()

# LED-ringen er bare fuldt tændt
def power_on():
    for i in range(n):
        np[i] = (255, 200, 0)
        np.write()
    print("POWER ON")

# cyclus af lys (cirkel løb)
def low_power():
    print("LOW POWER")
    for i in range(16 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        if (i // n) % 2 == 0:
            np[i % n] = (255, 0, 0)
        sleep_ms(50)
        np.write()

# LED ringen bouncer frem og tilbage
def trying_con():
    for i in range(16 * n):
        for j in range(n):
            np[j] = (255, 200, 0)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        sleep_ms(50)
        np.write()
