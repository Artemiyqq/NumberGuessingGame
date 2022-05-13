import os
from modules.work_with_files import File


class LanguageClass:
    languages = {'English': File.parse_program_text(os.path.realpath('localisation\\english_language.json')),
                 'Ukrainian': File.parse_program_text(os.path.realpath('localisation\\ukrainian_language.json'))}
    current_language = 'English'
    text = languages[current_language]

    def change_language(self):
        if self.current_language == 'English':
            self.current_language = 'Ukrainian'
        else:
            self.current_language = 'English'
        self.text = self.languages[self.current_language]
        print()
