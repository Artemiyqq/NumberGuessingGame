from time import sleep
import random
from modules.input_parsing import ParseInput

class GameClass:
    num_ranges = {"1": range(1, 6), "2": range(1, 11), "3": range(1, 21)}
    chosen_num_range = None
    guessed_number = None

    def game_start_massages(self):
        print(self.text['exit_possibility'])
        sleep(3)
        print(''.join(self.text['game_rules']))
        sleep(10)

    def get_nums_range(self):
        self.chosen_num_range = ParseInput.get_correct_value(['1', '2', '3', 'exit'], self.text['not_correct_value'])
        if self.chosen_num_range == 'exit':
            return self.main_menu

    def guess_the_number(self):
        self.guessed_number = random.choice(self.num_ranges[self.chosen_num_range])
        

class GameMenuClass(GameClass):
    def start_the_game(self):
        self.game_start_massages()
        self.get_nums_range()
        self.guess_the_number()
