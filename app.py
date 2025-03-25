from flask import Flask, render_template, Response, request
from model import detect
import cv2
import numpy as np
import base64

app = Flask(__name__)

# camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
        data = request.get_json()
        if data and 'image' in data:
            # Convert base64 image to numpy array
            image_data = data['image'].split(',')[1].encode()
            np_arr = np.frombuffer(base64.b64decode(image_data), np.uint8)
            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            
            frame = detect(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    frame=generate_frames()
    return Response(frame, mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
