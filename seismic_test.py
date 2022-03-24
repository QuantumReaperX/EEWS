# import csv
import time
import datetime as dt
import board
import busio
import adafruit_adxl34x
import adafruit_tca9548a
from datetime import datetime
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
#import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation
# from signal import signal, SIGTERM, SIGHUP, pause
# from rpi_lcd import LCD
# from gpiozero import Buzzer


i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

accel_1 = adafruit_adxl34x.ADXL345(tca[2])
accel_2 = adafruit_adxl34x.ADXL345(tca[3])
#accel_3 = adafruit_adxl34x.ADXL345(tca[4])
accel_4 = adafruit_adxl34x.ADXL345(tca[5])
#accelerometer = adafruit_adxl34x.ADXL345(i2c)

#accel_1._write_register_byte(0x2C,0b1111)
#accel_1._write_register_byte(0x31,0b11)
#now = datetime.now()
plt.style.use('fivethirtyeight')
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)



xs = []
ys1 = []
ys2 = []
ys3 = []
ys4 = []


fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex='col', sharey='row', figsize=(20, 40))
#ax1.plot(xs, ys1)
#ax2.plot(xs, ys2)

#(accel_x1, accel_y1, accel_z1) = accel_1.acceleration
#(accel_x2, accel_y2, accel_z2) = accel_2.acceleration
#(accel_x3, accel_y3, accel_z3) = accel_3.acceleration
#(accel_x4, accel_y4, accel_z4) = accel_4.acceleration


# # cal_x1 = float(input("Calibrate accel_x1: "))
# # cal_y1 = float(input("Calibrate accel_y1: "))
# # cal_z1 = float(input("Calibrate accel_z1: "))
# # cal_x2 = float(input("Calibrate accel_x2: "))
# # cal_y2 = float(input("Calibrate accel_y2: "))
# # cal_z2 = float(input("Calibrate accel_z2: "))
# cal_x3 = float(input("Calibrate accel_x3: "))
# cal_y3 = float(input("Calibrate accel_y3: "))
# cal_z3 = float(input("Calibrate accel_z3: "))


# acceleration_A = (accel_x1-cal_x1, accel_y1-cal_y1, accel_z1-cal_z1)
# acceleration_B = (accel_x2-cal_x2, accel_y2-cal_y2, accel_z2-cal_z2)
# acceleration_C = (accel_x3-cal_x3, accel_y3-cal_y3, accel_z3-cal_z3)





def animate(i, xs, ys1, ys2, ys3, ys4):

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys1.append(accel_1.acceleration[0])
    ys2.append(accel_1.acceleration[1])
    ys3.append(accel_1.acceleration[2])
    #ys4.append(accel_1.acceleration)
    print(accel_1.acceleration)
    print(accel_1.data_rate, accel_1.range)
    #time.sleep(0.0001)

    # Limit x and y lists to 20 items
    xs = xs[-25:]
    ys1 = ys1[-25:]
    ys2 = ys2[-25:]
    ys3 = ys3[-25:]
    #ys4 = ys4[-25:]


    ax1.relim()
    #ax1.set_ylim(top=-100, bottom=100)
    ax1.autoscale()
    ax2.relim()
    ax2.autoscale()
    ax3.relim()
    ax3.autoscale()
    #ax4.relim()
    #ax4.autoscale()

    # Draw x and y lists
    ax1.cla()
    ax1.plot(xs, ys1, color = 'blue', marker = 'o')
    ax2.cla()
    ax2.plot(xs, ys2, color = 'green', marker = 'o')
    ax3.cla()
    ax3.plot(xs, ys3, color = 'red', marker = 'o')
    #ax4.cla()
    #ax4.plot(xs, ys4)



    ytics = range(-20, 25, 5)
    plt.suptitle('Acceleration of Accelerometer 1')
    #plt.ylabel('Magnitude(m/s$^2$)')
    ax1.set_yticks(ytics)
    ax1.set_ylabel('x-axis')
    ax2.set_yticks(ytics)
    ax2.set_ylabel('y-axis')
    ax3.set_yticks(ytics)
    ax3.set_ylabel('z-axis')
    #ax4.set_yticks(ytics)
    ax4.set_ylabel('xyz-axis')
    ax1.set_yticklabels(ytics)
    ax2.set_yticklabels(ytics)
    ax3.set_yticklabels(ytics)
    #ax4.set_yticklabels(ytics)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.xlabel('Time(s)')


ani = FuncAnimation(fig, animate, fargs=(xs, ys1, ys2, ys3, ys4), interval=1000)
#plt.tight_layout()
plt.show()