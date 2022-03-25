import sys
import random
from localisation import english_language as text


def choosing_action():
    num_of_action = input(text.menu_text)
    while True:
        if not num_of_action in '123':
            num_of_action = input(random.choice(text.not_correct_value))
        else:
            return num_of_action


def proces
def main():
    choosing_action()


main()
