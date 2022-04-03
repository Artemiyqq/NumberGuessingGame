import configparser
import json
from os.path import exists
from configparser import ConfigParser
import psycopg2
import random


def is_file_exist(file_name):
    if not exists(file_name):
        raise NameError('Wrong location/name of file', file_name)


def parse_program_text(file_name):
    is_file_exist(file_name)
    with open(file_name) as text_file:
        return json.load(text_file)


def postgresql_config_parser(file_name='database.ini'):
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


def querying_data(query, db_config_loc="database.ini"):
    connection = None
    query_data = []
    try:
        connection = psycopg2.connect(postgresql_config_parser(db_config_loc))
        cursor = connection.cursor()
        cursor.execute(query)
        query_data = cursor.fetchall()
        return query_data
    finally:
        if connection is not None:
            connection.close()


def get_correct_number(correct_values, error_messages):
    num_of_action = input()
    while True:
        if not num_of_action in correct_values:
            num_of_action = input(random.choice(error_messages))
        else:
            return num_of_action


def get_yes_no(start_message, error_messages):
    entered_text = input(start_message).lower()
    while True:
        match entered_text:
            case 'yes' | 'no':
                return entered_text
            case _:
                entered_text = input(random.choice(error_messages)).lower()


def is_english_text(text):
    return text.isasscii()
