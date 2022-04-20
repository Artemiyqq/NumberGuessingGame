import os
import sys
from modules.work_with_files import File
from modules.input_parsing import ParseInput


class MainMenuClass:
    text = File.parse_program_text(os.path.realpath('localisation\\english_language.json'))
    menu_first_launch = True

    def main_menu(self):
        if self.menu_first_launch:
            print(self.text['greeting'], end='')
            self.menu_first_launch = False
        print(''.join(self.text["menu_text"]), end='')
        match ParseInput.get_correct_value(['1', '2', '3'], self.text['not_correct_value']):
            case '1': self.game_main()
            case '2': self.leader_board_main()
            case '3': sys.exit(self.text['parting'])
