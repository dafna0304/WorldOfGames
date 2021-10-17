from random import randint
from colorama import Fore, Back, Style, init
secret_number: int

def generate_number(difficulty):
    global secret_number
    secret_number = randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    guess_str: str
    while True:
            try:
                guess_str = input(f'\nGuess a random integer between 1 and {difficulty} > ')
                guess = int(guess_str)

                if 0 < guess < difficulty + 1:
                    break
                else:
                    print(f'''\n{Fore.RED}This is not a valid guess.{Style.RESET_ALL}''')
            except:
                print(f'''\n{Fore.RED}{guess_str} is not a valid integer.{Style.RESET_ALL}''')

    return guess


def compare_results(secret_number, guess):
    return guess is secret_number


def play(difficulty):
    result = compare_results(generate_number(difficulty), get_guess_from_user(difficulty))
    print(f'''\n{Fore.CYAN}The secret number was {secret_number}{Style.RESET_ALL}''')
    return result
