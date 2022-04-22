import csv
import time
import datetime
import board
import busio
import adafruit_adxl34x
import adafruit_tca9548a
from datetime import datetime
from time import sleep


i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)

accel_1 = adafruit_adxl34x.ADXL345(tca[2])
accel_2 = adafruit_adxl34x.ADXL345(tca[3])
accel_3 = adafruit_adxl34x.ADXL345(tca[4])
accel_4 = adafruit_adxl34x.ADXL345(tca[5])

'''for testing purpose'''
# accelerometer = adafruit_adxl34x.ADXL345(i2c) 

now = datetime.now()

x_raw_data = []
y_raw_data = []
z_raw_data = []

class Raw_Data_Logger:
    def __init__(self):
        self.data_dict = {}

    def collect_raw_data(self):
        '''collect data of accel_1 and assign to class variable'''
        self.data_dict['raw_accel_1'] = (now, *accel_1.acceleration)
        '''collect data of accel_2 and assign to class variable'''
        self.data_dict['raw_accel_2'] = (now, *accel_2.acceleration)
        '''collect data of accel_3 and assign to class variable'''
        self.data_dict['raw_accel_3'] = (now, *accel_3.acceleration)
        '''collect data of accel_4 and assign to class variable'''
        self.data_dict['raw_accel_4'] = (now, *accel_4.acceleration)

                
    def raw_data_logger(self):
        for file, data in self.data_dict.items():
            with open('raw_seismic_data/' + file + '.csv', 'a+', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(data)


    def print_raw_data(self):
        '''print select data with formatting'''
        print('*'*70)
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x1:{1:,.3f}, accel_y1:{2:,.3f}, accel_z1:{3:,.3f}".format(*self.data_dict['raw_accel_1']))
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x2:{1:,.3f}, accel_y2:{2:,.3f}, accel_z2:{3:,.3f}".format(*self.data_dict['raw_accel_2']))
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x3:{1:,.3f}, accel_y3:{2:,.3f}, accel_z3:{3:,.3f}".format(*self.data_dict['raw_accel_3']))
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x4:{1:,.3f}, accel_y4:{2:,.3f}, accel_z4:{3:,.3f}".format(*self.data_dict['raw_accel_4']))               
                        
def main():
    while True:
        raw_logger = Raw_Data_Logger()
        raw_logger.collect_raw_data()
        raw_logger.raw_data_logger()
        raw_logger.print_raw_data()
        sleep(0.5)

main()


