## Steering System

### Overview
In order to drive automously we need to remotely steer the mobility system. The base mobility sccooter has no powered steering and is manually steered through turning the handle bars which turn a steering column. Therefore, the steering system needs to mount on the frame of the mobility scooter and allow powered steering.

### Goals
* Allow the pi to autonomously control the angle of the steering column when powered on
  * This assumes that there is no rider or additional weight on the scooter while being autonomously operated. 
* Allow the scooter rider to manually steer the scooter while riding it
  * This will require either  a clutch or backdriving the motor. For the sake of simplicity, we chose to backdrive the motor.
* Attach to the frame of the scooter with minimal damage or modifications
* Allow precise control of the angle of the front wheel.
  * For the sake of simplicity, this version is open loop control. 

### Design
The steering angle is controlled by driving a servo mounted the the frame and belted to the steering column. The 2:1 gear ratio combined with the manual leverage from the handle bars make it reasonable to backdrive the unpowered servo without much difficulty. The motor requires a stepdown in voltage from the system power and is connected to the voltage stepdown in the central control box. This resulted in the motor being slightly undervolted at 5V instead of 6V. During tests, the motor was slower, but no less accurate. The belt sprockets used are 3D printed based on McMaster-Carr sprockets. The largest sprocket is left unchanged. The smaller sprocket has a large hole bored through the middle to accomodate the steering column and a small hole perpendicular to that to accomodate the bolt on the steering column. To reduce skipping, it is important that the mount is as rigid as possible. There is a shim used in the clamp to help tension the belt appropriately. To control the servo, you can use the "motor_driver.py" file. This file contains a function that takes the desired angle and Hz as an input. Then, it can either return the needed duty cycle for the pwm, or it can directly set the pwm. The gear ratio can also be modified in the function. 

<img width="253" height="222" alt="front" src="https://github.com/user-attachments/assets/0a616aa1-5b9d-4dc7-bbcc-026460ca786e" />

### Parts
* Annimos servo motor: https://www.amazon.com/dp/B0C69WWLWQ
* DROK DC Buck Converter: https://www.amazon.com/DROK-Converter-5-3V-32V-Regulator-Transformer/dp/B078Q1624B
* 1.75in OD Pulley: https://www.mcmaster.com/1277N23
* 3.28in OD Pulley: https://www.mcmaster.com/57105K32
* 13in Timing belt: https://www.mcmaster.com/1679K121
* 3D printed parts as shown in the CAD

### Installation
1. Print out both belt sprockets, both halves of the clamp, and the shim from the CAD.
2. Remove the two bolts on the steering column and split it into two pieces. Slide the smaller belt sproket and the belt on the steering column. Reattach the steering column.
3. Screw the round aluminum servo horn on to the large belt sprocket. Install sprocket on the servo.
4. Bolt the servo bracket to the clamp with a shim in between. The width of the shim can be adjusted to adjsut the tension in the belt. You may need to drill out the 3D printed holes. Screw the bracket into the servo motor. 
5. Align the clamp around the frame of the scooter. You may need to add a strip of double sided tape or foam to adjsut fit. Secure the belt around both sprockets. Bolt the two halves of the clamp together, starting with the bolt on the bottom.
6. Regularly inspect the mount for cracks or fatigue.
   
### Documentation
https://cad.onshape.com/documents?nodeId=2ab928cb0acfaec854c34554&resourceType=folder
