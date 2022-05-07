import sys
from modules.input_parsing import ParseInput


class MainMenuClass:
    menu_first_launch = True

    def main_menu(self):
        if self.menu_first_launch:
            print(self.text['greeting'], end='')
            self.menu_first_launch = False
        print(''.join(self.text["menu_text"]), end='')
        match ParseInput.get_correct_value(['1', '2', '3', '4'], self.text['not_correct_value']):
            case '1': self.game_main()
            case '2': self.leader_board_main()
            case '3': self.language_main()
            case '4': sys.exit(self.text['parting'])
