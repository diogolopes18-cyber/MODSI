#!/usr/bin/env python3

import os
import json
import psycopg2
from flask import Flask, render_template, flash, request, redirect, url_for
import database_conn as db

app = Flask(__name__)
error = None
authorize = 0

random_list = [1170654, 'Carolina']


####################
##      TODO      ##
####################

# 1. 1º login guarda na DB (Registo)
# 2. Procura na base de dados (SQL query)
# 3. Se existir informação na DB - login

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

        # # If someone wants to create an account
        # if(request.form['create'] == "true"):
        #     return redirect(url_for('sign_in'))

        else:
            db.connection_db(random_list, query="search")
            return redirect(url_for('homepage'))

    return render_template("login.html", error=error)


@app.route('/register', methods=['GET', 'POST'])
def sign_in():
    global error
    if(request.method == 'POST'):
        if(request.form['username'] == '' or request.form['pass'] == ''):
            error = 'Please provide some sign up information'
        else:
            params_to_insert = [
                request.form['username'], request.form['pass']
            ]
            db.connection_db(params_to_insert, query="insert")
            return redirect(url_for('login'))

    return render_template("registo.html", error=error)


@app.route('/get_back', methods=['GET', 'POST'])
def forgot_password():
    # # Resets password
    # if(request.method == 'GET'):
    #     if(request.form['forgot_password'] == "Forgot Password"):
    #         # Insert update method
    #         return render_template("forgot_password.html")
    #     else:
    #         error = 'Must provide a username for password recovery'

    return render_template("forgot_password.html")


@app.route('/connection')
def connect():
    db.connection_db(random_list)

    return redirect(url_for("main_page"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
