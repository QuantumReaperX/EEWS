from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from time import sleep


lcd = LCD()

def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

# def display_alert():
#     try:
#         signal(SIGTERM, safe_exit)
#         signal(SIGHUP, safe_exit)
#         lcd.text("Seismic Logging,", 1)
#         lcd.text("No EQ Alert!", 2)
#         pause()
#     except KeyboardInterrupt:
#         pass
#     finally:
#         lcd.clear()
#         sleep(0.5)

def clear_lcd():
    lcd.clear()

def display_alert():
    try:
        lcd.text("Seismic Logging,", 1)
        lcd.text("No EQ Alert!", 2)
        pause()
    except KeyboardInterrupt:
        pass
    finally:
        clear_lcd()

display_alert()