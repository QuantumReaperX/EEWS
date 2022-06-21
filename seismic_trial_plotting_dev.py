'''For trial plotting'''
# import board
# import busio
# import adafruit_adxl34x
# import adafruit_tca9548a
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
import requests
import pandas as pd
# from numpy import mean
# from seismic_sensor_trial_dev import path, file

# i2c = busio.I2C(board.SCL, board.SDA)
# tca = adafruit_tca9548a.TCA9548A(i2c)

# accel_1 = adafruit_adxl34x.ADXL345(tca[2])
# accel_2 = adafruit_adxl34x.ADXL345(tca[3])
# accel_3 = adafruit_adxl34x.ADXL345(tca[4])
# accel_4 = adafruit_adxl34x.ADXL345(tca[5])

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

number = input("Enter trial number: ")

# Parameters
x_len = 100       # Number of points to display
y_range = [-12, 12]  #Range of possible Y values to display

# Create figure for plotting
# fig = plt.figure(figsize=(20, 40), constrained_layout=True)
# spec = fig.add_gridspec(ncols=3, nrows=3)
# ax1 = fig.add_subplot(spec[0,0])
# ax2 = fig.add_subplot(spec[1,0])
# ax3 = fig.add_subplot(spec[-1,0])

# fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, sharex='col', sharey='row', figsize=(13.5,6), constrained_layout=True)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, sharex='col', sharey='row', figsize=(18,9), constrained_layout=True)

xs = list(range(0, 100))
ys1 = [0] * x_len
ys2 = [0] * x_len
ys3 = [0] * x_len
ys4 = [0] * x_len


ax1.set_ylim(y_range)
ax2.set_ylim(y_range)
ax3.set_ylim(y_range)
ax4.set_ylim(y_range)


# Add labels
plt.suptitle('Seismic Acceleration')
fig.text(0.01, 0.5,'Amplitude(m/s$^2$)',  va='center', rotation='vertical')
# plt.title('Seismic Acceleration')
plt.xlabel('Time(s)')
ax1.set_ylabel('Acceleration_Z')
ax2.set_ylabel('Acceleration_Y')
ax3.set_ylabel('Acceleration_X')
ax4.set_ylabel('Magnitude')

# Create a blank line. We will update the line in animate
line1, = ax1.plot(xs, ys1, color='red', marker='o')
line2, = ax2.plot(xs, ys2, color='blue', marker='o')
line3, = ax3.plot(xs, ys3, color='orange', marker='o')
line4, = ax4.plot(xs, ys4, color='black', marker='o')

# This function is called periodically from FuncAnimation
def animate(i, ys1, ys2, ys3, ys4):
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

   #  for file, data in self.data_dict.items():
#         with open(path + file + '.csv', 'a+', newline='') as csv_file:
#             csv_writer = csv.writer(csv_file)
#             csv_writer.writerow(data)

    with open('trial_seismic_data/intensity_tester/trial_'+number+'/ave_accel_x.csv', 'r') as ave_accel_x_data:
        ave_accel_x_data_reader = csv.reader(ave_accel_x_data)
        for row in ave_accel_x_data_reader:
            ave_accel_x = row

    with open('trial_seismic_data/intensity_tester/trial_'+number+'/ave_accel_y.csv', 'r') as ave_accel_x_data:
        ave_accel_x_data_reader = csv.reader(ave_accel_x_data)
        for row in ave_accel_x_data_reader:
            ave_accel_y = row

    with open('trial_seismic_data/intensity_tester/trial_'+number+'/ave_accel_z.csv', 'r') as ave_accel_x_data:
        ave_accel_x_data_reader = csv.reader(ave_accel_x_data)
        for row in ave_accel_x_data_reader:
            ave_accel_z = row

    all_accel_ave_x = float(ave_accel_x[1])-(float(accel_1_offset[0])+float(accel_2_offset[0])+float(accel_3_offset[0])+float(accel_4_offset[0]))/4
    print(all_accel_ave_x)
    all_accel_ave_y = float(ave_accel_y[1])-(float(accel_1_offset[1])+float(accel_2_offset[1])+float(accel_3_offset[1])+float(accel_4_offset[1]))/4
    print(all_accel_ave_y)
    all_accel_ave_z = float(ave_accel_z[1])-(float(accel_1_offset[2])+float(accel_2_offset[2])+float(accel_3_offset[2])+float(accel_4_offset[2]))/4
    print(all_accel_ave_z)
    magnitude = ((all_accel_ave_x**2)+(all_accel_ave_y**2)+(all_accel_ave_z**2))**(1/2)
    print(magnitude)

#     all_accel_ave_z =(
#         (accel_1.acceleration[2]-float(accel_1_offset[2])
#         +accel_2.acceleration[2]-float(accel_2_offset[2])
#         +accel_3.acceleration[2]-float(accel_3_offset[2])
#         +accel_4.acceleration[2]-float(accel_4_offset[2]) )/4)--2.3
#     print(all_accel_ave_z)
#     all_accel_ave_y =(
#         (accel_1.acceleration[1]-float(accel_1_offset[1])
#         +accel_2.acceleration[1]-float(accel_2_offset[1])
#         +accel_3.acceleration[1]-float(accel_3_offset[1])
#         +accel_4.acceleration[1]-float(accel_4_offset[1]) )/4)--2.1
#     print(all_accel_ave_y)
#     all_accel_ave_x =(
#         (accel_1.acceleration[0]-float(accel_1_offset[0])
#         +accel_2.acceleration[0]-float(accel_2_offset[0])
#         +accel_3.acceleration[0]-float(accel_3_offset[0])
#         +accel_4.acceleration[0]-float(accel_4_offset[0]) )/4)
#     print(all_accel_ave_x)
#     magnitude = ((all_accel_ave_x**2)+(all_accel_ave_y**2)+(all_accel_ave_z**2))**(1/2)
#     print(magnitude)

   #  sensor_readings = {'api_key':'QDHGPCKLJ547BKZR', 'field1':all_accel_ave_x,'field2':all_accel_ave_y, 'field3':all_accel_ave_z, 'field4':magnitude}
#     url = 'https://api.thingspeak.com/update.json'
#     requests_headers = {'Content-Type':'application/json'}
#     print("Sending EEWS data to thingspeak.com")

#     response = requests.post(url,sensor_readings,requests_headers)
#     print("Response code:", response.status_code)
#     print("Response code:", response.text)

#     Add y to list the mean of all sensors
    ys1.append(all_accel_ave_z)
    ys2.append(all_accel_ave_y)
    ys3.append(all_accel_ave_x)
    ys4.append(magnitude)

#     Limit y list to set number of items
    ys1 = ys1[-x_len:]
    ys2 = ys2[-x_len:]
    ys3 = ys3[-x_len:]
    ys4 = ys4[-x_len:]

#     Update line with new Y values
    line1.set_ydata(ys1)
    line2.set_ydata(ys2)
    line3.set_ydata(ys3)
    line4.set_ydata(ys4)

    return line1, line2, line3, line4,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys1,ys2,ys3,ys4,),
    interval=50, #0.05
    blit=True)
plt.show()