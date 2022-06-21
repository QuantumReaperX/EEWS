import csv
import time
import board
import busio
import adafruit_adxl34x
import adafruit_tca9548a
from datetime import datetime
from time import sleep
import os
# from seismic_trial_plotting_dev import *
from led_alert import *
import requests
# from lcd_display_alert import *
from threading import Thread
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
# from threading import *
from buzzer_alert import *
# from firebase.firebase import firebase

i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

reading = True
lcd = LCD()

message1 = ""
message2 = ""
intensity_level = 0
magnitude = 0
magnitude_data = []
mean_magnitude = []
accel_1 = adafruit_adxl34x.ADXL345(tca[2])
accel_2 = adafruit_adxl34x.ADXL345(tca[3])
accel_3 = adafruit_adxl34x.ADXL345(tca[4])
accel_4 = adafruit_adxl34x.ADXL345(tca[5])
# accelerometer = adafruit_adxl34x.ADXL345(i2c)

final_offset_x = float(input("Enter x_final_offset: "))
final_offset_y = float(input("Enter y_final_offset: "))
final_offset_z = float(input("Enter z_final offset: "))

timer = input("Enter timer: ")
number = input("Create trial file: ")
trial_dir = "trial_" + number +"/"
intensity_dir = "intensity_" + input("Create intensity directory: ")
parent_dir = 'trial_seismic_data/'+intensity_dir+"/"
#folder = parent_dir+trial_dir

path = os.path.join(parent_dir, trial_dir)

try:
    os.makedirs(path)
except OSError as error:
    print(error)

def safe_exit(signum, frame):
    exit(1)

class Logger():
    def __init__(self):
        self.data_dict = {}
        self.data2_dict = {}
        self.data3_dict = {}
        self.data4_dict = {}

    def collect_data(self):
        '''collect data of accel_1 and assign to class variable'''
        self.data_dict['accel_1'] = (datetime.now(), *accel_1.acceleration, accel_1.data_rate)
        '''collect data of accel_2 and assign to class variable'''
        self.data_dict['accel_2'] = (datetime.now(), *accel_2.acceleration, accel_2.data_rate)
        '''collect data of accel_3 and assign to class variable'''
        self.data_dict['accel_3'] = (datetime.now(), *accel_3.acceleration, accel_3.data_rate)
        '''collect data of accel_4 and assign to class variable'''
        self.data_dict['accel_4'] = (datetime.now(), *accel_4.acceleration, accel_4.data_rate)

    def collect_ave_data(self):
        global ave_accel_x,ave_accel_y,ave_accel_z,magnitude, str_magnitude# , mean_magnitude
        '''collect ave_data of all accel_x and assign to class variable'''
        ave_accel_x = ((accel_1.acceleration[0]+accel_2.acceleration[0]+accel_3.acceleration[0]+accel_4.acceleration[0])/4)-final_offset_x
        self.data3_dict['ave_accel_x'] = (datetime.now(), ave_accel_x)
        '''collect ave_data of all accel_y and assign to class variable'''
        ave_accel_y = ((accel_1.acceleration[1]+accel_2.acceleration[1]+accel_3.acceleration[1]+accel_4.acceleration[1])/4)-final_offset_y
        self.data3_dict['ave_accel_y'] = (datetime.now(), ave_accel_y)
        '''collect ave_data of all accel_z and assign to class variable'''
        ave_accel_z = ((accel_1.acceleration[2]+accel_2.acceleration[2]+accel_3.acceleration[2]+accel_4.acceleration[2])/4)-final_offset_z
        self.data3_dict['ave_accel_z'] = (datetime.now(), ave_accel_z)
        magnitude = ((ave_accel_x**2)+(ave_accel_y**2)+(ave_accel_z**2))**(1/2)
        str_magnitude = str(magnitude)
        self.data3_dict['accel_magnitude'] = (datetime.now(), magnitude)
        # ave_magnitude = (datetime.now(), magnitude/len(append.magnitude))
        # self.data4_dict['mean_magnitude'] = (datetime.now(), mean_magnitude)


    def thingspeak(self):
        global ave_accel_x, ave_accel_y, ave_accel_z,magnitude
        sensor_readings = {'api_key':'QDHGPCKLJ547BKZR', 'field1':ave_accel_x,'field2':ave_accel_y, 'field3':ave_accel_z, 'field4':magnitude}
        url = 'https://api.thingspeak.com/update.json'
        requests_headers = {'Content-Type':'application/json'}
        print(ave_accel_x,ave_accel_y,ave_accel_z,magnitude)
        print("Sending EEWS data to thingspeak.com")

        response = requests.post(url,sensor_readings,requests_headers)
        print("Response code:", response.status_code)
        print("Response code:", response.text)

    def print_data(self):
        '''print select data with formatting'''
        print('*'*70)
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x1:{1:,.3f}, accel_y1:{2:,.3f}, accel_z1:{3:,.3f}".format(*self.data_dict['accel_1']))
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x2:{1:,.3f}, accel_y2:{2:,.3f}, accel_z2:{3:,.3f}".format(*self.data_dict['accel_2']))
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x3:{1:,.3f}, accel_y3:{2:,.3f}, accel_z3:{3:,.3f}".format(*self.data_dict['accel_3']))
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x4:{1:,.3f}, accel_y4:{2:,.3f}, accel_z4:{3:,.3f}".format(*self.data_dict['accel_4']))

    def data_logger(self):
        for file, data in self.data_dict.items():
            with open(path + file + '.csv', 'a+', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(data)

    def directory(self):
        '''collect data of accel_1 and assign to class variable'''
        self.data2_dict['path'] = (intensity_dir, trial_dir)
        for file, data in self.data2_dict.items():
            with open(path + file + '.csv', 'w') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(data)

    def ave_data_logger(self):
        global magnitude, mean_magnitude

        for file, data in self.data3_dict.items():
            with open(path + file + '.csv', 'a+', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(data)

            with open(path + file + '.csv', 'r', newline='') as sensor_data:
                sensor_reader = csv.reader(sensor_data)
                for row in sensor_reader:
                    magnitude_data.append(float(row[1]))

                mean_magnitude = sum(magnitude_data)/len(magnitude_data)

                print("Mean magnitude_data: ", mean_magnitude)
                self.data4_dict['mean_magnitude'] = (datetime.now(), mean_magnitude)
                for file, data in self.data4_dict.items():
                    with open(path  + file +'.csv', 'a+', newline='') as mean_mag_data:
                        csv_writer = csv.writer(mean_mag_data)
                        csv_writer.writerow(data)




    # def earthquake_detection(self):

#         accel_1.enable_motion_detection(threshold = 10)
#         motion_1 = str(accel_1.events["motion"])

#         accel_2.enable_motion_detection(threshold = 10)
#         motion_2 = str(accel_2.events["motion"])

#         accel_3.enable_motion_detection(threshold = 10)
#         motion_3 = str(accel_3.events["motion"])

#         accel_4.enable_motion_detection(threshold = 10)
#         motion_4 = str(accel_4.events["motion"])

#         if all(motion == 'True' for motion in (motion_1, motion_2, motion_3, motion_4)):
#             print(datetime.now(), motion_1, motion_2, motion_3, motion_4)
#             eq_detected()
#             red_led()
#         elif all(motion == 'False' for motion in (motion_1, motion_2, motion_3, motion_4)):
#             print(motion_1, motion_2, motion_3, motion_4)
#             blue_led()
#             red_led_off()
#         else:
#             no_eq_detected()
#             print("no motion detected")


def main():
    while reading:
        logger = Logger()
        logger.collect_data()
        logger.collect_ave_data()
        logger.directory()
        logger.data_logger()
        logger.ave_data_logger()
        logger.thingspeak()
        logger.print_data()
#         logger.earthquake_detection()
        sleep(float(timer))

def earthquake_detection():
    while reading:
        global intensity_level
        global magnitude
        if 0.50 <= magnitude >= 1:
            t_value = 18
            intensity_level = 1
            accel_1.enable_motion_detection(threshold = t_value)
            motion_1 = str(accel_1.events["motion"])
            accel_2.enable_motion_detection(threshold = t_value)
            motion_2 = str(accel_2.events["motion"])
            accel_3.enable_motion_detection(threshold = t_value)
            motion_3 = str(accel_3.events["motion"])
            accel_4.enable_motion_detection(threshold = t_value)
            motion_4 = str(accel_4.events["motion"])
            if all(motion == 'True' for motion in (motion_1, motion_2, motion_3, motion_4)):
                print(datetime.now(), motion_1, motion_2, motion_3, motion_4)
                eq_detected()
                red_led()
            elif all(motion == 'False' for motion in (motion_1, motion_2, motion_3, motion_4)):
                print(motion_1, motion_2, motion_3, motion_4)
                no_eq_detected()
                blue_led()
                red_led_off()
            else:
                no_eq_detected()
                blue_led()
                red_led_off()
                print("no motion detected")
        elif 1 <= magnitude >= 1.5:
            t_value = 10
            intensity_level = 2
            accel_1.enable_motion_detection(threshold = t_value)
            motion_1 = str(accel_1.events["motion"])
            accel_2.enable_motion_detection(threshold = t_value)
            motion_2 = str(accel_2.events["motion"])
            accel_3.enable_motion_detection(threshold = t_value)
            motion_3 = str(accel_3.events["motion"])
            accel_4.enable_motion_detection(threshold = t_value)
            motion_4 = str(accel_4.events["motion"])
            if all(motion == 'True' for motion in (motion_1, motion_2, motion_3, motion_4)):
                print(datetime.now(), motion_1, motion_2, motion_3, motion_4)
                eq_detected()
                red_led()

            else:
                no_eq_detected()
                blue_led()
                red_led_off()
                print("no motion detected")
        elif 1.50 <= magnitude >= 2:
            t_value = 10
            intensity_level = 3
            accel_1.enable_motion_detection(threshold = t_value)
            motion_1 = str(accel_1.events["motion"])
            accel_2.enable_motion_detection(threshold = t_value)
            motion_2 = str(accel_2.events["motion"])
            accel_3.enable_motion_detection(threshold = t_value)
            motion_3 = str(accel_3.events["motion"])
            accel_4.enable_motion_detection(threshold = t_value)
            motion_4 = str(accel_4.events["motion"])
            if all(motion == 'True' for motion in (motion_1, motion_2, motion_3, motion_4)):
                print(datetime.now(), motion_1, motion_2, motion_3, motion_4)
                eq_detected()
                red_led()

            else:
                no_eq_detected()
                blue_led()
                red_led_off()
                print("no motion detected")
        elif 3 <= magnitude >= 4:
            t_value = 10
            intensity_level = 4
            accel_1.enable_motion_detection(threshold = t_value)
            motion_1 = str(accel_1.events["motion"])
            accel_2.enable_motion_detection(threshold = t_value)
            motion_2 = str(accel_2.events["motion"])
            accel_3.enable_motion_detection(threshold = t_value)
            motion_3 = str(accel_3.events["motion"])
            accel_4.enable_motion_detection(threshold = t_value)
            motion_4 = str(accel_4.events["motion"])
            if all(motion == 'True' for motion in (motion_1, motion_2, motion_3, motion_4)):
                print(datetime.now(), motion_1, motion_2, motion_3, motion_4)
                eq_detected()
                red_led()
            else:
                no_eq_detected()
                blue_led()
                red_led_off()
                print("no motion detected")
        else:
            pass

def intensity_pred():
    # while reading:
    global message1
    global message2
    global magnitude
    global intensity_level
    # print(magnitude, intensity_level)
   #  if accel_1.acceleration[0] >= 1:
#         intensity_level = 1
#         message1 = "EQ Warning!"
#         message2 = "Intensity: " + intensity_level
#         print(message1 + message2)
#         lcd.text(message1, 1)
#         lcd.text(message2, 2)
#         sleep(10)
#         lcd.clear()
#     else:
    if 0.50 <= magnitude >= 1:
        message1 = "EQ Warning!"
        message2 = "Intensity: " + str(intensity_level)
        print(message1 + message2)
        lcd.text(message1, 1)
        lcd.text(message2, 2)
        sleep(5)
        lcd.clear()
    elif 1 <= magnitude >= 1.5:
        message1 = "EQ Warning!"
        message2 = "Intensity: " + str(intensity_level)
        print(message1 + message2)
        lcd.text(message1, 1)
        lcd.text(message2, 2)
        sleep(5)
        lcd.clear()
    elif 1.5 <= magnitude >= 2:
        message1 = "EQ Warning!"
        message2 = "Intensity: " + str(intensity_level)
        print(message1 + message2)
        lcd.text(message1, 1)
        lcd.text(message2, 2)
        sleep(5)
        lcd.clear()
    elif 2 <= magnitude >= 2.5:
        message1 = "EQ Warning!"
        message2 = "Intensity: " + str(intensity_level)
        print(message1 + message2)
        lcd.text(message1, 1)
        lcd.text(message2, 2)
        sleep(5)
        lcd.clear()
    # elif magnitude >= 0.40:
#         message1 = "EQ Warning!"
#         message2 = "Intensity: " + str(intensity_level)
#         print(message1 + message2)
#         lcd.text(message1, 1)
#         lcd.text(message2, 2)
#         sleep(5)
#         lcd.clear()
#     elif magnitude >= 0.45:
#         message1 = "EQ Warning!"
#         message2 = "Intensity: " + str(intensity_level)
#         print(message1 + message2)
#         lcd.text(message1, 1)
#         lcd.text(message2, 2)
#         sleep(5)
#         lcd.clear()
#     elif magnitude >= 0.50:
#         message1 = "EQ Warning!"
#         message2 = "Intensity: " + str(intensity_level)
#         print(message1 + message2)
#         lcd.text(message1, 1)
#         lcd.text(message2, 2)
#         sleep(5)
#         lcd.clear()
#     elif magnitude >= 0.55:
#         message1 = "EQ Warning!"
#         message2 = "Intensity: " + str(intensity_level)
#         print(message1 + message2)
#         lcd.text(message1, 1)
#         lcd.text(message2, 2)
#         sleep(5)
#         lcd.clear()
#     elif magnitude >= 0.60:
#         message1 = "EQ Warning!"
#         message2 = "Intensity: " + str(intensity_level)
#         print(message1 + message2)
#         lcd.text(message1, 1)
#         lcd.text(message2, 2)
#         sleep(5)
#         lcd.clear()
#     elif magnitude >= 0.65:
#         message1 = "EQ Warning!"
#         message2 = "Intensity: " + str(intensity_level)
#         print(message1 + message2)
#         lcd.text(message1, 1)
#         lcd.text(message2, 2)
#         sleep(5)
#         lcd.clear()
#     elif magnitude >= 0.70:
#         message1 = "EQ Warning!"
#         message2 = "Intensity: " + str(intensity_level)
#         print(message1 + message2)
#         lcd.text(message1, 1)
#         lcd.text(message2, 2)
#         sleep(5)
#         lcd.clear()
    else:
        message1 = "Seismic Logging..."
        message2 = "No EQ Alert!"
        print(message1 + message2)
        lcd.text(message1, 1)
        lcd.text(message2, 2)


def display_alert():
    while reading:
        intensity_pred()
        sleep(0.05)


signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
    reader = Thread(target=main, daemon=True)
    lcd_alert = Thread(target=display_alert, daemon=True)
    led_indicator1 = Thread(target=green_led, daemon=True)
    eq_detect = Thread(target=earthquake_detection, daemon=True)
    i_predict = Thread(target=intensity_pred, daemon=True)


    reader.start()
    lcd_alert.start()
    led_indicator1.start()
    eq_detect.start()
    pause()

except KeyboardInterrupt:
    pass

finally:
    reading = False
    sleep(0.05)
    lcd.clear()

# x = 0.32
# y = -0.37
# z = 9.65