from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from bgfun import *

PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def save():
    path2 = 'static/people_photo/temp.jpg'
    if request.method == 'POST':
        f = request.files['file']
        # f.save(secure_filename(f.filename))
        print("done")
        f.save(path2)
        print('save')
        pre()
    return render_template('profile.html', user_image=os.path.join(app.config['UPLOAD_FOLDER'], 'new1.jpg'), before=os.path.join(app.config['UPLOAD_FOLDER'], 'temp.jpg'))


if __name__ == "__main__":
    app.run(debug=True)
