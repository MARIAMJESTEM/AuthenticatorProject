from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '27ba51b46332c22d3005b6534d881908'


@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/login",methods=['GET'])
def login():
    return render_template('signin.html')

@app.route('/getID', methods =["POST"])
def getID():
        userID = request.form.get("ID") 
        # TODO: Check if userID is in data base with users and assin it to inBase
        inBase = True
        if inBase:
            return redirect(url_for('takePicture'))
        else:
            flash('ID <{a}> not found in the database!'.format(a= userID))
            return redirect(url_for('login'))

@app.route('/takePicture', methods=['GET', 'POST'])
def takePicture():
     return render_template('takePicture.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' in request.files:
        file = request.files['photo']
        photo_path = 'static/images/photoTaken/photo.jpg'
        if os.path.exists(photo_path):
            os.remove(photo_path)
        file.save(photo_path)
        return redirect(url_for('access'))
    return 'No photo provided.', 400

@app.route('/access', methods=['GET', 'POST'])
def access():
     # TODO: Check if user has access after taking photo and assign the boolean output to  access
     #photo is saved at this path "static/images/photoTaken/photo.jpg"
     access = False
     return render_template('access.html', access=access)

if __name__ == '__main__':
    app.run(debug=True)
