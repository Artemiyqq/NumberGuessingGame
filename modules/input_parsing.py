import random


class ParseInput:
    @staticmethod
    def get_correct_value(correct_values, error_messages):
        value = input()
        while True:
            if value.lower() in correct_values:
                return value.lower()
            else:
                value = input(random.choice(error_messages))

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
