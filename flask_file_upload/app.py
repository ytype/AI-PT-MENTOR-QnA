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
   try :
      f = request.files['file']
      fileName = f.filename + '.wav'
      f.save(f'uploads/{secure_filename(fileName)}')
      return '200'
   
   except :
      return '500'
   
   
 
if __name__ == '__main__':
   app.run(debug = True)