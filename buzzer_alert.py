from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(4)

def intensity_level():
    while True:
        buzzer.on()
        sleep(0.5)
        buzzer.off()
        sleep(0.5)
