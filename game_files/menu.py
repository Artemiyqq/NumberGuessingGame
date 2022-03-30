import random
import general_functions
import os
import sys


class LeaderBoardClass:
    text = general_functions.parse_program_text(os.path.realpath('..\\localisation\\english_language.json'))

    def print_top10(self):
        print(self.text['leader_board_message'])
        top_players = general_functions.querying_data("SELECT * FROM leader_board ORDER BY userscore DESC",
                                                      os.path.realpath("..\\database.ini"))
        for some_of_top in enumerate(self.text['top10']):
            try:
                print(f'{some_of_top[1]} {top_players[some_of_top[0]][0]} with {top_players[some_of_top[0]][1]} p.')
            except IndexError:
                print(f'{some_of_top[1]} ...')

    def leader_board_menu(self):
        choose_in_menu = input(self.text['leader_board_menu'])
        while True:
            match choose_in_menu.lower():
                case "yes":
                    self.main()
                    break
                case "no": sys.exit(self.text['parting'])
                case _: choose_in_menu = input(random.choice(self.text['not_correct_value']))

    def main(self):
        self.print_top10()
        self.leader_board_menu()


class MenuClass(LeaderBoardClass):
    menu_first_launch = True

    def choosing_action(self):
        if self.menu_first_launch:
            print(self.text['greeting'])
            self.menu_first_launch = False
        self.num_of_action = input(f"{self.text['menu_text']}")
        while True:
            if not self.num_of_action in '123':
                self.num_of_action = input(random.choice(self.text['not_correct_value']))
            else:
                break

    def launch_selected_action(self):
        match self.num_of_action:
            case '1':
                pass
            case '2': super().main()
            case '3': sys.exit(self.text['parting'])

    def main(self):
        self.choosing_action()
        self.launch_selected_action()


menu = MenuClass()
menu.main()
