#!/usr/bin/env python3

import os
import json
import psycopg2
import configparser
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']


def connection_db(data_for_db, *args, **kwargs):

    query = kwargs.get('query', None)
    ######################
    # Connection details
    ######################
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')

    try:
        cursor = connection.cursor()
        print(connection.get_dsn_parameters(), "\n")

        #####################
        # Data insertion
        #####################
        if(query == "insert"):
            insert_query = "INSERT INTO alunos_modsi (mec_aluno, pass, mail) VALUES %s"
            assert len(data_for_db) != 0, "No data to insert"
            cursor.execute(
                insert_query, [(data_for_db[0], data_for_db[1], data_for_db[2])])

        elif(query == "search"):
            # Could also be "IF EXISTS(SELECT mec_aluno FROM alunos_modsi WHERE mec_aluno=%s) THEN
            #  raise notice 'yes'
            # END IF"
            search_query = "SELECT EXISTS(SELECT mec_aluno FROM alunos_modsi WHERE mec_aluno=%s)"
            cursor.execute(search_query, [data_for_db[0]])

        elif(query == "update"):
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
