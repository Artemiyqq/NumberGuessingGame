import os
from modules.work_with_files import File


class LanguageClass:
    languages_locations = {'English': File.parse_program_text(os.path.realpath('localisation\\english_language.json'))}
    text = languages_locations['English']

    def change_language_main(self):
        pass
