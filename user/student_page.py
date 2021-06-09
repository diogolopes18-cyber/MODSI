#!/usr/bin/env python3

import json
from flask import Flask, render_template, flash, request, redirect, url_for, Blueprint
import database_conn as db
from uuid import uuid4
from werkzeug.utils import secure_filename
import os


aluno = Blueprint('aluno', __name__)


@aluno.route('/aluno', methods=['GET', 'POST'])
def personal_page():
    return render_template("aluno.html")


@aluno.route('/aluno/submissions', methods=['GET', 'POST'])
def submited_papers():
    # Show submited files
    if(request.method == 'GET'):
        projects = db.connection_db(query="select", tablename="projetos")

    return render_template("submited_projects.html", data=projects)
