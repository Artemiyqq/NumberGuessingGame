import json
from os.path import exists


def parse_program_text(file_location):
    if not exists(file_location):
        raise NameError('Wrong location of file')
    with open(file_location) as text_file:
        return json.load(text_file)
