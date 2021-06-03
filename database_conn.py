#!/usr/bin/env python3

import os
import json
import psycopg2
import configparser

from werkzeug.wrappers import CommonRequestDescriptorsMixin


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
            search_query = "SELECT EXISTS(SELECT mec_aluno FROM alunos_modsi WHERE mec_aluno=%s);"
            cursor.execute(search_query, [(data_for_db)])
            result = cursor.fetchone()
            if(str(result) == "(False,)"):
                authorize = 0
            else:
                authorize = 1

        if(query == "search" and tablename == "diretor"):
            search_professor_query = "SELECT EXISTS(SELECT sigla FROM diretor WHERE sigla=%s);"
            cursor.execute(search_professor_query, [(data_for_db)])
            result_professor = cursor.fetchone()
            print(result_professor)

            if(str(result) == "(False,)"):
                authorize = 0
            else:
                authorize = 1

        if(query == "search" and tablename == "projetos"):
            search_projetos_query = "SELECT EXISTS(SELECT status_project FROM projetos WHERE status_project=null);"
            cursor.execute(search_projetos_query)
            result = cursor.fetchall()
            print("RESULT:", json.dumps(result, indent=2))

            ###################
            ##  Data Update  ##
            ###################

            ################################
            ##      UNDER DEVELOPMENT     ##
            ################################
            # if(query == "update"):
            #     if(tablename == "student"):
            #         update_query = "UPDATE alunos_modsi SET pass=%s WHERE username=%s"
            #         cursor.execute(update_query, [(data_for_db[1], data_for_db[0])])

            #     elif(tablename == "diretor"):
            #         update_query = "INSERT INTO projetos (status_project) VALUES=%s;"
            #         cursor.execute(update_query, [data_for_db])

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
