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


def connection_db(*args, **kwargs):

    global authorize

    data = kwargs.get('data', None)
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
        if(query == "insert"):
            if(tablename == "student"):
                insert_query = "INSERT INTO alunos_modsi (mec_aluno, pass, email) VALUES %s ON CONFLICT DO NOTHING;"
                assert len(data) != 0, "No data to insert"
                cursor.execute(
                    insert_query, [(data[0], data[1], data[2])])

            if(tablename == "orientador"):
                insert_query = "INSERT INTO orientador (sigla, pass, email) VALUES %s ON CONFLICT DO NOTHING;"
                assert len(data) != 0, "No data to insert"
                cursor.execute(
                    insert_query, [(data[0], data[1], data[2])])

            if(tablename == "diretor"):
                insert_query = "INSERT INTO diretor (sigla, pass, email) VALUES %s ON CONFLICT DO NOTHING;"
                assert len(data) != 0, "No data to insert"
                cursor.execute(
                    insert_query, [(data[0], data[1], data[2])])

            if(tablename == "projetos"):
                insert_query = "INSERT INTO projetos (nome_projeto, student_id, sigla_orientador) VALUES %s ON CONFLICT DO NOTHING;"
                assert len(data) != 0, "No data to insert"

                # Inserts project information
                for i in range(len(data)):
                    cursor.execute(insert_query,
                                   [(
                                       data[i]['title'],
                                       data[i]['student'],
                                       data[i]['orientador']
                                   )]
                                   )

        ###################
        ##  Data Search  ##
        ###################
        if(query == "search"):
            if(tablename == "student"):
                search_query = "SELECT EXISTS(SELECT (mec_aluno,pass) FROM alunos_modsi WHERE (mec_aluno,pass)=%s);"
                cursor.execute(search_query, [(data[0], data[1])])
                result = cursor.fetchone()
                if(str(result) == "(False,)"):
                    authorize = 0
                else:
                    authorize = 1

            if(tablename == "orientador"):
                search_orientador_query = "SELECT EXISTS(SELECT (sigla,pass) FROM orientador WHERE (sigla,pass)=%s);"
                cursor.execute(search_orientador_query, [(data[0], data[1])])
                result_orientador = cursor.fetchone()

                if(str(result_orientador) == "(False,)"):
                    authorize = 0
                else:
                    authorize = 1

            if(tablename == "diretor"):
                search_professor_query = "SELECT EXISTS(SELECT sigla FROM diretor WHERE sigla=%s);"
                cursor.execute(search_professor_query, [(data)])
                result_professor = cursor.fetchone()

                if(str(result_professor) == "(False,)"):
                    authorize = 0
                else:
                    authorize = 1

            return authorize

        #######################################
        ##  Check for not approved projects  ##
        #######################################
        if(query == "search" and tablename == "projetos"):
            search_projetos_query = "SELECT nome_projeto FROM projetos WHERE status_project IS NULL;"
            cursor.execute(search_projetos_query)
            result = cursor.fetchall()
            print("RESULT:", json.dumps(result, indent=2))

            return result

        ###################
        ##  SELECT DATA  ##
        ###################
        if(query == "select"):
            if(tablename == "projetos"):
                # Selects approved projects
                select_projetos_query = "SELECT nome_projeto FROM projetos WHERE status_project IS NOT NULL;"
                cursor.execute(select_projetos_query)
                result_projetos = cursor.fetchall()

                return result_projetos

            if(tablename == "orientador"):
                select_orientador_query = "SELECT sigla FROM orientador;"
                cursor.execute(select_orientador_query)
                result_orientador = cursor.fetchall()

                return result_orientador

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
