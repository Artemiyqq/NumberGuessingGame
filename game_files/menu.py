import random
import general_functions
import os
import sys


class MenuClass:
    text = general_functions.parse_program_text(os.path.realpath('..\\localisation\\english_language.json'))

    def choosing_action(self):
        self.num_of_action = input(f"{self.text['greeting']}{self.text['menu_text']}")
        while True:
            if not self.num_of_action in '123':
                self.num_of_action = input(random.choice(self.text['not_correct_value']))
            else:
                break

    def launch_selected_action(self):
        match self.num_of_action:
            case '1':
                pass
            case '2':
                pass
            case '3': sys.exit(self.text['parting'])

    def main(self):
        self.choosing_action()
        self.launch_selected_action()


menu = MenuClass()
menu.main()
