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

mean_accel_x = []
file = ""
user_command = ""
            
def get_sensor_average():
    with open('raw_seismic_data/' + file + '.csv', 'r') as sensor_data:
        sensor_reader = csv.reader(sensor_data)
        
        for row in sensor_reader:
            x_raw_data.append(float(row[1]))
            y_raw_data.append(float(row[2]))
            z_raw_data.append(float(row[3]))
            
    mean_accel_x = sum(x_raw_data)/len(x_raw_data)
    mean_accel_y = sum(y_raw_data)/len(y_raw_data)
    mean_accel_z = sum(z_raw_data)/len(z_raw_data)
    
    print("Mean x_raw_data: ", mean_accel_x)
    print("Mean y_raw_data: ", mean_accel_y)
    print("Mean z_raw_data: ", mean_accel_z)
        
while True:
    user_command = input("Enter accel_number or help: ").lower()
    if user_command == "accel_1":
        file = "raw_accel_1"
        get_sensor_average()
    elif user_command == "accel_2":
        file = "raw_accel_2"
        get_sensor_average()
    elif user_command == "accel_3":
        file = "raw_accel_3"
        get_sensor_average()
    elif user_command == "accel_4":
        file = "raw_accel_4"
        get_sensor_average()
    elif user_command == "help":
        print("""
accel_1 = to select accelerometer 1
accel_2 = to select accelerometer 2
accel_3 = to select accelerometer 3
accel_4 = to select accelerometer 4
quit = to exit
""")
    elif user_command == "quit":
        break
    else:
        print("Not recognized, enter help to see more")

