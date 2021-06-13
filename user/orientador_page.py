#!/usr/bin/env python3

from dotenv.main import load_dotenv
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, session, abort, Blueprint
import database_conn as db


# App context
orientador = Blueprint('orientador', __name__)


@orientador.route('/orientador', methods=['GET', 'POST'])
def orientador_page():

    return render_template("orientador.html")


@orientador.route('/orientador/projects', methods=['GET', 'POST'])
def new_projects():
    # Submit new project proposals
    if(request.method == 'POST'):

        suggestions = [
            {
                "sigla": request.form['sigla'],
                "nome_projeto": request.form['name'],
                "description": request.form['description']
            }
        ]

        db.connection_db(data=suggestions, query="insert", tablename="orientador_suggestions")

    return render_template("project_suggestion.html")


@orientador.route('/orientador/projects/available', methods=['GET', 'POST'])
def available_projects():

    projects = db.connection_db(query="select", tablename="orientador_suggestions")
    return render_template("available_projects.html", data=projects)


@orientador.route('/orientador/submit_grade', methods=['GET', 'POST'])
def submit_grade():

    if(request.method == 'POST'):

        # Submit final grade
        grade = {
            "student": request.form['student'],
            "project_name": request.form['project'],
            "grade": request.form['note']
        }

        # Insert data into DB
        db.connection_db(data=grade, query="insert", tablename="grades")

    return render_template("final_grade.html")
