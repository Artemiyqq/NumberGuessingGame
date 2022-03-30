import configparser
import json
import sys
from os.path import exists
from configparser import ConfigParser
import psycopg2


def is_file_exist(file_name):
    if not exists(file_name):
        raise NameError('Wrong location/name of file')


def parse_program_text(file_name):
    sys.path.append('..')
    is_file_exist(file_name)
    with open(file_name) as text_file:
        return json.load(text_file)


def postgresql_config_parser(file_name='database.ini'):
    sys.path.append('..')
    is_file_exist(file_name)
    parser = ConfigParser()
    parser.read(file_name)
    db = []
    try:
        for db_param in parser.items('postgresql'):
            db.append(f'{db_param[0]}={db_param[1]}')
    except configparser.NoSectionError:
        print(f'Section postgresql has not been found in your file({file_name})')
    return ' '.join(db)


def querying_data(query, db_params_loc="database.ini"):
    connection = None
    query_data = []
    try:
        connection = psycopg2.connect(postgresql_config_parser(db_params_loc))
        cursor = connection.cursor()
        cursor.execute(query)
        query_data = cursor.fetchall()
        return query_data
    finally:
        if connection is not None:
            connection.close()
