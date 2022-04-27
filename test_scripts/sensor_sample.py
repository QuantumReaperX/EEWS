'''Sample Test code for each sensor offset, data rate, range'''
import time
import board
import busio
import adafruit_adxl34x
import adafruit_tca9548a
import csv
import adafruit_mpu6050

# import buzzer_test as btest
from gpiozero import Buzzer
from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

# accel_1 = adafruit_mpu6050.MPU6050(tca[2])
accel_2 = adafruit_adxl34x.ADXL345(tca[3])
# accel_3 = adafruit_adxl34x.ADXL345(tca[4])
# accel_3 = adafruit_adxl34x.ADXL345(tca[5])

# accel_2 = adafruit_adxl34x.ADXL345(i2c)
# accel_1.offset = 0,0,0
# accel_1.data_rate = 15
# accel_1.range = 0
# print(accel_1.offset)
# print(accel_1.data_rate)
# print(accel_1.range)

while True:
    
    print(accel_2.acceleration)
    sleep(1)

# buzzer = Buzzer(4)
# 
# def intensity_level():
#     buzzer.on()
#     sleep(0.5)
#     buzzer.off()
#     sleep(0.5)
# # 
# while True:
#     if accel_4.acceleration[2] >= 2:
#         print(accel_4.acceleration[2])
#         intensity_level()
#         print("motion detected!")
#     else:
#         print(accel_4.acceleration[2])
#         print("*"*10)
#         print("no motion detected...")
#     time.sleep(1)

# intensity_level()