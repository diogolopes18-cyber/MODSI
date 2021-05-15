#!/usr/bin/env python3

import os
import json
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
import database_conn as db
from uuid import uuid4
from werkzeug.utils import secure_filename
#from student import student

app = Flask(__name__)

######################
##  App blueprints  ##
######################
# app.register_blueprint(student)

error = None
authorize = 0

random_list = [1170654, 'Carolina']


@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    global error
    if(request.method == 'POST'):

        # Check for empty inputs
        if(request.form['username'] == "" or request.form['password'] == ""):
            error = 'Invalid Credentials. Please try again.'
        else:
            db.connection_db(random_list, query="search")
            return redirect(url_for('student.submit_paper'))

    return render_template("login.html", error=error)


@app.route('/register', methods=['GET', 'POST'])
def sign_in():
    global error
    if(request.method == 'POST'):
        if(request.form['username'] == "" or request.form['password'] == "" or request.form['email'] == ""):
            error = 'Please provide some sign up information'
        else:
            params_to_insert = [
                request.form['username'], request.form['password'], request.form['email']
            ]
            db.connection_db(params_to_insert, query="insert")
            return redirect(url_for('login'))

    return render_template("registo.html", error=error)


@app.route('/get_back', methods=['GET', 'POST'])
def forgot_password():
    global error
    # Resets password
    if(request.method == 'POST'):
        if(request.form['new_username'] == "" or request.form['new_password']):
            error = 'Provide new data'
        else:
            update = [
                request.form['new_username'], request.form['new_password']
            ]
            print(update)
            # Updates password on database
            db.connection_db(update, query="update")
            return redirect(url_for('login'))

    return render_template("forgot_password.html", error=error)


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'png'}
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 8mb
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/test', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            print('No file selected')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')


@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
