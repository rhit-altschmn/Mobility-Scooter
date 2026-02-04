import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT) #change this pin as needed
pwm = GPIO.PWM(11,1000) #set duty cycle to 50Hz or 20 ms
#operating frequency is 50-330Hz

#motor operates from 500-2500 microseconds or 0.5-2.5ms
#motor nuetral is at 1500 microseconds or 1.5ms

#set motor to neutral
pwm.start(100) #sets pwm to 7.5% of duty cycle, or 1.5ms
print("started pwm")
sleep(500)

pwm.stop()
GPIO.cleanup()