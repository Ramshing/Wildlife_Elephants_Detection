from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO


app = Flask(__name__)

# Capture video from webcam (use 0) or a drone stream URL
cap = cv2.VideoCapture(0)  # Replace 0 with stream URL for drone, e.g., 'rtsp://...'

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Optional: Add detection overlays here

            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')  # Web interface

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
