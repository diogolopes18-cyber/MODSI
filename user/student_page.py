#!/usr/bin/env python3

from flask import Flask, render_template, flash, request, redirect, url_for, Blueprint
import database_conn as db


aluno = Blueprint('aluno', __name__)


@aluno.route('/aluno', methods=['GET', 'POST'])
def personal_page():
    return render_template("aluno.html")


@aluno.route('/aluno/submissions', methods=['GET', 'POST'])
def submited_papers():
    # Show submited files
    if(request.method == 'GET'):
        projects = db.connection_db(query="select", tablename="projetos", public="false")

    return render_template("submited_projects.html", data=projects)


@aluno.route('/aluno/submit_tema', methods=['GET', 'POST'])
def submit_theme():
    if(request.method == 'POST'):

        # Submits a theme and the status becomes to_approve
        data = [
            {
                'title': request.form['title'],
                'status': 'to_approve',
                'student': request.form['student'],
                'orientador': request.form['orientador']
            }
        ]

        db.connection_db(data=data, query="insert", tablename="projetos")

    return render_template("submit_tema.html")
