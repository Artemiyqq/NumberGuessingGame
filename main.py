from authorization import AuthorizationMenuClass
from leaderboard import LeaderboardMenuClass
from game import GameMenuClass
from main_menu import MainMenuClass


class AllClassesMenu(LeaderboardMenuClass, GameMenuClass, AuthorizationMenuClass, MainMenuClass):
    def game_main(self):
        self.authorization_main()

    def authorization_main(self):
        self.account_menu()

    def leader_board_main(self):
        self.print_top10()
        self.leader_board_menu()

    def main(self):
        self.main_menu()


menu = AllClassesMenu()
menu.main()
