#!/usr/bin/env python3

from flask import Flask, render_template, flash, request, redirect, url_for, Blueprint
import database_conn as db


public = Blueprint('public', __name__)


@public.route('/public', methods=['GET', 'POST'])
def public_projects():

    if(request.method == 'GET'):
        # Request approved projects
        approved_projects = db.connection_db(query="select", tablename="projetos", public="true")

    return render_template("publico.html", data=approved_projects)
