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


user_command = ""
user_operation = ""

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
        #round(-(z - 250) / 8),  # Z should be '250' at 1g (4mg per bit)
        round(-z),  # Z should be '250' at 1g (4mg per bit)
    )
    print("Calibrated offsets: ", accel_number.offset)

def set_data_rate(accel_number):
    accel_number._write_register_byte(0x2C,0b0000)
    print('{0} data rate is: {1}'.format(user_command, accel_number.data_rate))

def set_data_range(accel_number):
    accel_number._write_register_byte(0x31,0b00)
    print('{0} data range is: {1}'.format(user_command, accel_number.range))

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
exit = go back to sensor selection
            """)
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
exit = go back to sensor selection
            """)
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
exit = go back to sensor selection
            """)
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
exit = go back to sensor selection
            """)
            elif user_operation == "exit":
                break
            else:
                print("Not recognized operation")
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