import csv
import time
import board
import busio
import adafruit_adxl34x
import adafruit_tca9548a



i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

accelerometer_1 = adafruit_adxl34x.ADXL345(tca[2])
accelerometer_2 = adafruit_adxl34x.ADXL345(tca[3])
accelerometer_3 = adafruit_adxl34x.ADXL345(tca[4])
accelerometer_4 = adafruit_adxl34x.ADXL345(tca[5])

accel_1 = accelerometer_1.acceleration
accel_2 = accelerometer_2.acceleration
accel_3 = accelerometer_3.acceleration
accel_4 = accelerometer_4.acceleration

user_raw_command = ""

x_raw_data = []
y_raw_data = []
z_raw_data = []


# def sensor_raw(accel_number):
# #     print(type(accel_number))
#     return accel_number

def raw_sensor_data(accel_number):
   for i in range(100):
#         print(type(accelerometer_1.acceleration))
#         print(type(accel_number))
        time.sleep(0.05)

def write_raw_csv(accel_number):

    with open('raw_data.csv', 'w+') as sensor_readings:
        fieldnames = ['raw_x','raw_y','raw_z']
        sensor_writer = csv.DictWriter(sensor_readings, fieldnames=fieldnames)
        sensor_writer.writeheader()

        info = {'raw_x':accel_number[0],'raw_y':accel_number[1],'raw_z':accel_number[2]}

        for i in range(100):
            print(accel_number)
            time.sleep(0.05)
            # sensor_writer.writerow([sensor_raw(accel_number)])
            sensor_writer.writerow(info)


#         print(info)
#         time.sleep(1)
#         # sensor_writer.writerow([sensor_raw(accel_number)])
#         sensor_writer.writerow(info)


#         data_row = 10
#         while data_row < 10:
#             print(accel_number)
#             sensor_writer.writerow(info)
#             data_row += 1
#             time.sleep(1)
#             # sensor_writer.writerow([sensor_raw(accel_number)])


def get_raw_csv(accel_number):
    with open('raw_data.csv', 'r') as sensor_data:
        sensor_reader = csv.DictReader(sensor_data)

        for row in sensor_reader:
            x_raw_data.append(float(row['raw_x']))
            y_raw_data.append(float(row['raw_y']))
            z_raw_data.append(float(row['raw_z']))
    print("Average x_raw_data: ", sum(x_raw_data)/len(x_raw_data))
    print("Average y_raw_data: ", sum(y_raw_data)/len(y_raw_data))
    print("Average z_raw_data: ", sum(z_raw_data)/len(z_raw_data))

def get_data_rate(accel_number):
    print(accelerometer_1.data_rate)

def raw_accel_selection(accel_number):
    while True:
        user_raw_command = input("Enter acceleremoter number: ").lower()
        if user_raw_command == "accel_1":
    # #         sensor_raw(accel_1)
            write_raw_csv(accel_1)
            get_raw_csv(accel_1)
    #         raw_sensor_data(accel_1)
    #         get_data_rate(accel_1)
        elif user_raw_command == "accel_2":
    #         sensor_raw(accel_1)
            write_raw_csv(accel_2)
            get_raw_csv(accel_2)
        elif user_raw_command == "accel_3":
    #         sensor_raw(accel_1)
            write_raw_csv(accel_3)
            get_raw_csv(accel_3)
        elif user_raw_command == "accel_4":
    #         sensor_raw(accel_1)
            write_raw_csv(accel_4)
            get_raw_csv(accel_4)
        elif user_raw_command == "help":
            print("""
    accel_1 = to select accelerometer 1
    accel_2 = to select accelerometer 2
    accel_3 = to select accelerometer 3
    accel_4 = to select accelerometer 4
    quit = to exit
    """)
        elif user_raw_command == "quit":
            break
        else:
            print("Not recognized, enter help to see more")




