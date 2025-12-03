import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT) # DAC1 pwm
GPIO.setup(38,GPIO.OUT) # relay 1 hi/lo
GPIO.setup(37,GPIO.OUT) # DAC2 pwm
GPIO.setup(35,GPIO.OUT) # relay 2 hi/lo

pwm = GPIO.PWM(40,1000) #set duty cycle to 50Hz or 20 ms
pwm2 = GPIO.PWM(37,1000) #set duty cycle to 50Hz or 20 ms
#operating frequency is 20Hz-22khz
x = -1 #command input #1 for forward, -1 for backward
for i in range(1,20,1):
	pwm.start(50+20*x) #sets pwm to 7.5% of duty cycle, or 1.5ms
	pwm2.start(50-20*x) #sets pwm to 7.5% of duty cycle, or 1.5ms
	sleep(.25)

	GPIO.output(38, 0)
	GPIO.output(35, 0)
	sleep(1)

	pwm.ChangeDutyCycle(50)
	pwm2.ChangeDutyCycle(50)
	GPIO.output(38, 1)
	GPIO.output(35, 1)
	sleep(.5)

#pwm.stop()

#set motor to left
#pwm.ChangeDutyCycle(2.5) #sets pwm to 2.5% of duty cycle, or .5ms
#sleep(5)

#set motor to right
#pwm.ChangeDutyCycle(12.5) #sets pwm to 12.5% of duty cycle, or 2.5ms
#sleep(5)

#GPIO.cleanup()
