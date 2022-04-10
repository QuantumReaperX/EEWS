import csv
import time

accel = input("Enter acceleremoter number: ")
accel_1 = 10
accel_2 = 20
accel_3 = 30
accel_4 = 40

def sensor_raw(accel_number):
    return accel_number

def write_raw_csv(accel_number):
    with open('raw_data.csv', 'w+') as sensor_readings:
        fieldnames = ['raw']
        sensor_writer = csv.DictWriter(sensor_readings, fieldnames=fieldnames)
        sensor_writer.writeheader()

        info = {'raw':sensor_raw(accel_number)}

        for i in range(5):  
            print(accel_number)
            # sensor_writer.writerow([sensor_raw(accel_number)])
            sensor_writer.writerow(info)

def get_raw_csv(accel_number):
    with open('raw_data.csv', 'r') as sensor_data:
        sensor_reader = csv.DictReader(sensor_data)
        
        for line in sensor_reader:
            print(line)


match accel:
    case "1":        
        # sensor_raw(accel_1)
        write_raw_csv(accel_1)
        get_raw_csv(accel_1)
    case "2":
        # sensor_raw(accel_2)
        write_raw_csv(accel_2)
        get_raw_csv(accel_2)
    case "3":
        # sensor_raw(accel_3)
        write_raw_csv(accel_3)
        get_raw_csv(accel_3)
    case "4":
        # sensor_raw(accel_4)
        write_raw_csv(accel_4)
        get_raw_csv(accel_4)
    case "exit":
        print('exiting...')
        time.sleep(3)
    case _:
        print('not recognized')
        pass
    
        




