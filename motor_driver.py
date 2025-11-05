def turn_to_angle(angle, pwm):
    """This assumes that the motor is in pin 11 and 50 Hz. Takes values between -67.5 and 67.5 for angles"""
    #Mechanical parameters
    gear_ratio = 2
    Hz = 50
    cycle_length = ((1/Hz) * 1000) #in ms

    #Motor parameters
    operating_range = 2000 #microseconds
    min_width = 500 #microseconds
    operating_angle = 270

    turn_angle = (angle * gear_ratio) + operating_angle/2 #returns a value beetween 0 and 270

    width = ((operating_range/operating_angle * turn_angle) + min_width) / 1000 #calculates the pulse width in ms assuming linear relationship

    duty_cycle = width / cycle_length #finds what percent of the duty_cycle corresponds to that pulse width

    pwm.ChangeDutyCycle(duty_cycle)