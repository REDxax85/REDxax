from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video part'}), 400

    video = request.files['video']
    if video.filename == '':
        return jsonify({'error': 'No selected video'}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(filepath)
    return jsonify({'message': 'Video uploaded successfully', 'path': filepath}), 200

@app.route('/')
def index():
    return 'Servidor de subida de videos funcionando!'

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
