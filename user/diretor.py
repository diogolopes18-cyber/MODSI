#!/usr/bin/env python3


import os
from flask import Flask, render_template, flash, request, redirect, url_for, Blueprint
import database_conn as db
from dotenv import load_dotenv
import json

# ENV variables
load_dotenv()
diretor_username = os.getenv('DIRETOR_USERNAME')
diretor_password = os.getenv('DIRETOR_PASSWORD')

diretor = Blueprint('diretor', __name__)


@diretor.route('/diretor/login', methods=['GET', 'POST'])
def login_diretor():
    if(request.method == 'POST'):
        assert len(request.form['username']) > 0, "Empty value"

        if(request.form['username'] == diretor_username and request.form['password'] == diretor_password):
            return render_template("diretor.html")
        else:
            return redirect(url_for('app.login'))

    # return render_template("login.html")


@diretor.route('/diretor/workspace', methods=['GET', 'POST'])
def diretor_page():
    if(request.method == 'GET'):
        data = db.connection_db(query="select", tablename="projetos")
        data_json = json.dumps(data)

    # Present to page
    return render_template("diretor.html", data=data_json)
