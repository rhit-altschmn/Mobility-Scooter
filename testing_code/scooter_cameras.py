import cv2
from picamera2 import Picamera2, Preview

rev_cam= Picamera2()
rev_cam.preview_configuration.size=(1920,1080)
rev_cam.preview_configuration.__format__="RDB888"
rev_cam.start()
r=bool
r == True

if r == True:
    while True:
        vd=rev_cam.capture_array()
        cv2.imshow("Reverse",vd)
        if cv2.waitKey(1) == ord("q"):
            break
else:
    print()

rev_cam.stop()

"""
from picamera2 import Picamera2, Preview
import time
testcam = Picamera2()
camera_config = testcam.create_preview_configuration()
testcam.configure(camera_config)
testcam.start_preview(Preview.QTGL)
testcam.start()
time.sleep(30)
testcam.capture_file("test.jpg")
        """