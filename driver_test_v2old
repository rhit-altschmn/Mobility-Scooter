import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT) # DAC1 pwm
GPIO.setup(38,GPIO.OUT) # relay 1 hi/lo
GPIO.setup(37,GPIO.OUT) # DAC2 pwm
GPIO.setup(35,GPIO.OUT) # relay 2 hi/lo

pwm = GPIO.PWM(40,50) #set duty cycle to 50Hz or 20 ms
pwm2 = GPIO.PWM(37,50) #set duty cycle to 50Hz or 20 ms
#operating frequency is 20Hz-22khz
x = 10 #command input

pwm.start(50+x) #sets pwm to 7.5% of duty cycle, or 1.5ms
pwm2.start(50-x) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(1)

GPIO.output(38, 1)
GPIO.output(35, 1)
sleep(10)

pwm.ChangeDutyCycle(50)
pwm2.ChangeDutyCycle(50)
GPIO.output(38, 0)
GPIO.output(35, 0)

#pwm.stop()

#set motor to left
#pwm.ChangeDutyCycle(2.5) #sets pwm to 2.5% of duty cycle, or .5ms
#sleep(5)

#set motor to right
#pwm.ChangeDutyCycle(12.5) #sets pwm to 12.5% of duty cycle, or 2.5ms
#sleep(5)

#GPIO.cleanup()