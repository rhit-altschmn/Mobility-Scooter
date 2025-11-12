#import RPi.GPIO as GPIO
from time import sleep

import motor_driver
#GPIO.setmode(GPIO.BOARD)

def __init__(self):
    #GPIO.setup(11,GPIO.OUT) #change this pin as needed
    #self.pwm = GPIO.PWM(11,50) #set duty cycle to 50Hz or 20 ms
    #operating frequency is 50-330Hz

    #motor operates from 500-2500 microseconds or 0.5-2.5ms
    #motor nuetral is at 1500 microseconds or 1.5ms

    #set motor to neutral
    #self.pwm.start(7.5) #sets pwm to 7.5% of duty cycle, or 1.5ms
    self.heading = 0
    sleep(5)


def controlCommand(self, command):
    match command:
        case "LEFT":
            self.heading = self.heading -10
            if self.heading < -67.5:
                self.heading = -60

















