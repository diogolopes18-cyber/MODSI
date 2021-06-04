#!/usr/bin/env python3


from os import abort
from flask import Flask, render_template, flash, request, redirect, url_for, Blueprint
import database_conn as db
import json


diretor = Blueprint('diretor', __name__)


@diretor.route('/diretor/login', methods=['GET', 'POST'])
def login_diretor():
    if(request.method == 'POST'):
        assert len(request.form['username']) > 0, "Empty value"

        # Checks for the username and password on DB
        authorization = db.connection_db(
            data=request.form['username'], query="search", tablename="diretor")

        if(authorization == 1):
            return redirect(url_for('diretor_page'))
        elif(authorization == 0):
            error = 'Invalid Credentials. Please try again.'
            return render_template("login.html", error=error)


@diretor.route('/diretor/workspace', methods=['GET', 'POST'])
def diretor_page():
    if(request.method == 'GET'):
        data = db.connection_db(query="select", tablename="projetos")
        data_json = json.dumps(data)

        # Present to page
        return render_template("diretor.html", data=data_json)
