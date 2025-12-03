import RPi.GPIO as GPIO
from time import sleep
from atexit import register
@register

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT) # DAC1 pwm
GPIO.setup(38,GPIO.OUT) # relay 1 hi/lo
GPIO.setup(37,GPIO.OUT) # DAC2 pwm
GPIO.setup(35,GPIO.OUT) # relay 2 hi/lo

pwm = GPIO.PWM(40,200) #set duty cycle to 50Hz or 20 ms
pwm2 = GPIO.PWM(37,200) #set duty cycle to 50Hz or 20 ms
#operating frequency is 20Hz-22khz

state = 50
x = 10 #command input
for x in range(state,state+x+1,1):
    pwm.start(x) #sets pwm to 7.5% of duty cycle, or 1.5ms
    pwm2.start(x) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(1)
GPIO.output(38, 0)
GPIO.output(35, 0)
sleep(1)
GPIO.output(38, 1)
GPIO.output(35, 1)
#pwm.stop()
sleep(1)

user_in = input("Currently at 10% - Press Enter to continue...")

inc=10
for val in range(state, state+inc+1, 1):
    pwm.ChangeDutyCycle(val) #sets pwm to 7.5% of duty cycle, or 1.5ms
    pwm2.ChangeDutyCycle(val) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(1)
state = val
user_in = input(f"Currently at {state-50}% - Press Enter to continue...")


inc = 10
for val in range(state, state+inc+1, 1):
    pwm.ChangeDutyCycle(val) #sets pwm to 7.5% of duty cycle, or 1.5ms
    pwm2.ChangeDutyCycle(val) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(1)
user_in = input(f"Currently at {state-50}% - Press Enter to continue...")

inc = 10
for val in range(state, state+inc+1, 1):
    pwm.ChangeDutyCycle(val) #sets pwm to 7.5% of duty cycle, or 1.5ms
    pwm2.ChangeDutyCycle(val) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(1)
user_in = input(f"Currently at {state-50}% - Press Enter to continue...")

for val in range(state, 50, -1):
    pwm.ChangeDutyCycle(val) #sets pwm to 7.5% of duty cycle, or 1.5ms
    pwm2.ChangeDutyCycle(val) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(1)
user_in = input(f"Currently at {state-50}% - Press Enter to continue... (and abort)")





pwm.ChangeDutyCycle(50)
pwm2.ChangeDutyCycle(50) # theorizing that drive controller does not like instantaneous return to center
sleep(1)
GPIO.output(38, 1)
GPIO.output(35, 1)

#pwm.stop()
#GPIO.cleanup()

def terminate():
    pwm.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50) # theorizing that drive controller does not like instantaneous return to center
    sleep(1)
    GPIO.output(38, 1)
    GPIO.output(35, 1)
    #pwm.stop()
    #pwm2.stop()