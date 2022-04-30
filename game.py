import random
from time import sleep
from modules.input_parsing import ParseInput
from modules.database_postgresql import Database


class GameClass:
    num_ranges = {"1": range(1, 6), "2": range(1, 11), "3": range(1, 21)}
    chosen_num_range = None
    guessed_number = None
    points_for_win = None
    probable_value = None
    continue_guessing = True
    first_game = True

    def game_start_messages(self):
        if ParseInput.get_yes_no(''.join(self.text['need_of_tutorial']),
                                 self.text['not_correct_value']).lower() == 'yes':
            print(self.text['exit_possibility'])
            sleep(3)
            print(''.join(self.text['game_rules']))
            sleep(10)

    def get_nums_range(self):
        self.chosen_num_range = ParseInput.get_correct_value(['1', '2', '3', 'exit'],
                                                             self.text['not_correct_value'],
                                                             ''.join(self.text['nums_range_menu']))
        if self.chosen_num_range == 'exit':
            return self.main_menu

    def set_win_points(self):
        self.points_for_win = int(len(self.num_ranges[self.chosen_num_range]))

    def choose_the_num(self):
        self.guessed_number = str(random.choice(self.num_ranges[self.chosen_num_range]))

    def is_correct_assumption(self):
        if self.probable_value == self.guessed_number:
            self.continue_guessing = False
            self.win()
        else:
            self.points_for_win -= 1
            self.probable_value = str(input(self.text['wrong_intend']))

    def player_inputted_exit(self):
        if self.probable_value == 'exit':
            self.continue_guessing = False
            print()
            return self.main_menu()

    def check_probable_value(self):
        if int(self.probable_value) in self.num_ranges[self.chosen_num_range]:
            self.is_correct_assumption()
        else:
            self.probable_value = str(input(self.text['out_of_range']))

    def win(self):
        self.continue_guessing = False
        print(self.text['win_message'][0], self.points_for_win, self.text['win_message'][1])
        if not self.play_without_account:
            Database.update_user_score(self.player_name, self.points_for_win)
        sleep(3)
        self.after_win_menu()

    def guess_the_number(self):
        self.continue_guessing = True
        print(self.text["num_entering_massages"][0])
        sleep(1)
        self.probable_value = str(input(self.text['num_entering_massages'][1])).lower()
        while self.continue_guessing:
            self.player_inputted_exit()
            if self.probable_value.isdigit():
                self.check_probable_value()
            elif self.continue_guessing:
                self.probable_value = str(input(self.text['not_num_value'])).lower()

    def set_pregame_settings(self):
        self.chosen_num_range = None
        self.guessed_number = None
        self.points_for_win = None
        self.probable_value = None
        self.continue_guessing = True

    def reset(self):
        self.first_game = True
        self.player_name = None
        self.player_name_entered = False
        self.player_password = None
        self.player_password_entered = False
        self.play_without_account = False


class GameMenuClass(GameClass):
    def start_the_game(self):
        self.set_pregame_settings()
        self.game_start_messages()
        self.get_nums_range()
        self.set_win_points()
        self.choose_the_num()
        self.guess_the_number()

    def after_win_menu(self):
        match ParseInput.get_correct_value(['1', '2'],
                                           self.text['not_correct_value'],
                                           ''.join(self.text['after_win_menu'])):
            case '1':
                print()
                self.first_game = False
                self.start_the_game()
            case '2':
                print()
                self.reset()
                return self.main()
