import flask
import threading
#from plateloader import PlateLoader

app = flask.Flask(__name__,
                  static_url_path="",
                  static_folder="public")

serial_lock = threading.Lock()

@app.get("/")
def naked_domain_redirect():
    return flask.redirect("index.html")

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

        resp = command
        print(f"Incoming command: {resp}")
        return resp
    

   

app.run(host="0.0.0.0", port=5000, debug=True)