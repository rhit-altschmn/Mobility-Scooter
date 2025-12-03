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
x = 10 #command input

pwm.start(50+x) #sets pwm to 7.5% of duty cycle, or 1.5ms
pwm2.start(50-x) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(1)

GPIO.output(38, 0)
GPIO.output(35, 0)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
sleep(10)

GPIO.output(38, 1)
GPIO.output(35, 1)

#pwm.stop()
=======
sleep(1)

user_in = input("Currently at 10% - Press Enter to continue...")
>>>>>>> Stashed changes

x=20
pwm.ChangeDutyCycle(50+x) #sets pwm to 7.5% of duty cycle, or 1.5ms
pwm2.ChangeDutyCycle(50-x) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(5)

user_in = input("Currently at 20% - Press Enter to continue...")

<<<<<<< Updated upstream
#GPIO.cleanup()
=======
=======
sleep(1)

user_in = input("Currently at 10% - Press Enter to continue...")

x=20
pwm.ChangeDutyCycle(50+x) #sets pwm to 7.5% of duty cycle, or 1.5ms
pwm2.ChangeDutyCycle(50-x) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(5)

user_in = input("Currently at 20% - Press Enter to continue...")

>>>>>>> Stashed changes
x=30
pwm.ChangeDutyCycle(50+x) #sets pwm to 7.5% of duty cycle, or 1.5ms
pwm2.ChangeDutyCycle(50-x) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(5)

user_in = input("Currently at 30% - Press Enter to continue...")

x=40
pwm.ChangeDutyCycle(50+x) #sets pwm to 7.5% of duty cycle, or 1.5ms
pwm2.ChangeDutyCycle(50-x) #sets pwm to 7.5% of duty cycle, or 1.5ms
sleep(5)


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
<<<<<<< Updated upstream
    #GPIO.cleanup()
>>>>>>> Stashed changes
=======
    #GPIO.cleanup()
>>>>>>> Stashed changes
