import random
import general_functions
import os
import sys


class LeaderBoardClass:
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
                    menu.main()
                    break
                case "no": sys.exit(self.text['parting'])
                case _: choose_in_menu = input(random.choice(self.text['not_correct_value']))

    def leader_board_main(self, text):
        self.text = text
        self.print_top10()
        self.leader_board_menu()


class AuthorizationClass:
    player_name = ""
    player_password = ""

    def account_menu(self):
        print(''.join(self.text["game_logging_menu"]))
        match general_functions.get_correct_number('123', self.text['not_correct_value']):
            case '1': self.account_sign_in()
            case '2':
                pass
            case '3':
                pass

    def account_sign_in(self):
        remaining_log_attempts = 5
        while True:
            if remaining_log_attempts == 0:
                match general_functions.get_yes_no(self.text['after_errors_offer'],self.text['not_correct_value']):
                    case 'yes':
                        self.account_menu()
                        break
                    case 'no':
                        remaining_log_attempts = 5

    def authorization_main(self,texte):
        self.texte = texte
        self.account_menu()


class GameClass(AuthorizationClass):
    def game_main(self, text):
        self.authorization_main(self.text)
        self.text = text


class MenuClass(LeaderBoardClass, GameClass):
    choose_in_menu = ''
    text = general_functions.parse_program_text(os.path.realpath('..\\localisation\\english_language.json'))
    menu_first_launch = True

    def choosing_action(self):
        if self.menu_first_launch:
            print(self.text['greeting'])
            self.menu_first_launch = False
        print(self.text['menu_text'], end='')
        self.num_of_action = general_functions.get_correct_number('123', self.text['not_correct_value'])

    def launch_selected_action(self):
        match self.num_of_action:
            case '1': super().game_main(self.text)
            case '2': super().leader_board_main(self.text)
            case '3': sys.exit(self.text['parting'])

    def main(self):
        self.choosing_action()
        self.launch_selected_action()


menu = MenuClass()
menu.main()
