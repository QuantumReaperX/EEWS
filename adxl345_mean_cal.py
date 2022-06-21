import time
import board
import busio
import adafruit_adxl34x
import adafruit_tca9548a
import csv

i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

accel_1 = adafruit_adxl34x.ADXL345(tca[2])
accel_2 = adafruit_adxl34x.ADXL345(tca[3])
accel_3 = adafruit_adxl34x.ADXL345(tca[4])
accel_4 = adafruit_adxl34x.ADXL345(tca[5])

x_raw_data = []
y_raw_data = []
z_raw_data = []

file = ""
mean = ""
user_input = ""

def get_cal_sensor_average(file, mean):
    with open('calibrated_seismic_data/' + file + '.csv', 'r') as sensor_data:
        sensor_reader = csv.reader(sensor_data)

        for row in sensor_reader:
            x_raw_data.append(float(row[1]))
            y_raw_data.append(float(row[2]))
            z_raw_data.append(float(row[3]))

    mean_accel_x = sum(x_raw_data)/len(x_raw_data)
    mean_accel_y = sum(y_raw_data)/len(y_raw_data)
    mean_accel_z = sum(z_raw_data)/len(z_raw_data)
    mean_values = (mean_accel_x, mean_accel_y, mean_accel_z)
    print("Mean x_raw_data: ", mean_accel_x)
    print("Mean y_raw_data: ", mean_accel_y)
    print("Mean z_raw_data: ", mean_accel_z)

    with open('offset_data/' + mean + '.csv', 'w') as sensor_data:
        sensor_writer = csv.writer(sensor_data)
        sensor_writer.writerow(mean_values)

    print("Mean values saved to offset_data folder")

def cal_accel_selection():
    while True:
        user_input = input("Enter accel_number to get mean values or help: ").lower()
        if user_input == "accel_1":
            file = "cal_accel_1"
            mean = "mean_cal_accel_1"
            get_cal_sensor_average(file, mean)
        elif user_input == "accel_2":
            file = "cal_accel_2"
            mean = "mean_cal_accel_2"
            get_cal_sensor_average(file, mean)
        elif user_input == "accel_3":
            file = "cal_accel_3"
            mean = "mean_accel_3"
            get_cal_sensor_average(file, mean)
        elif user_input == "accel_4":
            file = "cal_accel_4"
            mean = "mean_cal_accel_4"
            get_cal_sensor_average(file, mean)
        elif user_input == "help":
            print("""
    accel_1 = to select accelerometer 1
    accel_2 = to select accelerometer 2
    accel_3 = to select accelerometer 3
    accel_4 = to select accelerometer 4
    quit = to exit
    """)
        elif user_input == "quit":
            break
        else:
            print("Not recognized, enter help to see more")

# accel_selection()