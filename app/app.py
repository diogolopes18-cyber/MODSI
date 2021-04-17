import os
import json
import psycopg2
from flask import Flask
import database_conn as db

# app = Flask(__name__)

random_list = [1170503, 'Diogo']


# @app.route('/')
# def main_page():

#     text = '<a href="%s">Yolo bitches</a>'
#     return text % connect()


def connect():
    db.connection_db(random_list)


if __name__ == "__main__":
    # app.run(debug=True, port=65200)
    connect()
