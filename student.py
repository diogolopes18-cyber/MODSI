#!/usr/bin/env python3

from flask import Flask, render_template, flash, request, redirect, url_for, Blueprint
import database_conn as db
from uuid import uuid4
from werkzeug.utils import secure_filename
import os


student = Blueprint('student', __name__)


###########################################
##        STUDENT INFORMATION            ##
###########################################

@student.route('/aluno', methods=['GET', 'POST'])
def submit_paper():
    if(request.method == 'POST'):
        uploaded_file = request.files['input_name']
        assert len(uploaded_file) > 0, "File size must be greater than zero"

    return render_template("aluno.html")
