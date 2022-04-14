import sys
import random
from modules.database_postgresql import Database


class LeaderboardClass:
    def print_top10(self):
        print(self.text['leader_board_message'])
        top_players = Database.querying_db_data("SELECT * FROM leader_board ORDER BY userscore DESC")
        for some_of_top in enumerate(self.text['top10']):
            try:
                print(f'{some_of_top[1]} {top_players[some_of_top[0]][0]} with {top_players[some_of_top[0]][1]} p.')
            except IndexError:
                print(f'{some_of_top[1]} ...')


class LeaderboardMenuClass(LeaderboardClass):
    def leader_board_menu(self):
        choose_in_menu = input(self.text['leader_board_menu'])
        while True:
            match choose_in_menu.lower():
                case "yes":
                    print()
                    return self.main()
                case "no": sys.exit(self.text['parting'])
                case _: choose_in_menu = input(random.choice(self.text['not_correct_value']))
