#!/usr/bin/env python3

import os
import json
import psycopg2
import configparser


# Parses file
config = configparser.ConfigParser()
config.read('db/database_info.ini', encoding='utf-8')

authorize = None


def connection_db(data_for_db, *args, **kwargs):

    global authorize
    query = kwargs.get('query', None)
    tablename = kwargs.get('tablename', None)
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
        if(query == "insert" and tablename == "student"):
            insert_query = "INSERT INTO alunos_modsi (mec_aluno, pass, email) VALUES %s ON CONFLICT DO NOTHING;"
            assert len(data_for_db) != 0, "No data to insert"
            cursor.execute(
                insert_query, [(data_for_db[0], data_for_db[1], data_for_db[2])])

        if(query == "insert" and tablename == "diretor"):
            insert_query = "INSERT INTO diretor (sigla, pass, email) VALUES %s ON CONFLICT DO NOTHING;"
            assert len(data_for_db) != 0, "No data to insert"
            cursor.execute(
                insert_query, [(data_for_db[0], data_for_db[1], data_for_db[2])])

        ###################
        ##  Data Search  ##
        ###################
        if(query == "search" and tablename == "student"):
            search_query = "SELECT EXISTS(SELECT mec_aluno FROM alunos_modsi WHERE mec_aluno=%s)"
            cursor.execute(search_query, [(data_for_db)])
            result = cursor.fetchone()
            if(str(result) == "(False,)"):
                authorize = 0
            else:
                authorize = 1

        if(query == "search" and tablename == "diretor"):
            search_professor_query = "SELECT EXISTS(SELECT sigla FROM diretor WHERE sigla=%s)"
            cursor.execute(search_professor_query, [(data_for_db)])
            result_professor = cursor.fetchone()

            if(str(result) == "(False,)"):
                authorize = 0
            else:
                authorize = 1

        ###################
        ##  Data Update  ##
        ###################

        if(query == "update"):
            update_query = "UPDATE alunos_modsi SET pass=%s WHERE username=%s"
            cursor.execute(update_query, [(data_for_db[1], data_for_db[0])])

        #####################
        # Data commit
        #####################
        connection.commit()
        cursor.close()
        #print("Query sucessful")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

    return authorize
