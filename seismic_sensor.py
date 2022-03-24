import csv
import time
import datetime
import board
import busio
import adafruit_adxl34x
import adafruit_tca9548a
from datetime import datetime
from time import sleep
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import matplotlib.dates as mdates
# from matplotlib.animation import FuncAnimation
# from signal import signal, SIGTERM, SIGHUP, pause
# from rpi_lcd import LCD
# from gpiozero import Buzzer


i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

accel_1 = adafruit_adxl34x.ADXL345(tca[2])
accel_2 = adafruit_adxl34x.ADXL345(tca[3])
accel_3 = adafruit_adxl34x.ADXL345(tca[4])
accel_4 = adafruit_adxl34x.ADXL345(tca[5])
accelerometer = adafruit_adxl34x.ADXL345(i2c)

now = datetime.now()


(accel_x1, accel_y1, accel_z1) = accel_1.acceleration
(accel_x2, accel_y2, accel_z2) = accel_2.acceleration
(accel_x3, accel_y3, accel_z3) = accel_3.acceleration
(accel_x4, accel_y4, accel_z4) = accel_4.acceleration

# cal_x0 = float(input("Calibrate accel_x0: "))
# cal_y0 = float(input("Calibrate accel_y0: "))
# cal_z0 = float(input("Calibrate accel_z0: "))

# lcd = LCD()
# # times = pd.date_range('now', periods=10, freq='1000ms')
# buzzer = Buzzer(17)
#
# plt.style.use('fivethirtyeight')
#
# xs = [] #live time
# ys = [] #sensor reading
#
# def safe_exit(signum, frame):
#         exit(1)
#
class Logger:
    def __init__(self):
        self.data_dict = {}

    #def collect_data(self):
        #'''collect data of accel_1 and assign to class variable'''
         #self.data_dict['accel_1'] = (now, accel_x1, accel_y1, accel_z1)
#
#         '''collect data of accel_2 and assign to class variable'''
#         self.data_dict['accel_2'] = (now, accel_x2, accel_y2, accel_z2)
#
#         '''collect data of accel_3 and assign to class variable'''
# #         self.data_dict['accel_3'] = (now, accel_x3, accel_y3, accel_z3)
        #'''collect data of accel_4 and assign to class variable'''
# #         self.data_dict['accel_4'] = (now, accel_x4, accel_y4, accel_z4)
#
#
#     def animate(i):
#         xs.append(now)
#         ys.append(accel_x0) #di mabgo yung x-axis at nagploplot yung data
#
#
#     plt.cla()
#
#     plt.plot(xs, ys, label='Sensor 1')
#
#     plt.legend(loc='upper left')
#     plt.tight_layout()
#
#     ani = FuncAnimation(plt.gcf(), animate, interval=1000)
#
#     plt.tight_layout()
#     plt.show()
#
    def print_data(self):
        '''print select data with formatting'''
        print(accelerometer.acceleration)
        print(accelerometer.data_rate, accelerometer.range)
        #print("{0:%Y-%m-%d-%H:%M:%S} , accel_x0:{1:,.3f}, accel_y0:{2:,.3f}, accel_z0:{3:,.3f}".format(*self.data_dict['accel_0']))

#         print("{0:%Y-%m-%d-%H:%M:%S} , accel_x1:{1:,.3f}, accel_y1:{2:,.3f}, accel_z1:{3:,.3f}".format(*self.data_dict['accel_1']))
#
#         print("{0:%Y-%m-%d-%H:%M:%S} , accel_x2:{1:,.3f}, accel_y2:{2:,.3f}, accel_z2:{3:,.3f}".format(*self.data_dict['accel_2']))

#         print("{0:%Y-%m-%d-%H:%M:%S} , accel_x3:{1:,.3f}, accel_y3:{2:,.3f}, accel_z3:{3:,.3f}".format(*self.data_dict['accel_3']))

#
#
    def log_seismicdata(self):
        '''log seismic data into separate file'''
        for file, data in self.data_dict.items():
            with open('seismic_data/' + file + '.csv', 'a+', newline='') as csv_file:
#                 fieldnames = ['Date/Time','acceleration_x', 'acceleration_y', 'acceleration_z']
#                 csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames) #paano kaya lagyan ng header yung mga csv kada csvfile?
#                 csv_writer.writeheader()
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(data)
#
#
#     def lcd_display(self): #late ang display sa lcd , ska lang nagdidisplay pag nagclose ng plot
#         try:
#             signal(SIGTERM, safe_exit)
#             signal(SIGHUP, safe_exit)
#             lcd.text("Earthquake Alert", 1)
#             lcd.text("Intensity", 2)
#             pause()
#
#         except KeyboardInterrupt:
#             pass
#
#         finally:
#             lcd.clear()

def main():
    while True:
        logger = Logger()
        #logger.collect_data()
        #logger.log_seismicdata()
#         logger.animate()
        logger.print_data()
#         logger.lcd_display()
        sleep(0.50)


main()


