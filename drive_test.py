import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT) #change this pin as needed
GPIO.setup(38,GPIO.OUT) #change this pin as needed

GPIO.output(38, GPIO.HIGH)
sleep(1)

pwm = GPIO.PWM(40,50) #set duty cycle to 50Hz or 20 ms
#operating frequency is 50-330Hz

#motor operates from 500-2500 microseconds or 0.5-2.5ms
#motor nuetral is at 1500 microseconds or 1.5ms

#set motor to neutral
pwm.start(50) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(5)

GPIO.output(38, GPIO.LOW)

pwm.stop()

#set motor to left
#pwm.ChangeDutyCycle(2.5) #sets pwm to 2.5% of duty cycle, or .5ms
#sleep(5)

#set motor to right
#pwm.ChangeDutyCycle(12.5) #sets pwm to 12.5% of duty cycle, or 2.5ms
#sleep(5)

GPIO.cleanup()
