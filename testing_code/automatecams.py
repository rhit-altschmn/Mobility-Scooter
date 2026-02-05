import cv2
from flask import Flask, render_template, Response
import time
import threading
import scooterController 
import cv2
from picamera2 import Picamera2, Preview

app = Flask(__name__)

serial_lock = threading.Lock()


# --- Setup Pi Camera ---
pi_cam = Picamera2()
camera_config = pi_cam.create_preview_configuration()
pi_cam.configure(camera_config)
pi_cam.start()
time.sleep(1)  

live_camera = "pi" #default ---can be changed
# --- Setup USB cameras ---
usb_cam0 = cv2.VideoCapture(0)   # side / forward /reverse
usb_cam2 = cv2.VideoCapture(2)   # side / forward /reverse
#---Scooter control -----
cont = scooterController.scooterController()

# --- verify that all cameras are properly streaming --- 
if not usb_cam0.isOpened():
   print("Error: Could not open USB camera 0")
if not usb_cam2.isOpened():
    print("Error: Could not open USB camera 2")

def get_all_frames():
    global live_camera

    while True:
        frame = None
        ret = False

        if live_camera == "pi":
            # got to finalize what view this shows
            frame = pi_cam.capture_array()
            frame = cv2.resize(frame, (640, 480))
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            ret = True  

        elif live_camera == "usb0":
            # got to finalize what view this shows
            ret, frame = usb_cam0.read()
            if not ret:
                print("Failed to read from USB camera 0")
                continue
            frame = cv2.resize(frame, (640, 480))

        elif live_camera == "usb2":
            # got to finalize what view this shows
            ret, frame = usb_cam2.read()
            if not ret:
                print("Failed to read from USB camera 2")
                continue
            frame = cv2.resize(frame, (640, 480))

        else:
            print("INVALID CAMERA:", live_camera)
            time.sleep(0.1)
            continue

        # JPEG things
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        #Yield Magic
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        
        time.sleep(0.75) #controls frames per second



@app.route('/set_camera/<cam_name>', methods=['POST'])
def set_camera(cam_name):
    global live_camera
    if cam_name in ["pi","usb0","usb2"]:
        live_camera = cam_name
        print(f"Active camera set to: {live_camera}")
        return "OK", 200
    else:
        return "Invalid camera", 400
        
@app.route('/video_feed')
def video_feed():
    return Response(get_all_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')    
@app.route('/')
def index():
    
    return render_template('index.html')
    
@app.route("/api/<command>")
def command_api(command):
    with serial_lock:
        # pl = PlateLoader()
        # #/dev/ttyUSB0 for USB plateloader  
        # # /dev/ttyACM0 for COM port
        # #Be sure to change it in all 3 places!
        # pl.connect ("/dev/ttyUSB0")  
        # resp = pl.send_command(command)
        # pl.disconnect()

        
        resp_cmd,heading,dists = cont.controlCommand(command)
        print(f"Site Incoming command: {resp_cmd} Heading:{heading} Distances:{dists}")
        response = resp_cmd + "?" + str(heading) +"?" + str(dists)
        print(response)
        return response

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
    finally:
        #usb_cam0.release()
        usb_cam2.release()
        pi_cam.stop()
        cv2.destroyAllWindows()
