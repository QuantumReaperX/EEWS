'''Calibration of adxl345 sensors'''

import time
import board
import busio
import adafruit_adxl34x
import adafruit_tca9548a
from raw_seismic_data import *
from adxl345_mean import *

i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

accel_1 = adafruit_adxl34x.ADXL345(tca[2])
accel_2 = adafruit_adxl34x.ADXL345(tca[3])
accel_3 = adafruit_adxl34x.ADXL345(tca[4])
accel_4 = adafruit_adxl34x.ADXL345(tca[5])

user_command = ""
user_operation = ""
timer = ""

def offset_sensor(accel_number):
    accel_number.offset = 0,0,0
    print(accel_number)
    print("Hold accelerometer flat to set offsets to 0, 0, and -1accelg...")
    time.sleep(1)
    x = accel_number.raw_x
    y = accel_number.raw_y
    z = accel_number.raw_z
    print("Raw x: ", x)
    print("Raw y: ", y)
    print("Raw z: ", z)

    accel_number.offset = (
        round(-x ),
        round(-y ),
        round(-(z - 250) / 8),  # Z should be '250' at 1g (4mg per bit)
    )
    print("Calibrated offsets: ", accel_number.offset)

def reset(accel_number):
    accel_number.offset = 0,0,0
    print('{0} offset is: {1}'.format(user_command, accel_number.offset))
    accel_number.data_rate = 0
    print('{0} data rate is: {1}'.format(user_command, accel_number.data_rate))
    accel_number.range = 0
    print('{0} data range is: {1}'.format(user_command, accel_number.range))

def set_data_rate(accel_number):
    '''
    RATE_3200_HZ: int = const(0b1111)  # 1600Hz Bandwidth   140mA IDD
    RATE_1600_HZ: int = const(0b1110)  # 800Hz Bandwidth    90mA IDD
    RATE_800_HZ: int = const(0b1101)  # 400Hz Bandwidth   140mA IDD
    RATE_400_HZ: int = const(0b1100)  # 200Hz Bandwidth   140mA IDD
    RATE_200_HZ: int = const(0b1011)  # 100Hz Bandwidth   140mA IDD
    RATE_100_HZ: int = const(0b1010)  # 50Hz Bandwidth   140mA IDD
    RATE_50_HZ: int = const(0b1001)  # 25Hz Bandwidth    90mA IDD
    RATE_25_HZ: int = const(0b1000)  # 12.5Hz Bandwidth    60mA IDD
    RATE_12_5_HZ: int = const(0b0111)  # 6.25Hz Bandwidth    50mA IDD
    RATE_6_25HZ: int = const(0b0110)  # 3.13Hz Bandwidth    45mA IDD
    RATE_3_13_HZ: int = const(0b0101)  # 1.56Hz Bandwidth    40mA IDD
    RATE_1_56_HZ: int = const(0b0100)  # 0.78Hz Bandwidth    34mA IDD
    RATE_0_78_HZ: int = const(0b0011)  # 0.39Hz Bandwidth    23mA IDD
    RATE_0_39_HZ: int = const(0b0010)  # 0.20Hz Bandwidth    23mA IDD
    RATE_0_20_HZ: int = const(0b0001)  # 0.10Hz Bandwidth    23mA IDD
    RATE_0_10_HZ: int = const(0b0000)  # 0.05Hz Bandwidth    23mA IDD (default value)
    '''
    try:
        accel_number.data_rate = int(input("Select sensor data rate between 0-15: "))
        #accel_number._write_register_byte(0x2C,0b0000)
        print('{0} data rate is: {1}'.format(user_command, accel_number.data_rate))
    except ValueError:
        exception_alert()

def set_data_range(accel_number):
    '''
    RANGE_16_G: int = const(0b11)  # +/- 16g
    RANGE_8_G: int = const(0b10)  # +/- 8g
    RANGE_4_G: int = const(0b01)  # +/- 4g
    RANGE_2_G: int = const(0b00)  # +/- 2g (default value)
    '''
    try:
        accel_number.range = int(input("Select sensor range between 0-3: "))
        #accel_number._write_register_byte(0x31,0b00)
        print('{0} data range is: {1}'.format(user_command, accel_number.range))
    except ValueError:
        exception_alert()

def sensor_test(accel_number):
    print("Accelerometer Properties:\n\tData rate is: {0}\n\tRange is: {1}\n\tOffset is: {2}" .format(accel_number.data_rate,accel_number.range, accel_number.offset))
    try:
        timer = float(input("Set time of sensor gathering in seconds: "))
        for i in range(10):
            print(accel_number.acceleration)
            time.sleep(timer)
    except ValueError:
        print("Float/Integer is only allowed!")

def set_to_max_rate():
    accel_1.data_rate, accel_2.data_rate, accel_3.data_rate, accel_4.data_rate = 15, 15, 15, 15
    print("Sensors are set to max data_rate of {0}".format(15))

def set_to_max_range():
    accel_1.range, accel_2.range, accel_3.range, accel_4.range, = 3, 3, 3, 3
    print("Sensors are set to max data_range of {0}".format(3))

def set_to_zero_g(accel_number):
    accel_number.offset = 0,0,0
    time.sleep(1)
    print(accel_number)
    print("Hold accelerometer flat to set offsets to 0, 0, and -1accelg...")
    time.sleep(1)
    x = accel_number.raw_x
    y = accel_number.raw_y
    z = accel_number.raw_z
    print("Raw x: ", x)
    print("Raw y: ", y)
    print("Raw z: ", z)

    accel_number.offset = (
        round(-x ),
        round(-y ),
        round(-(z + 250) / 8),  #Z should be '250' at -1g (4mg per bit)
    )
    print("Calibrated offsets: ", accel_number.offset)

def show_property():
    print("*****Initial Sensor Properties*****")
    print("Accel_1: data_rate is {0}, data_range is {1}, offset is {2}".format(accel_1.data_rate, accel_1.range, accel_1.offset))
    print("Accel_2: data_rate is {0}, data_range is {1}, offset is {2}".format(accel_2.data_rate, accel_2.range, accel_2.offset))
    print("Accel_3: data_rate is {0}, data_range is {1}, offset is {2}".format(accel_3.data_rate, accel_3.range, accel_3.offset))
    print("Accel_4: data_rate is {0}, data_range is {1}, offset is {2}".format(accel_4.data_rate, accel_4.range, accel_4.offset))

def exception_alert():
    print("Integer input is only accepted")

while True:
    user_command = input("Enter accel_number or help: ").lower()
    if user_command == "accel_1":
        while True:
            user_operation = input("Enter operation or option: ").lower()
            if user_operation == "offset":
                offset_sensor(accel_1)
            elif user_operation == "rate":
                set_data_rate(accel_1)
            elif user_operation == "range":
                set_data_range(accel_1)
            elif user_operation == "option":
                print("""
offset = sensor offset
rate = sensor data rate
range = sensor range
reset = reset sensor to initial
zero = -1g offset of the sensor
exit = go back to sensor selection
            """)
            elif user_operation == "test":
                sensor_test(accel_1)
            elif user_operation == "zero":
                set_to_zero_g(accel_1)
            elif user_operation == "reset":
                reset(accel_1)
            elif user_operation == "exit":
                break
            else:
                print("Not recognized operation")

    elif user_command == "accel_2":
        while True:
            user_operation = input("Enter operation or option: ").lower()
            if user_operation == "offset":
                offset_sensor(accel_2)
            elif user_operation == "rate":
                set_data_rate(accel_2)
            elif user_operation == "range":
                set_data_range(accel_2)
            elif user_operation == "option":
                print("""
offset = sensor offset
rate = sensor data rate
range = sensor range
reset = reset sensor to initial
zero = -1g offset of the sensor
exit = go back to sensor selection
            """)
            elif user_operation == "test":
                sensor_test(accel_2)
            elif user_operation == "zero":
                set_to_zero_g(accel_2)
            elif user_operation == "reset":
                reset(accel_2)
            elif user_operation == "exit":
                break
            else:
                print("Not recognized operation")
    elif user_command == "accel_3":
        while True:
            user_operation = input("Enter operation or option: ").lower()
            if user_operation == "offset":
                offset_sensor(accel_3)
            elif user_operation == "rate":
                set_data_rate(accel_3)
            elif user_operation == "range":
                set_data_range(accel_3)
            elif user_operation == "option":
                print("""
offset = sensor offset
rate = sensor data rate
range = sensor range
reset = reset sensor to initial
zero = -1g offset of the sensor
exit = go back to sensor selection
            """)
            elif user_operation == "test":
                sensor_test(accel_3)
            elif user_operation == "zero":
                set_to_zero_g(accel_3)
            elif user_operation == "reset":
                reset(accel_3)
            elif user_operation == "exit":
                break
            else:
                print("Not recognized operation")
    elif user_command == "accel_4":
        while True:
            user_operation = input("Enter operation or option: ").lower()
            if user_operation == "offset":
                offset_sensor(accel_4)
            elif user_operation == "rate":
                set_data_rate(accel_4)
            elif user_operation == "range":
                set_data_range(accel_4)
            elif user_operation == "option":
                print("""
offset = sensor offset
rate = sensor data rate
range = sensor range
reset = reset sensor to initial
zero = -1g offset of the sensor
exit = go back to sensor selection
            """)
            elif user_operation == "test":
                sensor_test(accel_4)
            elif user_operation == "zero":
                set_to_zero_g(accel_4)
            elif user_operation == "reset":
                reset(accel_4)
            elif user_operation == "exit":
                break
            else:
                print("Not recognized operation")
    elif user_command == "show":
        show_property()
    elif user_command == "maxrate":
        set_to_max_rate()
    elif user_command == "maxrange":
        set_to_max_range()
    elif user_command == "raw":
        main()
    elif user_command == "mean":
        accel_selection()
    elif user_command == "help":
        print("""
accel_1 = to select accelerometer 1
accel_2 = to select accelerometer 2
accel_3 = to select accelerometer 3
accel_4 = to select accelerometer 4
mean = get mean of all sensor for calibration
show = to show all sensor properties
maxrange = setting to max range sensor property
maxrate = setting to max rate sensor property
quit = to terminate program
""")
    elif user_command == "quit":
        break
    else:
        print("Not recognized, enter help to see more")