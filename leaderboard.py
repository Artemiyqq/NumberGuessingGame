import sys
from time import sleep
from modules.database_postgresql import Database
from modules.input_parsing import ParseInput


class LeaderboardClass:
    mini_words = {'English': ['with', 'p.'], 'Ukrainian': ['з', 'о.']}

    def print_top10(self):
        print(self.text['leader_board_message'])
        top_players = Database.querying_db_data("SELECT * FROM leader_board ORDER BY userscore DESC")
        for some_of_top in enumerate(self.text['top10']):
            try:
                print(f'{some_of_top[1]} '
                      f'{top_players[some_of_top[0]][0]} '
                      f'{self.mini_words[self.current_language][0]} '
                      f'{top_players[some_of_top[0]][1]} '
                      f'{self.mini_words[self.current_language][1]}')
            except IndexError:
                print(f'{some_of_top[1]} ...')
        sleep(4)


class LeaderboardMenuClass(LeaderboardClass):
    def leader_board_menu(self):
        match ParseInput.get_yes_no(self.text['leader_board_menu'], self.text['not_correct_value']):
            case "yes":
                print()
                return self.main()
            case "no": sys.exit(self.text['parting'])
