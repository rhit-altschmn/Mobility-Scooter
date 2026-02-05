#t= 123
#print(t)
from picamera2 import Picamera2, Preview
import time
testcam = Picamera2()
camera_config = testcam.create_preview_configuration()
testcam.configure(camera_config)
testcam.start_preview(Preview.QTGL)
testcam.start()
time.sleep(30)
testcam.capture_file("test.jpg")
