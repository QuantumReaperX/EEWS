# from signal import signal, SIGTERM, SIGHUP, pause
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

# def clear_lcd():
#     lcd.clear()

def display_alert():
    try:
        message1 = "Seismic Logging..."
        message2 = "No EQ Alert!"
        lcd.text(message1, 1)
        lcd.text(message2, 2)
       #  pause()
    except KeyboardInterrupt:
        pass
    finally:
#         clear_lcd()# finally:
        # reading = False
        sleep(0.05)
        lcd.clear()

# display_alert()