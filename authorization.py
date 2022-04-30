from modules.input_parsing import ParseInput
from modules.database_postgresql import Database
from time import sleep
import getpass


class SignInClass:
    player_name = None
    player_name_entered = False
    player_password = None
    player_password_entered = False
    play_without_account = False
    remaining_log_attempts = 3

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
        match ParseInput.get_yes_no(self.text['after_errors_offer'], self.text['not_correct_value']):
            case 'yes':
                self.remaining_log_attempts = 3
                return self.account_menu()
            case 'no':
                self.remaining_log_attempts = 2

    def login_enter(self):
        player_name = input(self.text['sing_in_messages']['login'])
        if not Database.is_name_original(player_name):
            print(self.text['sing_in_messages']['correct_login'])
            self.player_name = player_name
            self.player_name_entered = True
        else:
            print(self.text['sing_in_errors']['login_error'])
            self.remaining_log_attempts -= 1

    def password_enter(self):
        player_password = getpass.getpass(prompt=self.text["sing_in_messages"]["password"])
        password_query = f"SELECT userpassword FROM users WHERE username = '{self.player_name}';"
        if Database.querying_db_data(password_query)[0][0] == player_password:
            self.player_password = player_password
            self.player_password_entered = True
            print(self.text['successfully_authorization'], end='')
            sleep(2)
        else:
            print(self.text['sing_in_errors']['password_error'])
            self.remaining_log_attempts -= 1


class SignUpClass:
    def get_new_login(self):
        while True:
            new_account_login = input(self.text['sing_up_messages']['login'])
            if not ParseInput.is_correct_len(new_account_login, 15):
                print(self.text['sing_up_errors']['len'], end='16\n')
            elif not new_account_login.isascii():
                print(self.text['sing_up_errors']['latin'])
            elif not Database.is_name_original(new_account_login):
                print(self.text['sing_up_errors']['existing_name'])
            else:
                return new_account_login

    def get_new_password(self):
        while True:
            new_account_password = getpass.getpass(prompt=self.text['sing_up_messages']['password'])
            if not ParseInput.is_correct_len(new_account_password, 20):
                print(self.text['sing_up_errors']['len'], end='21\n')
            elif not new_account_password.isascii():
                print(self.text['sing_up_errors']['latin'])
            else:
                if getpass.getpass(self.text['sing_up_messages']['confirm_password']) == new_account_password:
                    return new_account_password
                else:
                    print(self.text['sing_up_messages']['wrong_password_confirmation'])

    def create_an_account(self):
        new_account_login = self.get_new_login()
        new_account_password = self.get_new_password()
        account_creation_query = f"""INSERT INTO users VALUES ('{new_account_login}','{new_account_password}');
                                     INSERT INTO leader_board VALUES ('{new_account_login}');"""
        Database.insert_to_db(account_creation_query)
        print(self.text['successfully_account_creation'])
        return self.account_menu()


class AuthorizationMenuClass(SignInClass, SignUpClass):
    def account_menu(self):
        print(''.join(self.text["game_logging_menu"]), end='')
        match ParseInput.get_correct_value(['1', '2', '3', '4'], self.text['not_correct_value']):
            case '1': self.account_sign_in()
            case '2': self.create_an_account()
            case '3': self.play_without_account = True
            case '4':
                print()
                return self.main()
