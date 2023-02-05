from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
# import torch
import numpy as np
# import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    model_file = request.files['model_file']
    model_filename = secure_filename(model_file.filename)
    model_file.save(model_filename)
    # model = torch.jit.load(model_filename)
    
    image_file = request.files['image_file']
    image_filename = secure_filename(image_file.filename)
    image_file.save(image_filename)
    # image = cv2.imread(image_filename)
    
    # prediction = model(torch.from_numpy(image).unsqueeze(0))
    return render_template('result.html', image_filename=image_filename, prediction='-99999999')

if __name__ == '__main__':
    app.run(debug=True)