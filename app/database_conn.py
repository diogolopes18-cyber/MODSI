#!/usr/bin/env python3

import os
import json
import psycopg2
import configparser


config = configparser.ConfigParser()
config.read(
    '/home/diogo/Mestrado/MODSI/information_system/db/database_info.ini', encoding='utf-8')


def connection_db(data_for_db):

    try:
        connection = psycopg2.connect(user=config['db']['user'],
                                      password=config['db']['password'],
                                      host=config['db']['host'],
                                      port=config['db']['port'],
                                      database=config['db']['database'])
        ######################
        # Connection details
        ######################
        cursor = connection.cursor()
        print(connection.get_dsn_parameters(), "\n")

        #####################
        # Data insertion
        #####################
        insert_query = "INSERT INTO alunos_modsi (mec_aluno, nome) VALUES %s"
        cursor.execute(
            insert_query, [(data_for_db[0], data_for_db[1])])

        connection.commit()
        print("Data inserted")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        connection.close()

    print("Closing...")
