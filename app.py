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
def main_page():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def form():
    return render_template("login.html")


@app.route('/connection')
def connect():
    db.connection_db(random_list)

    return redirect(url_for("main_page"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
