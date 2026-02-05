from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import cv2
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Video Streaming
def generate_frames():
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame_data = base64.b64encode(buffer).decode('utf-8')
        socketio.emit('frame', {'image': frame_data})
    cap.release()

@socketio.on('connect')
def connect():
    socketio.start_background_task(generate_frames)

# Button Push Handling
@socketio.on('button_push')
def handle_button_push(data):
    button_id = data.get('id')
    emit('button_pressed', {'id': button_id}, broadcast=True)

# UI Route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
