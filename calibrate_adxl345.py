import time
import board
import busio
import adafruit_adxl34x

i2c = board.I2C()
#i2c = busio.I2C(board.SCL, board.SDA)
#i2c = board.STEMMA_I2C()  # uses board.SCL and board.SDA

# For ADXL343
#accelerometer = adafruit_adxl34x.ADXL343(i2c)
# For ADXL345
accelerometer = adafruit_adxl34x.ADXL345(i2c)

# accelerometer.offset = 0, 0, 0
# 
# print("Hold accelerometer flat to set offsets to 0, 0, and -1g...")
# time.sleep(1)


# accelerometer.offset = (round(-accelerometer.raw_x / 8),round(-accelerometer.raw_y / 8),round(-(accelerometer.raw_z - 250) / 8))
# print("Calibrated offsets: ", accelerometer.offset)

while True:
    #print("%f %f %f m/s^2" % accelerometer.acceleration)
    print(accelerometer.acceleration)
    time.sleep(0.2)