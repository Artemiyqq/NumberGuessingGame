import random
import general_functions
import os
import sys
import getpass


class LeaderBoardClass:
    def print_top10(self):
        print(self.text['leader_board_message'])
        top_players = general_functions.querying_db_data("SELECT * FROM leader_board ORDER BY userscore DESC",
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
                    print()
                    return menu.main()
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
    remaining_log_attempts = 3

    def account_menu(self):
        print(''.join(self.text["game_logging_menu"]), end='')
        match general_functions.get_correct_number('1234', self.text['not_correct_value']):
            case '1': self.account_sign_in()
            case '2': self.create_an_account()
            case '3':
                pass
            case '4': return menu.main()

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
                self.remaining_log_attempts = 3
                return self.account_menu()
            case 'no':
                self.remaining_log_attempts = 2

    def login_enter(self):
        player_name = input(self.text['sing_in_messages']['login'])
        if not general_functions.is_name_original(player_name, self.db_config_location):
            print(self.text['sing_in_messages']['correct_login'])
            self.player_name = player_name
            self.player_name_entered = True
        else:
            print(self.text['sing_in_errors']['login_error'])
            self.remaining_log_attempts -= 1

    def password_enter(self):
        player_password = getpass.getpass(prompt=self.text["sing_in_messages"]["password"])
        password_query = f"SELECT userpassword FROM users WHERE username = '{self.player_name}';"
        if general_functions.querying_db_data(password_query, self.db_config_location)[0][0] == player_password:
            self.player_password = player_password
            self.player_password_entered = True
            print(self.text['successfully_authorization'])
        else:
            print(self.text['sing_in_errors']['password_error'])
            self.remaining_log_attempts -= 1

    def get_new_login(self):
        while True:
            new_account_login = input(self.text['sing_up_messages']['login'])
            if not general_functions.is_correct_len(new_account_login, 15):
                print(self.text['sing_up_errors']['len'], end='16\n')
            elif not general_functions.is_english_text(new_account_login):
                print(self.text['sing_up_errors']['latin'])
            elif not general_functions.is_name_original(new_account_login, self.db_config_location):
                print(self.text['sing_up_errors']['existing_name'])
            else:
                return new_account_login

    def get_new_password(self):
        while True:
            new_account_password = getpass.getpass(prompt=self.text['sing_up_messages']['password'])
            if not general_functions.is_correct_len(new_account_password, 20):
                print(self.text['sing_up_errors']['len'], end='21\n')
            elif not general_functions.is_english_text(new_account_password):
                print(self.text['sing_up_errors']['latin'])
            else:
                if getpass.getpass(self.text['sing_up_messages']['confirm_password']) == new_account_password:
                    return new_account_password
                else:
                    print(self.text['sing_up_messages']['wrong_password_confirmation'])

    def create_an_account(self):
        new_account_login = self.get_new_login()
        new_account_password = self.get_new_password()
        account_creation_query = f"INSERT INTO users VALUES ('{new_account_login}','{new_account_password}');" \
                                 f"INSERT INTO leader_board VALUES ('{new_account_login}');"
        general_functions.insert_to_db(account_creation_query, self.db_config_location)
        print(self.text['successfully_account_creation'])
        return self.account_menu()

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
            print(self.text['greeting'], end='')
            self.menu_first_launch = False
        print(''.join(self.text["menu_text"]), end='')
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
