from gpiozero import LED
from time import sleep

red = LED(17)
green = LED(27)
blue = LED(22)

# while True:
#     red.on()
#     sleep(1)
#     red.off()
#     green.on()
#     sleep(1)
#     blue.on()

def green_led():
    green.blink(0.5,0.25)
    print("Seismic logging...")

def red_led():
    red.on()
    print("Seismic alert...")

def red_led_off():
    red.off()

def blue_led():
    blue.blink(1,1)
    print("No seismic event...")
