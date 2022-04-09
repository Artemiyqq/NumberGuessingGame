import random


class ParseInput:
    @staticmethod
    def get_correct_number(correct_values, error_messages):
        num_of_action = input()
        while True:
            if not num_of_action in correct_values:
                num_of_action = input(random.choice(error_messages))
            else:
                return num_of_action

    @staticmethod
    def get_yes_no(start_message, error_messages):
        entered_text = input(start_message).lower()
        while True:
            match entered_text:
                case 'yes' | 'no':
                    return entered_text
                case _:
                    entered_text = input(random.choice(error_messages)).lower()

    @staticmethod
    def is_correct_len(text, max_len):
        if 1 <= len(text) <= max_len:
            return True
        return False
