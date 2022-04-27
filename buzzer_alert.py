from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(4)

def intensity_level_1():
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(0.5)

def intensity_level_2():
    pass