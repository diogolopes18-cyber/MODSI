#!/usr/bin/env python3

import os
import json
import psycopg2
from flask import Flask, render_template, flash, request, redirect, url_for
import database_conn as db

app = Flask(__name__)

random_list = [1170503, 'Diogo']


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
def form():
    error = None
    if(request.method == 'POST'):
        if(request.form['username'] != "test" or request.form['password'] != "test"):
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('homepage'))

    return render_template("login.html", error=error)


@app.route('/connection')
def connect():
    db.connection_db(random_list)

    return redirect(url_for("main_page"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
