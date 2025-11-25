import flask
import threading
import scooterController as cont
import cv2
# from picamera2 import Picamera2, Preview

app = flask.Flask(__name__,
                  static_url_path="",
                  static_folder="public")

serial_lock = threading.Lock()
cont.__init__(cont)
camera = cv2.VideoCapture(0)

@app.get("/")
def naked_domain_redirect():
    return flask.redirect("index.html")

def generate_frames(camera):
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
    return flask.Response(generate_frames(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

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

        resp_cmd,heading,dists = cont.controlCommand(cont,command)
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