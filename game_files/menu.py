import random
import general_functions
import os


class MenuClass:
    text = general_functions.parse_program_text(os.path.realpath('..\\localisation\\english_language.json'))

    def choosing_action(self):
        num_of_action = input(self.text['menu_text'])
        while True:
            if not num_of_action in '123':
                num_of_action = input(random.choice(self.text['not_correct_value']))
            else:
                return num_of_action

    def main(self):
        self.choosing_action()


menu = MenuClass()
menu.choosing_action()
