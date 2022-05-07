from authorization import AuthorizationMenuClass
from leaderboard import LeaderboardMenuClass
from main_menu import MainMenuClass
from game import GameMenuClass
from language import LanguageClass


class AllClassesMenu(LeaderboardMenuClass, GameMenuClass, AuthorizationMenuClass, MainMenuClass, LanguageClass):
    def game_main(self):
        self.authorization_main()
        self.start_the_game()

    def authorization_main(self):
        self.account_menu()

    def leader_board_main(self):
        self.print_top10()
        self.leader_board_menu()

    def change_language_main(self):
        pass

    def main(self):
        self.main_menu()


menu = AllClassesMenu()
menu.main()
