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
    db_config_location = os.path.realpath('..\\database.ini')
    player_name = ""
    player_name_entered = False
    player_password = ""
    player_password_entered = False
    remaining_log_attempts = 5

    def account_menu(self):
        print(''.join(self.text["game_logging_menu"]), end='')
        match general_functions.get_correct_number('123', self.text['not_correct_value']):
            case '1': self.account_sign_in()
            case '2':
                pass
            case '3':
                pass

    def account_sign_in(self):
        while True:
            if self.remaining_log_attempts == 0:
                self.zero_log_attempts()
            elif not self.player_name_entered:
                self.login_enter()
            elif not self.player_password_entered:
                self.password_enter()
            else:
                break

    def zero_log_attempts(self):
        match general_functions.get_yes_no(self.text['after_errors_offer'], self.text['not_correct_value']):
            case 'yes':
                return self.account_menu()
            case 'no':
                self.remaining_log_attempts = 5

    def login_enter(self):
        player_name = input(self.text['sing_in_messages'][0]['login'])
        name_query = f"SELECT userpassword FROM users WHERE username = '{player_name}';"
        if len(general_functions.querying_data(name_query, self.db_config_location)) > 0:
            self.player_name = player_name
            self.player_name_entered = True
        else:
            print(self.text['sing_in_errors'][0]['login_error'])

    def password_enter(self):
        first_try = True
        player_password = input(self.text['sing_in_messages'][0]['password'])
        password_query = f"SELECT userpassword FROM users WHERE username = '{self.player_name}';"
        if general_functions.querying_data(password_query, self.db_config_location) == player_password:
            self.player_password = player_password
            self.player_password_entered = True
        else:
            print(self.text['sing_in_errors'][0]['password_error'])

    def authorization_main(self, text):
        self.text = text
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
