# Ultrasonic Distance Sensors

## Overview
Four [A02YYUW waterproof ultrasonic distances](https://www.dfrobot.com/product-1935.html?gad_source=1&gad_campaignid=23441887437&gbraid=0AAAAADucPlCRXa7D_Kvba-kukyFipLa4a&gclid=CjwKCAiA1obMBhAbEiwAsUBbIlLDa9yQKhEFwBFZINNrHECve9TGsDGMjDDfvNWs-kgvXg-K0WDj-hoCmBUQAvD_BwE) were put on the scooter. One was placed to view each direction, with the left and right sensors being mounted low and pointed slightly upwards in an effort to see cars nearby in a parking lot scenario. The rear sensor uses a [3D printed mount](https://cad.onshape.com/documents/c4d6c58f98211453321110ab/w/8268dd0c223b57df2334ac4d/e/cfee72e95296e9f6bdb92858) inserted into the hitch. These distance readings are used for safe navigation, ensuring that a user or autonmous controller do not hit any obstacles.

## Setup
The A02YYUW operates at either 3.3 or 5V, and will output the same voltage. If using with a Raspberry Pi it is important to power with 3.3V to avoid damaging any pins. Please see the [datasheet](https://media.digikey.com/pdf/Data%20Sheets/DFRobot%20PDFs/SEN0311_Web.pdf) for relevant information.

Note that the blue wire is TX and Green is RX for UART.

Setup procedure on a new Pi is as follows:
1. Enable UART in config by using `sudo nano /boot/config.txt` and adding the following to the bottom:
   `dtoverlay=disable-bt
   enable_uart=1
   dtoverlay=uart3
   dtoverlay=uart4
   dtoverlay=uart5`
2. Disable bluetooth with the following:
   `sudo systemctl disable hciuart.service
   sudo systemctl mask hciuart.service
   sudo reboot`
3. Install pyserial with:
   `pip install pyserial`

## Code
Please see ultrasonic.py for example code on using the sensors. If the serial ports are not working you can verify the ports with `ls /dev/ttyAMA`. The CPU speed function is useful for checking the load cuased by the sensors, with speeds below 1100 being ideal for continouse use without cooling.

