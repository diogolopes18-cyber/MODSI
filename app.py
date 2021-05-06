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
            return redirect(url_for('homepage'))

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
            # Insert update method
            error = 'Provide new data'
        else:
            update = [
                request.form['new_username'], request.form['new_password']
            ]
            db.connection_db(update, query="update")
            return redirect(url_for('login'))

    return render_template("forgot_password.html", error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
