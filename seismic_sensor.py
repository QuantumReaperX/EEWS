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
# accelerometer = adafruit_adxl34x.ADXL345(i2c)

now = datetime.now()

x_raw_data = []
y_raw_data = []
z_raw_data = []

class Logger:
    def __init__(self):
        self.data_dict = {}

    def collect_data(self):
        '''collect data of accel_1 and assign to class variable'''
        self.data_dict['accel_1'] = (now, *accel_1.acceleration)
        '''collect data of accel_2 and assign to class variable'''
        self.data_dict['accel_2'] = (now, *accel_2.acceleration)
        '''collect data of accel_3 and assign to class variable'''
        self.data_dict['accel_3'] = (now, *accel_3.acceleration)
        '''collect data of accel_4 and assign to class variable'''
        self.data_dict['accel_4'] = (now, *accel_4.acceleration)

    def print_data(self):
        '''print select data with formatting'''
        print('*'*70)
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x1:{1:,.3f}, accel_y1:{2:,.3f}, accel_z1:{3:,.3f}".format(*self.data_dict['accel_1']))
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x2:{1:,.3f}, accel_y2:{2:,.3f}, accel_z2:{3:,.3f}".format(*self.data_dict['accel_2']))
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x3:{1:,.3f}, accel_y3:{2:,.3f}, accel_z3:{3:,.3f}".format(*self.data_dict['accel_3']))
        print("{0:%Y-%m-%d-%H:%M:%S} , accel_x4:{1:,.3f}, accel_y4:{2:,.3f}, accel_z4:{3:,.3f}".format(*self.data_dict['accel_4']))


#     def log_seismicdata(self):
#         '''log seismic data into separate file'''
#         for file, data in self.data_dict.items():
#             with open('seismic_data/' + file + '.csv', 'w', newline='') as csv_file:
#                 fieldnames = ['Date/Time','Acceleration_x', 'Acceleration_y', 'Acceleration_z']
#                 csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames) 
#                 csv_writer.writeheader()               
#                 info = {"Date/Time":data[0],"Acceleration_x":data[1],"Acceleration_y":data[2], "Acceleration_z":data[3]}
#                 csv_writer.writerow(info)
                
    def data_logger(self):
        for file, data in self.data_dict.items():
            with open('seismic_data/' + file + '.csv', 'a+', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(data)
                
    def get_raw_csv(self):
        for file, data in self.data_dict.items():
           with open('seismic_data/' + file + '.csv', 'r') as sensor_data:
                sensor_reader = csv.reader(sensor_data)
                
                for row in sensor_reader:
#                     print(data)
                    x_raw_data.append(float(row[1]))
                    y_raw_data.append(float(row[2]))
                    z_raw_data.append(float(row[3]))
                
                print("Average x_raw_data: ", sum(x_raw_data)/len(x_raw_data))
                print("Average y_raw_data: ", sum(y_raw_data)/len(y_raw_data))
                print("Average z_raw_data: ", sum(z_raw_data)/len(z_raw_data))               
                        
def main():
    while True:
        logger = Logger()
        logger.collect_data()
#         logger.log_seismicdata()
        logger.data_logger()
        logger.get_raw_csv()
#         logger.print_data()
        sleep(1)


main()


