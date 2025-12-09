import RPi.GPIO as GPIO
from time import sleep

import motor_driver
GPIO.setmode(GPIO.BOARD)

import serial
#import ultrasonic just copied functions
import random


class scooterController:

    def __init__(self):
        #pwm.stop()
        GPIO.setup(40,GPIO.OUT) # DAC1 pwm
        GPIO.setup(38,GPIO.OUT) # relay 1 hi/lo
        GPIO.setup(37,GPIO.OUT) # DAC2 pwm
        GPIO.setup(35,GPIO.OUT) # relay 2 hi/lo
        GPIO.setup(11,GPIO.OUT) #change this pin as needed
        
        self.pwm = GPIO.PWM(11,250) #set duty cycle to 50Hz or 20 ms
        self.pwm1 = GPIO.PWM(40,1000) #set duty cycle to 50Hz or 20 ms
        self.pwm2 = GPIO.PWM(37,1000) #set duty cycle to 50Hz or 20 ms
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
        # Setting serial ports for each sensors, skip AMA1 and 2
        #self.ports=[
            # serial.Serial("/dev/ttyAMA0",9600,timeout=0.1),
            # serial.Serial("/dev/ttyAMA3",9600,timeout=0.1),
            # serial.Serial("/dev/ttyAMA4",9600,timeout=0.1),
            # serial.Serial("/dev/ttyAMA5",9600,timeout=0.1)
        #]
        # Flushing ports and waiting for sensors to stabilize
        print("Resetting serial ports")
        #for ser in self.ports:
            #ser.reset_input_buffer()
        sleep(1.0)

        self.distances = []
        
    def read_dist(self,ser):
        data=ser.read(4)
        distance = (data[1] * 256 + data[2])
        return distance
        
    def distance_read(self):
        self.distances.clear()
        for ser in self.ports: # Add each distance reading
            dist = self.read_dist(ser)
            distances.append(dist)
        return distances

    def controlCommand(self,command):
        print(f"Controller Read: {command}")
        
        #self.distances = self.distance_read()
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
                self.heading = self.heading * 0.75
                cycle = motor_driver.turn_to_angle(self.heading)
                self.pwm.ChangeDutyCycle(cycle)
                sleep(0.2)
                self.heading = self.heading * 0.5
                cycle = motor_driver.turn_to_angle(self.heading)
                self.pwm.ChangeDutyCycle(cycle)
                sleep(0.2)
                self.heading = self.heading * 0.5
                cycle = motor_driver.turn_to_angle(self.heading)
                self.pwm.ChangeDutyCycle(cycle)
                sleep(0.2)
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
                self.pwm1.start(50+20) #sets pwm to 7.5% of duty cycle, or 1.5ms
                self.pwm2.start(50-20) #sets pwm to 7.5% of duty cycle, or 1.5ms
                sleep(0.25)

                GPIO.output(38, 0)
                GPIO.output(35, 0)
                sleep(0.25)

                # self.pwm1.ChangeDutyCycle(50)
                # self.pwm2.ChangeDutyCycle(50)
                # GPIO.output(38, 1)
                # GPIO.output(35, 1)
                # sleep(.5)
                
                # pwm.stop()
                # GPIO.cleanup()
            case "REVERSE":
                # call the actual gas pedal thing here
                print(f"Calling Drive Reverse. Heading: {self.heading}")
                self.pwm1.start(50-10) #sets pwm to 7.5% of duty cycle, or 1.5ms
                self.pwm2.start(50+10) #sets pwm to 7.5% of duty cycle, or 1.5ms
                sleep(.25)

                GPIO.output(38, 0)
                GPIO.output(35, 0)
                sleep(0.25)

                # self.pwm1.ChangeDutyCycle(50)
                # self.pwm2.ChangeDutyCycle(50)
                # GPIO.output(38, 1)
                # GPIO.output(35, 1)
                # sleep(.5)
                # pwm.stop()
                # GPIO.cleanup()
            case "STOP":
                # stop the drive pwms
                print(f"Stopping!!!")
                self.pwm1.ChangeDutyCycle(50)
                self.pwm2.ChangeDutyCycle(50)
                GPIO.output(38, 1)
                GPIO.output(35, 1)
                sleep(.5)
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
        












