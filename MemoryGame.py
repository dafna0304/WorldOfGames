from time import sleep
from random import randint
from colorama import Fore, Back, Style, init
from Utils import screen_cleaner


def generate_sequence(difficulty):
    numbers = []

    for _ in range(0, difficulty):
        numbers.append(randint(1, 101))

    return numbers


def get_list_from_user(difficulty, sequence):
    print(f'\nAre you ready? Here are the numbers:')
    sleep(2.0)
    # show the sequence
    for index in range(0, difficulty):
        print(f'''\n{Back.YELLOW}{Fore.BLACK}{sequence[index]}{Style.RESET_ALL}''')
        sleep(0.7)

    screen_cleaner()
    user_inputs = []

    # user enters sequence
    for index in range(0, difficulty):
        valid_integer = False

        while not valid_integer:
            try:
                number_str = input(f'Enter integer #{index+1} > ')
                number = int(number_str)
                user_inputs.append(number)
                valid_integer = True
            except:
                print(f'''\n{Fore.RED}{number_str} is not a valid integer.{Style.RESET_ALL}''')

    return user_inputs


def is_list_equal(sequence, inputs):
    for index in range(0, len(sequence)):
        if sequence[index] is not inputs[index]:
            return False

    return True


def play(difficulty):
    sequence = generate_sequence(difficulty)

    return is_list_equal(sequence, get_list_from_user(difficulty, sequence))
