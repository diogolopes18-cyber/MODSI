#!/usr/bin/env python3

import os
import json
import psycopg2
import configparser

# Parses file
config = configparser.ConfigParser()
config.read('db/database_info.ini', encoding='utf-8')

# Importing SQL files


def connection_db(data_for_db, *args, **kwargs):

    query = kwargs.get('query', None)
    ######################
    # Connection details
    ######################
    connection = psycopg2.connect(user=config['db']['user'],
                                  password=config['db']['password'],
                                  host=config['db']['host'],
                                  port=config['db']['port'],
                                  database=config['db']['database'])

    try:
        cursor = connection.cursor()
        print(connection.get_dsn_parameters(), "\n")

        #####################
        # Data insertion
        #####################
        if(query == "insert"):
            insert_query = "INSERT INTO alunos_modsi (mec_aluno, nome) VALUES %s"
            assert len(data_for_db) != 0, "No data to insert"
            cursor.execute(insert_query, [(data_for_db[0], data_for_db[1])])

        elif(query == "search"):
            search_query = "SELECT EXISTS(SELECT mec_aluno FROM alunos_modsi WHERE mec_aluno=%s);"
            cursor.execute(search_query, [data_for_db[0]])

        elif(query == "update"):
            print("Test")
        #####################
        # Data commit
        #####################
        connection.commit()
        print("Query sucessful")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        connection.close()

    print("Closing...")
