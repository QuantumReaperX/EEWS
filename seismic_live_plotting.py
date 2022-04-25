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
from matplotlib.animation import FuncAnimation



i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

accel_1 = adafruit_adxl34x.ADXL345(tca[2])
accel_2 = adafruit_adxl34x.ADXL345(tca[3])
accel_3 = adafruit_adxl34x.ADXL345(tca[4])
accel_4 = adafruit_adxl34x.ADXL345(tca[5])

xs = []
ys1 = []
ys2 = []
ys3 = []
ys4 = []

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex='col', sharey='row', figsize=(18, 8))

def animate(i, xs, ys1, ys2, ys3, ys4):

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys1.append(accel_1.acceleration)
    ys2.append(accel_2.acceleration)
    ys3.append(accel_3.acceleration)
    ys4.append(accel_4.acceleration)

    # Limit x and y lists to 20 items
    xs = xs[-25:]
    ys1 = ys1[-25:]
    ys2 = ys2[-25:]
    ys3 = ys3[-25:]
    ys4 = ys4[-25:]


    ax1.relim()
    ax1.autoscale()
    ax2.relim()
    ax2.autoscale()
    ax3.relim()
    ax3.autoscale()
    ax4.relim()
    ax4.autoscale()

    # Draw x and y lists
    ax1.cla()
    #ax1.plot(xs, ys1)
    ax1.plot(xs, ys1, color = 'blue', marker = 'o')
    ax2.cla()
    #ax2.plot(xs, ys2)
    ax2.plot(xs, ys2, color = 'green', marker = 'o')
    ax3.cla()
    #ax3.plot(xs, ys3)
    ax3.plot(xs, ys3, color = 'red', marker = 'o')
    ax4.cla()
    #ax4.plot(xs, ys4)
    ax4.plot(xs, ys4, color = 'yellow', marker = 'o')


    ytics = range(-20, 25, 5)
    plt.suptitle('Acceleration of Accelerometers')
    #plt.ylabel('Magnitude(m/s$^2$)')
    ax1.set_yticks(ytics)
    ax1.set_ylabel('accel_1')
    ax2.set_yticks(ytics)
    ax2.set_ylabel('accel_2')
    ax3.set_yticks(ytics)
    ax3.set_ylabel('accel_3')
    ax4.set_yticks(ytics)
    ax4.set_ylabel('accel_4')
    ax1.set_yticklabels(ytics)
    ax2.set_yticklabels(ytics)
    ax3.set_yticklabels(ytics)
    ax4.set_yticklabels(ytics)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.xlabel('Time(s)')


ani = FuncAnimation(fig, animate, fargs=(xs, ys1, ys2, ys3, ys4), interval=100)
plt.show()