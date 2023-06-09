from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os


from ml_model import givePredict

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = "static/uploads"
app.secret_key = "secretket1234fornm5678"

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

RESULT = []

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods = ("POST","GET"))
def get_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            print("No file part")
            return redirect(request.url)


        # print(request.files('file'))
        file = request.files['file']

        if file.filename == '':
            print("File name is invalid")
            return redirect(request.url)
        # return render_template("confirm.html")
        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

        # basedir = os.path.abspath(os.path.dirname(__file__))
            file.save(os.path.join(app.config['IMAGE_UPLOADS'],filename))
            print('Image successfully uploaded')
            
            # result = 'SAI MUKESH'
            
            result = givePredict(filename)

            RESULT.append(filename)
            RESULT.append(result)
            
            
            return render_template('confirm.html', filename = RESULT)

        else:
            print("Not in allowed types")
            return redirect(request.url)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    # getdir()
    app.run(debug=True)