import os
import json
import psycopg2
from flask import Flask
import database_conn as db

app = Flask(__name__)

random_list = [1170503, 'Diogo']


####################
##      TODO      ##
####################

# 1. 1º login guarda na DB (Registo)
# 2. Procura na base de dados (SQL query)
# 3. Se existir informação na DB - login

@app.route('/')
def main_page():

    text = '<a href="%s">Yolo bitches</a>'
    return text % connect()


@app.route('/login')
def connect():
    db.connection_db(random_list)

    return "Data inserted"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=65200)
