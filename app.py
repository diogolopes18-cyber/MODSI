#!/usr/bin/env python3

import os
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, session, abort
import database_conn as db
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from user.orientador_page import orientador
from user.student_page import aluno
from user.diretor import diretor
from user.public_projects import public


#####################
##  ENV VARIABLES  ##
#####################
diretor_username = os.environ.get('DIRETOR_USERNAME')
diretor_password = os.environ.get('DIRETOR_PASSWORD')


####################
##  APP CONTEXTS  ##
####################

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_PATH'] = 'uploads'
app.config['UPLOAD_EXTENSIONS'] = ['.pdf', '.txt', '.png', '.docx', '.ppt', '.xlsx']
# limit upload size upto 20MB
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

##################
##  BLUEPRINTS  ##
##################

app.register_blueprint(orientador)
app.register_blueprint(aluno)
app.register_blueprint(diretor)
app.register_blueprint(public)
error = None


@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global error
    return render_template("home.html", error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global error
    if(request.method == 'POST'):
        # Check for empty inputs
        if(request.form['username'] == "" or request.form['password'] == ""):
            error = 'No credentials provided. Please try again.'
        else:
            # Student login
            if(request.form['username'].isnumeric()):
                authorization = db.connection_db(
                    data=[
                        request.form['username'],
                        request.form['password']
                    ],
                    query="search",
                    tablename="student")

                if(authorization == 1):
                    return redirect(url_for('aluno.personal_page'))
                elif(authorization == 0):
                    error = 'Invalid Credentials. Please try again.'
                    return render_template("login.html", error=error)

            # Conselour login
            if(request.form['username'].isnumeric() == False):
                if(request.form['username'] != diretor_username):
                    authorization = db.connection_db(
                        data=[
                            request.form['username'],
                            request.form['password']
                        ],
                        query="search", tablename="orientador")

                    if(authorization == 1):
                        return redirect(url_for('orientador.orientador_page'))
                    elif(authorization == 0):
                        error = 'Invalid Credentials. Please try again.'
                        return render_template("login.html", error=error)

                # Administrator login
                elif(request.form['username'] == diretor_username and request.form['password'] == diretor_password):
                    return redirect(url_for('diretor.diretor_page'))
                else:
                    return redirect(url_for('app.login'))

    return render_template("login.html", error=error)


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
                db.connection_db(data=params_to_insert, query="insert", tablename="orientador")
                return redirect(url_for('login'))

            # Student
            elif(request.form['username'].isnumeric()):
                params_to_insert = [
                    request.form['username'], request.form['password'], request.form['email']
                ]
                db.connection_db(data=params_to_insert, query="insert", tablename="student")
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
            db.connection_db(data=update, query="update")
            return redirect(url_for('login'))

    return render_template("forgot_password.html", error=error)


@app.route('/file_upload', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):

        # Retrieve data from form
        data = [
            {
                'title': request.form['title'],
                'status': 'submitted',
                'student': request.form['student'],
                'orientador': request.form['orientador']
            }
        ]

        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)

        if(filename != ""):
            file_ext = os.path.splitext(filename)[1]
            if(file_ext not in app.config['UPLOAD_EXTENSIONS']):
                return "Invalid image", 400

            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            db.connection_db(data=data, query="insert", tablename="projetos")

            return redirect(url_for('aluno.personal_page'))

    return render_template("upload.html")

######################################################
# Redirect to this function while accessing files
######################################################


@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=65200)
