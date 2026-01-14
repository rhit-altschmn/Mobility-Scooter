# Mobility-Scooter
This is a repo to handle code for automating a mobility scooter. A joint partnership between Intro to Robotics team and Dr. Bill Smart's lab.
(https://www.markdownguide.org/basic-syntax/#links)

## Hardware
* Raspberry Pi4 - the brain that runs code and hosts the flask server
* Stepper Motor - used with belt system on drive shaft for steering front wheel
* Voltage-stepdowns - used with PWM for controlling rear wheels powerin the scooter forward/backward
* Cameras (2 USB and 1 picam) - for viewing so users can teleop the scooter. maybe used for computer vision in future
* ultrasonics (4) - for object avoidance sensing

## Software
* scooterSite.py - runs the flask site html and handles camera frame creation and streaming to site
* templates/index.html - the html for the flask site
* public/main.js - the javascript to handle button pushes on the html
* scotterController.py - does all the backend scooter control:
  - initializes all the GPIO pins and serial ports
  - calls the appropriate functions for moving & turning scooter
  - handles ultrasonics gets readings and publishes them.
* motor_driver.py - calculates the correct pwm setting for desired turn angle

  all the other files are old testing files not needed in final scooter operation.
