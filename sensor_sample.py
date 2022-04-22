'''Sample Test code for each sensor offset, data rate, range'''
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

#accel_1.offset = 0,0,0
print(accel_1.offset)
print(accel_1.data_rate)
print(accel_1.range)

while True:
    print(accel_1.acceleration)
    time.sleep(1)

