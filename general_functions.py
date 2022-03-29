import configparser
import json
from os.path import exists
from configparser import ConfigParser


def is_file_exist(file_name):
    if not exists(file_name):
        raise NameError('Wrong location/name of file')


def parse_program_text(file_name):
    is_file_exist(file_name)
    with open(file_name) as text_file:
        return json.load(text_file)


def postgresql_config_parser(file_name='database.ini'):
    is_file_exist(file_name)
    parser = ConfigParser()
    parser.read(file_name)
    db = {}
    try:
        for db_param in parser.items('postgresql'):
            db[db_param[0]] = db_param[1]
    except configparser.NoSectionError:
        print(f'Section postgresql has not been found in your file({file_name})')
    return db
