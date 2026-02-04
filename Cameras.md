# Camera System Documentation

## Overview

During teleoperation of the mobility scooter, there is a high likelihood that the scooter may move out of the operator’s direct line of sight. To address this challenge, the team developed a three view camera system to provide continuous visual feedback of the scooter’s surroundings.

This system enables real time monitoring by providing views from the front, rear, and left side of the scooter. The left side view is particularly useful during docking operations. Together, these views improve situational awareness and enhance safe remote operation.

---

## Camera System

The camera system consists of one PiCamera and two USB cameras.

The PiCamera is mounted at the front of the scooter to provide the forward facing view.  
One USB camera is mounted at the rear to provide the back view.  
Another USB camera is mounted on the left side to assist during docking.

The PiCamera is connected directly to the Raspberry Pi 4B through the dedicated camera interface port. The two USB cameras are connected through USB extension cables to the available USB ports on the Raspberry Pi.

For demonstration purposes, non waterproof cameras were selected to reduce cost. However, these cameras can be enclosed in waterproof housings for outdoor or adverse weather use.

## Specifications
-  PiCamera            - https://www.raspberrypi.com/documentation/accessories/camera.html#camera-module-2
-  USB Camera(FIT0892) - https://www.digikey.com/en/products/detail/dfrobot/FIT0892/18069226
   

---

## Integration into the General System

The camera system is integrated into the local domain host using a Flask based web interface.

A single display window is designed to showcase the selected camera view. Three control buttons are provided to allow the operator to switch between camera feeds in real time:

- FRONT CAM for the front view  
- BACK CAM for the rear view  
- SIDE CAM for the left side view  

These controls enable flexible and efficient monitoring during teleoperation.

For reference, the implementation code can be found in:

- 
- 
-  
- 

---

## Current State of the Camera System

Currently, the camera system is not fully operational due to power limitations of the Raspberry Pi when supporting all cameras and other system components simultaneously.

- The rear and side cameras are physically disconnected and unmounted from their designated positions  
- The PiCamera remains mounted but is currently disconnected  
- All other system components remain as described in the previous sections  

These limitations are temporary and will be addressed through future power management and hardware upgrades.
