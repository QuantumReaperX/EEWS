from gpiozero import LED
from time import sleep

red = LED(17)
green = LED(27)
blue = LED(22)

while True:
    red.on()
    sleep(1)
    red.off()
    green.on()
    sleep(1)
    blue.on()