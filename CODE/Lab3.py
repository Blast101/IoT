# FLASH AN LED ON GIVEN ON_TIME AND OFF_TIME CYCLE. WHERE THE TWO TIMES ARE TAKEN FROM THE FILE . 

import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

led = 15
gpio.setup(led,gpio.OUT,initial=0)

file = open('Lab3.txt','r')
lines = file.readlines()

ON_TIME = int(lines[0].split("=")[1])
OFF_TIME = int(lines[1].split("=")[1])

try:
    while(True):
        gpio.output(led,True)
        time.sleep(ON_TIME)
        gpio.output(led,False)
        time.sleep(OFF_TIME)
except KeyboardInterrupt:
    gpio.cleanup()
