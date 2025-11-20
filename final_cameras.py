import cv2
import numpy as np
from picamera2 import Picamera2, Preview
import time
print(cv2.__version__)
testcam = Picamera2() #Pi-camera
camera_config = testcam.create_preview_configuration()
testcam.configure(camera_config)
testcam.start_preview(Preview.QTGL)

stream = cv2.VideoCapture(0) # 
stream2 = cv2.VideoCapture(2) # 
#reszing frame for side view
side_height = 200
side_width = 200
side_dimensions = (side_width,side_height)
#Defining need parameters
no_movement = 0
move_forward = 1
move_reverse = 2
state = 3
state = int(input("What state:"))
#if r = 0, if r =-1 , if r = 1 
while True:
    if state == no_movement:
        print("There is nothing to show")
    elif state == move_reverse:
        retB, frameB= stream2.read()  #-----reverse
        if not retB:
            print("Failed to read cameras")
            break
        reverse_cam = np.hstack((frameB))
        cv2.imshow("REVERSE CAM", reverse_cam)
        if cv2.waitKey(1)==ord('q'):
            break
    if state == move_forward:
        retA, frameA= stream.read() #----forward(side)
        frame_pi = testcam.capture_array()  #---forward(ford)
        if not retA  or  frame_pi:
            print("Failed to read cameras")
            break
        side_frame = cv2.resize(frameA, side_dimensions)
        side_forward = np.hstack((side_frame,frame_pi))
        cv2.imshow("SIDE & FORWARD VIEW", side_forward)
        if cv2.waitKey(1)==ord('q'):
            break
testcam.start()
time.sleep(30)
stream.release()
stream2.release()
cv2.destroyAllWindows()

#t= 123
#print(t)

#testcam = Picamera2()



#testcam.capture_file("test.jpg")
