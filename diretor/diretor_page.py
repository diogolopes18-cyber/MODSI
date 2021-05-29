#!/usr/bin/env python3

import os
import json
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, session, abort, Blueprint
import database_conn as db

# App context
diretor = Blueprint('professor', __name__, template_folder='templates')


@diretor.route('/diretor', methods=['GET', 'POST'])
def professor_page():

    return render_template("diretor.html")


# @diretor.route('/diretor/login', methods=['GET', 'POST'])
# def professor_login():
#     if(request.method == 'POST'):
#         if(request.form['username'] == "" or request.form['password'] == ""):
#             error = 'No credentials provided. Please try again.'
#         else:
#             authorization = db.connection_db(request.form['username'], query="search", professor="true")

#             if(authorization == 1):
#                 return redirect(url_for('professor_page'))
#             elif(authorization == 0):
#                 error = 'Invalid Credentials. Please try again.'
#                 return render_template("login.html", error=error)

#     return render_template("index.html")
