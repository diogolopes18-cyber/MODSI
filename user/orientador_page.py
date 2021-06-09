#!/usr/bin/env python3

import os
import json
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

#############################
# 1. Route para approve
#############################

# @diretor.route('/diretor/approve', methods=['GET', 'POST'])
# def approved_projects(prof_name):
#     if(request.method == 'GET'):
#         assert len(prof_name) > 0, "No name provided"
#         prof_exist = db.connection_db(prof_name, query="search", tablename="diretor")

#         if(prof_exist == 1):
#             if(request.form['approve_button'] == 'approve'):
#                 # Update column status_project of table projetos with approved
#                 status = "approved"
#                 db.connection_db(status, query="update", tablename="diretor")
#         else:
#             pass

#     return render_template("professor_aprove.html")


# @diretor.route('/diretor/proposals', methods=['GET', 'POST'])
# def proposals():
#     # Presents proposed projects by professor

#     if(request.method == 'POST'):
#         if(request.form['propose_project'] == "true"):
#             # Insert text box
#         else:
#             pass

#     elif(request.method == 'GET'):
#         # Fetch from DB and present to HTML page
#         projects_from_professor = db.connection_db()
#         return render_template("diretor_proposals.html", data=projects_from_professor)
