import RPi.GPIO as GPIO
from time import sleep

import motor_driver
GPIO.setmode(GPIO.BOARD)

import serial
# import ultrasonic
import random


class scooterController:

    def __init__(self):
        # pwm.stop()
        
        GPIO.setup(11,GPIO.OUT) #change this pin as needed
        
        self.pwm = GPIO.PWM(11,50) #set duty cycle to 50Hz or 20 ms
        #operating frequency is 50-330Hz

        #motor operates from 500-2500 microseconds or 0.5-2.5ms
        #motor nuetral is at 1500 microseconds or 1.5ms

        #set motor to neutral
        self.pwm.start(7.5) #sets pwm to 7.5% of duty cycle, or 1.5ms
        self.heading = 0
        
        sleep(1)
        print("resetting header")

        # Assigned Pins:
        # S1: Blue(TX) to GPIO14, Green(RX) to GPIO15
        # S2: TX to GPIO4, RX to GPIO5
        # S3: TX to GPIO8, RX to GPIO9
        # S4: TX to GPIO12, RX to GPIO13
        # Setting serial ports for each sensors, skip AMA1
        # self.ports=[
        #     serial.Serial("/dev/ttyAMA0",9600,timeout=0.1),
            # serial.Serial("/dev/ttyAMA3",9600,timeout=0.1),
            # serial.Serial("/dev/ttyAMA4",9600,timeout=0.1),
            # serial.Serial("/dev/ttyAMA5",9600,timeout=0.1)
        # ]
        # Flushing ports and waiting for sensors to stabilize
        # print("Resetting serial ports")
        # for ser in self.ports:
        #     ser.reset_input_buffer()
        # sleep(1.0)

        self.distances = []


    def controlCommand(self,command):
        print(f"Controller Read: {command}")
        
        # self.distances = ultrasonic.distance_read(self.ports)
        self.distances = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
        
        match command:

            case "RIGHT":
                self.heading = self.heading -10
                if self.heading < -67.5:
                    self.heading = -60
                cycle = motor_driver.turn_to_angle(self.heading)
                self.pwm.ChangeDutyCycle(cycle)
                print(f"Right: {self.heading}  {cycle}")
                
            case "CENTER":
                self.heading = 0
                cycle = motor_driver.turn_to_angle(self.heading)
                self.pwm.ChangeDutyCycle(cycle)
                print(f"Center: {self.heading}  {cycle}")
                
            case "LEFT":
                self.heading = self.heading + 10
                if self.heading > 67.5:
                    self.heading = 60
                cycle = motor_driver.turn_to_angle(self.heading)
                self.pwm.ChangeDutyCycle(cycle)
                print(f"Left: {self.heading}  {cycle}")
            case "FORWARD":
                # call the actual gas pedal thing here
                print(f"Calling Drive Forward. Heading: {self.heading}")
                sleep(1)
                # pwm.stop()
                # GPIO.cleanup()
            case "REVERSE":
                # call the actual gas pedal thing here
                print(f"Calling Drive Backward. Heading: {self.heading}")
                sleep(1)
                # pwm.stop()
                # GPIO.cleanup()

        return command,self.heading,self.distances


if __name__ == "__main__":

    cont = scooterController()
    while True:
        resp = ""
        
        selection = input("Make a selection: ")
        if selection == "EXIT":
            break
        else:
            resp = cont.controlCommand(selection)
            print(resp)
        
    cont.pwm.stop()
    # cont.GPIO.cleanup() 
    print("Goodbye")
        












