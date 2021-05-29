#!/usr/bin/env python3

import os
import json
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, session, abort
import database_conn as db
from werkzeug.utils import secure_filename
import webbrowser as web
from threading import Timer
from diretor.diretor_page import diretor

###############################
## FILE UPLOAD AND DOWNLOAD  ##
###############################

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'png'}
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

####################
##  APP CONTEXTS  ##
####################

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 20MB
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

##################
##  BLUEPRINTS  ##
##################

app.register_blueprint(diretor)


error = None


def open_browser():
    web.open_new('http://127.0.0.1:65200')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    global error
    if(request.method == 'POST'):
        # Check for empty inputs
        if(request.form['username'] == "" or request.form['password'] == ""):
            error = 'No credentials provided. Please try again.'
        else:
            authorization = db.connection_db(request.form['username'], query="search")

            if(authorization == 1):
                return redirect(url_for('student'))
            elif(authorization == 0):
                error = 'Invalid Credentials. Please try again.'
                return render_template("login.html", error=error)

        if(type(request.form['username'] == str)):
            authorization = db.connection_db(request.form['username'], query="search", tablename="diretor")

            if(authorization == 1):
                return redirect(url_for('diretor.professor_page'))
            elif(authorization == 0):
                error = 'Invalid Credentials. Please try again.'
                return render_template("login.html", error=error)

    return render_template("login.html", error=error)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global error
    return render_template("home.html", error=error)


@app.route('/register', methods=['GET', 'POST'])
def sign_in():
    global error
    if(request.method == 'POST'):
        if(request.form['username'] == "" or request.form['password'] == "" or request.form['email'] == ""):
            error = 'Please provide some sign up information'
        else:
            # Professor
            if(request.form['username'].isnumeric() == False):
                params_to_insert = [
                    request.form['username'], request.form['password'], request.form['email']
                ]
                db.connection_db(params_to_insert, query="insert", tablename="diretor")
                return redirect(url_for('login'))

            # Student
            elif(request.form['username'].isnumeric()):
                params_to_insert = [
                    request.form['username'], request.form['password'], request.form['email']
                ]
                db.connection_db(params_to_insert, query="insert", tablename="student")
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


@app.route('/file_upload', methods=['GET', 'POST'])
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
            # process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')


@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):

    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)


@app.route('/aluno', methods=['GET', 'POST'])
def student():
    return render_template("aluno.html")


if __name__ == "__main__":
    # Starts thread
    # Timer(1, open_browser).start()
    app.run(debug=True, host='0.0.0.0', port=65200)
