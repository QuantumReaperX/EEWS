'''For trial plotting'''
import board
import busio
import adafruit_adxl34x
import adafruit_tca9548a
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
import pandas as pd
i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

accel_1 = adafruit_adxl34x.ADXL345(tca[2])
accel_2 = adafruit_adxl34x.ADXL345(tca[3])
accel_3 = adafruit_adxl34x.ADXL345(tca[4])
accel_4 = adafruit_adxl34x.ADXL345(tca[5])

# accel_1_offset = ""
# accel_2_offset = ""
# accel_3_offset = ""
# accel_4_offset = ""

# while True:
#     try:
#         z_average_offset = float(input("Enter value for average offset_z: " ))
#         y_average_offset = float(input("Enter value for average offset_y: " ))
#         x_average_offset = float(input("Enter value for average offset_x: " ))
#         break
#     except ValueError:
#         print("Float/Integer only applied")
#         raise


# Parameters
x_len = 100       # Number of points to display
y_range = [-20, 20]  #Range of possible Y values to display

# Create figure for plotting
# fig = plt.figure(figsize=(20, 40), constrained_layout=True)
# spec = fig.add_gridspec(ncols=3, nrows=3)
# ax1 = fig.add_subplot(spec[0,0])
# ax2 = fig.add_subplot(spec[1,0])
# ax3 = fig.add_subplot(spec[-1,0])

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex='col', sharey='row', figsize=(13.5,6), constrained_layout=True)

xs = list(range(0, 100))
ys1 = [0] * x_len
ys2 = [0] * x_len
ys3 = [0] * x_len


ax1.set_ylim(y_range)
ax2.set_ylim(y_range)
ax3.set_ylim(y_range)


# Add labels
plt.suptitle('Seismic Acceleration')
fig.text(0.01, 0.5,'Amplitude(m/s$^2$)',  va='center', rotation='vertical')
# plt.title('Seismic Acceleration')
plt.xlabel('Time(s)')
ax1.set_ylabel('Acceleration_Z')
ax2.set_ylabel('Acceleration_Y')
ax3.set_ylabel('Acceleration_X')

# Create a blank line. We will update the line in animate
line1, = ax1.plot(xs, ys1, color='red', marker='o')
line2, = ax2.plot(xs, ys2, color='blue', marker='o')
line3, = ax3.plot(xs, ys3, color='orange', marker='o')

# def ave_offset_accel_1():
#     with open('offset_data/mean_accel_1.csv', 'r') as sensor1_data:
#         sensor1_reader = csv.reader(sensor1_data)
#         for row in sensor1_reader:
#             global accel_1_offset
#             accel_1_offset = row
#             print(type(accel_1_offset[0]))

# def ave_offset_accel_2():
#     with open('offset_data/mean_accel_2.csv', 'r') as sensor2_data:
#         sensor2_reader = csv.reader(sensor2_data)
#         for row in sensor2_reader:
#             global accel_2_offset
#             accel_2_offset = row

# def ave_offset_accel_3():
#     with open('offset_data/mean_accel_3.csv', 'r') as sensor3_data:
#         sensor3_reader = csv.reader(sensor3_data)
#         for row in sensor3_reader:
#             global accel_3_offset
#             accel_3_offset = row

# def ave_offset_accel_4():
#     with open('offset_data/mean_accel_4.csv', 'r') as sensor4_data:
#         sensor4_reader = csv.reader(sensor1_data)
#         for row in sensor4_reader:
#             global accel_4_offset
#             accel_4_offset = row

# This function is called periodically from FuncAnimation
def animate(i, ys1, ys2, ys3):

    # data1 = pd.read_csv('offset_data/mean_accel_1.csv')
#     accel_1_offset = data1.iloc[0,0]
#     print(accel_1_offset)
#     data2 = pd.read_csv('offset_data/mean_accel_2.csv')
#     accel_2_offset = data2
#     data3 = pd.read_csv('offset_data/mean_accel_3.csv')
#     accel_3_offset = data3
#     data4 = pd.read_csv('offset_data/mean_accel_4.csv')
#     accel_4_offset = data4
    with open('offset_data/mean_accel_1.csv', 'r') as sensor1_data:
        sensor1_reader = csv.reader(sensor1_data)
        for row1 in sensor1_reader:
            accel_1_offset = row1
    with open('offset_data/mean_accel_2.csv', 'r') as sensor2_data:
        sensor2_reader = csv.reader(sensor2_data)
        for row2 in sensor2_reader:
            accel_2_offset = row2
    with open('offset_data/mean_accel_3.csv', 'r') as sensor3_data:
        sensor3_reader = csv.reader(sensor3_data)
        for row3 in sensor3_reader:
            accel_3_offset = row3
    with open('offset_data/mean_accel_4.csv', 'r') as sensor4_data:
        sensor4_reader = csv.reader(sensor4_data)
        for row4 in sensor4_reader:
            accel_4_offset = row4

    all_accel_ave_z =(
        (accel_1.acceleration[2]-float(accel_1_offset[2])
        +accel_2.acceleration[2]-float(accel_2_offset[2])
        +accel_3.acceleration[2]-float(accel_3_offset[2])
        +accel_4.acceleration[2]-float(accel_4_offset[2]) )/4)

    all_accel_ave_y =(
        (accel_1.acceleration[1]-float(accel_1_offset[1])
        +accel_2.acceleration[1]-float(accel_2_offset[1])
        +accel_3.acceleration[1]-float(accel_3_offset[1])
        +accel_4.acceleration[1]-float(accel_4_offset[1]) )/4)

    all_accel_ave_x =(
        (accel_1.acceleration[0]-float(accel_1_offset[0])
        +accel_2.acceleration[0]-float(accel_2_offset[0])
        +accel_3.acceleration[0]-float(accel_3_offset[0])
        +accel_4.acceleration[0]-float(accel_4_offset[0]) )/4)

#     Add y to list the mean of all sensors
    ys1.append(all_accel_ave_z)
    ys2.append(all_accel_ave_y)
    ys3.append(all_accel_ave_x)

#     ys2.append((accel_1.acceleration[1]+accel_2.acceleration[1]+accel_3.acceleration[1]+accel_4.acceleration[1])/4)#-y_average_offset)
#     ys3.append((accel_1.acceleration[0]+accel_2.acceleration[0]+accel_3.acceleration[0]+accel_4.acceleration[0])/4)#-x_average_offset)

#     Limit y list to set number of items
    ys1 = ys1[-x_len:]
    ys2 = ys2[-x_len:]
    ys3 = ys3[-x_len:]

#     Update line with new Y values
    line1.set_ydata(ys1)
    line2.set_ydata(ys2)
    line3.set_ydata(ys3)

    return line1, line2, line3,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys1,ys2,ys3,),
    interval=50, #0.05
    blit=True)
plt.show()