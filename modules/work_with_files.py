import configparser
import json
from os.path import exists
from configparser import ConfigParser


class File:
    @staticmethod
    def is_file_exist(file_name):
        if not exists(file_name):
            raise NameError('Wrong location/name of file', file_name)

    @classmethod
    def parse_program_text(cls, file_name):
        cls.is_file_exist(file_name)
        with open(file_name) as text_file:
            return json.load(text_file)

    @classmethod
    def postgresql_config_parser(cls, file_name='database.ini'):
        cls.is_file_exist(file_name)
        parser = ConfigParser()
        parser.read(file_name)
        db = []
        try:
            for db_param in parser.items('postgresql'):
                db.append(f'{db_param[0]}={db_param[1]}')
        except configparser.NoSectionError:
            print(f'Section postgresql has not been found in your file({file_name})')
        return ' '.join(db)
