# This code is an example for controlling the GoPiGo3 Motors
#
# Results:  When you run this program, the GoPiGo3 Motors will rotate back and forth.

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import signal
from easygopigo3 import *
from di_sensors import inertial_measurement_unit
import csv


def Main(): 

    GPG = EasyGoPiGo3() # Create an instance of the GoPiGo3 class. GPG will be the GoPiGo3 object.
    
    # try to init the distance sensor
    try:
        my_distance_sensor = GPG.init_distance_sensor()
    except Exception:
        print("initialization of sensor didn't work")
        pass
    
    GPG.offset_motor_encoder(GPG.MOTOR_LEFT, GPG.get_motor_encoder(GPG.MOTOR_LEFT))
    GPG.offset_motor_encoder(GPG.MOTOR_RIGHT, GPG.get_motor_encoder(GPG.MOTOR_RIGHT))
    
    move = True

    if move is True: 
        

        with open('problem1_pathtrace.csv', mode='w') as csv_file:
            fieldnames = ['Row', 'Encoder', 'Distance']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            GPG.drive_cm(50);
            print("Encoder L: %6d  R: %6d" % (GPG.get_motor_encoder(GPG.MOTOR_LEFT), GPG.get_motor_encoder(GPG.MOTOR_RIGHT)))
            print("Distance reading: " + str(my_distance_sensor.read_mm()))
            writer.writerow({'Row': '1', 'Encoder': str(GPG.get_motor_encoder(GPG.MOTOR_LEFT)) + ' , ' + str(GPG.get_motor_encoder(GPG.MOTOR_RIGHT)) , 'Distance': str(my_distance_sensor.read_mm())})

            GPG.turn_degrees(90, blocking = True)
            GPG.drive_cm(50);
            print("Encoder L: %6d  R: %6d" % (GPG.get_motor_encoder(GPG.MOTOR_LEFT), GPG.get_motor_encoder(GPG.MOTOR_RIGHT)))
            print("Distance reading: " + str(my_distance_sensor.read_mm()))
            writer.writerow({'Row': '2', 'Encoder': str(GPG.get_motor_encoder(GPG.MOTOR_LEFT)) + ' , ' + str(GPG.get_motor_encoder(GPG.MOTOR_RIGHT)) , 'Distance': str(my_distance_sensor.read_mm())})

            GPG.turn_degrees(90, blocking = True)
            GPG.drive_cm(50);
            print("Encoder L: %6d  R: %6d" % (GPG.get_motor_encoder(GPG.MOTOR_LEFT), GPG.get_motor_encoder(GPG.MOTOR_RIGHT)))
            print("Distance reading: " + str(my_distance_sensor.read_mm()))
            writer.writerow({'Row': '3', 'Encoder': str(GPG.get_motor_encoder(GPG.MOTOR_LEFT)) + ' , ' + str(GPG.get_motor_encoder(GPG.MOTOR_RIGHT)) , 'Distance': str(my_distance_sensor.read_mm())})

            GPG.turn_degrees(90, blocking = True)
            GPG.drive_cm(50);
            print("Encoder L: %6d  R: %6d" % (GPG.get_motor_encoder(GPG.MOTOR_LEFT), GPG.get_motor_encoder(GPG.MOTOR_RIGHT)))
            print("Distance reading: " + str(my_distance_sensor.read_mm()))
            writer.writerow({'Row': '4', 'Encoder': str(GPG.get_motor_encoder(GPG.MOTOR_LEFT)) + ' , ' + str(GPG.get_motor_encoder(GPG.MOTOR_RIGHT)) , 'Distance': str(my_distance_sensor.read_mm())})
            
            GPG.turn_degrees(90, blocking = True)
            GPG.stop();
            move = False;

        
if __name__ == "__main__":
    # set up a handler for ignoring the Ctrl+Z commands
    signal.signal(signal.SIGTSTP, lambda signum, frame : print("Press the appropriate key for closing the app."))

    try:
        Main()
    except IOError as error:
        # if the GoPiGo3 is not reachable
        # then print the error and exit
        print(str(error))
        exit(1)

    exit(0)

