# PROGRAM TO SWITCH ON RELAY

import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

relay1 = 38
gpio.setup(relay1, gpio.OUT, initial=0)

try:
    gpio.output(relay1, True)
    print("relay is switched on ...Please press ctrl+c to exit")
    time.sleep(15)
    gpio.output(relay1, False)
    print("relay is switched off")

except KeyboardInterrupt:
    gpio.cleanup()
    print("program exited")