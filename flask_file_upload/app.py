from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
   return "Hello!"
 

@app.route('/fileUpload', methods = ['POST'])
def upload_file():
    f = request.files['file']
    f.save(f'uploads/{secure_filename(f.filename)}')
    return 'uploads 디렉토리 -> 파일 업로드 성공!'
 
if __name__ == '__main__':
   app.run(debug = True)