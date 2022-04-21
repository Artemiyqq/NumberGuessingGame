from time import sleep
import random
from modules.input_parsing import ParseInput


class GameClass:
    num_ranges = {"1": range(1, 6), "2": range(1, 11), "3": range(1, 21)}
    chosen_num_range = None
    guessed_number = None
    points_for_win = None
    probable_value = None
    continue_guessing = True

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
    
    def win(self):
        pass

    def guess_the_number(self):
        print(self.text["num_entering_massages"][0])
        self.probable_value = str(input(self.text['num_entering_massages'][1])).lower()
        while self.continue_guessing:
            if self.probable_value == 'exit':
                self.continue_guessing = False
                return self.main_menu
            elif self.probable_value.isdigit():
                if int(self.probable_value) in self.num_ranges[self.chosen_num_range]:
                    self.is_correct_assumption()
                else:
                    self.probable_value = str(input(self.text['out_of_range']))


class GameMenuClass(GameClass):
    def start_the_game(self):
        self.game_start_messages()
        self.get_nums_range()
        self.set_win_points()
        self.choose_the_num()
        self.guess_the_number()
