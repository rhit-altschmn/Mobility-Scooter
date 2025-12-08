import flask
import threading
import scooterController 
from time import sleep
import cv2
from picamera2 import Picamera2, Preview

app = flask.Flask(__name__,
                  static_url_path="",
                  static_folder="public")

serial_lock = threading.Lock()
# --- Setup Pi Camera ---
pi_cam = Picamera2()
camera_config = pi_cam.create_preview_configuration()
pi_cam.configure(camera_config)
pi_cam.start()
sleep(1)  

live_camera = "pi" #default ---can be changed
# --- Setup USB cameras ---
#check the ports to be sure on the pi
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
            sleep(0.1)
            continue

        # JPEG things
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        #Yield Magic
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')



@app.route('/set_camera/<cam_name>', methods=['POST'])
def set_camera(cam_name):
    global live_camera
    if cam_name in ["pi","usb0","usb2"]:
        live_camera = cam_name
        print(f"Active camera set to: {live_camera}")
        return "OK", 200
    else:
        return "Invalid camera", 400
   
@app.route('/')
def index():
    return flask.render_template('index.html')

def generate_frames(camera): # turn debug mode off or camera no work!
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield frame in MJPEG format
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
@app.route('/video_feed')           
def video_feed():
    return flask.Response(generate_frames(cam1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/api/<command>")
def command_api(command):
    
    with serial_lock:
        
        resp_cmd,heading,dists = cont.controlCommand(command)
        print(f"Site Incoming command: {resp_cmd} Heading:{heading} Distances:{dists}")
        response = resp_cmd + "?" + str(heading) +"?" + str(dists)
        print(response)
        return response
    
  

app.run(host="0.0.0.0", port=5000, debug=False)


'''
def __init__(self):
    self.server = flask.Flask(__name__,
                static_url_path="",
                static_folder="public")
    self.HTML_PAGE = """
                    <html>
                    <head>
                        <title>Raspberry Pi Webcam Stream</title>
                    </head>
                    <body>
                        <h1>Live Stream</h1>
                        <img src="{{ url_for('video_feed') }}" width="640" height="480">
                    </body>
                    </html>
                    """
    self.camera = cv2.VideoCapture(0)
    # Register routes after initializing Flask app
    self.server.add_url_rule('/', 'index', self.index)
    self.server.add_url_rule('/video_feed', 'video_feed', self.video_feed)

def generate_frames(self):
    while True:
        success, frame = self.camera.read()
        if not success:
            break
        else:
            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield frame in MJPEG format
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
def index(self):
    return flask.render_template_string(self.HTML_PAGE)

def video_feed(self):
    return flask.Response(self.generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
def run(self):
    self.server.run(host='0.0.0.0', port=5000)
'''
