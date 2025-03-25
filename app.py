from flask import Flask, render_template, Response, request, jsonify
from model import detect
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed', methods=['POST'])
def video_feed():
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data received'}), 400

        # Convert base64 image to numpy array
        image_data = data['image'].split(',')[1].encode()
        np_arr = np.frombuffer(base64.b64decode(image_data), np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        # Process frame
        processed_frame = detect(frame)
        
        # Convert processed frame back to image
        _, buffer = cv2.imencode('.jpg', processed_frame)
        response_image = base64.b64encode(buffer).decode('utf-8')
        
        return jsonify({'image': f'data:image/jpeg;base64,{response_image}'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
