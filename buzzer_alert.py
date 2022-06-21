from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(4)

def eq_detected():
    buzzer.on()
    sleep(10)
    buzzer.off()
    sleep(0.05)

def no_eq_detected():
    buzzer.off()
    sleep(0.05)

# eq_detected()