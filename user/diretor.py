#!/usr/bin/env python3

from flask import Flask, render_template, flash, request, redirect, url_for, Blueprint
import database_conn as db
import json

diretor = Blueprint('diretor', __name__)


@diretor.route('/diretor', methods=['GET', 'POST'])
def diretor_page():
    return render_template("diretor.html")


@diretor.route('/diretor/approval', methods=['GET', 'POST'])
def approve_papers():
    if(request.method == 'GET'):
        # Search for projects with null status on DB
        result = db.connection_db(query="search", tablename="projetos")

    return render_template("approved.html", data=result)
