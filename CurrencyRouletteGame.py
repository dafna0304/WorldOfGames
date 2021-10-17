from currency_converter import CurrencyConverter
from random import randint
from colorama import Fore, Back, Style, init

total_usd = int

def get_money_interval(difficulty, total_usd):
    converter = CurrencyConverter()
    total = int(round(converter.convert(1, 'USD', 'ILS'), 2)) * total_usd
    return total - (5 - difficulty), total + (5 - difficulty)


def get_guess_from_user(total_usd):
    guess_str: str
    guess: int

    valid_integer = False
    while not valid_integer:
        try:
            guess_str = input(f'\nEnter an integer as a guess for how much shekels are worth {total_usd}$ > ')
            guess = int(guess_str)
            valid_integer = True
        except:
            print(f'''{Fore.RED}\nInvalid integer.{Style.RESET_ALL}''')

    return guess


def play(difficulty):
    pick_usd = randint(1, 100)
    interval = get_money_interval(difficulty, pick_usd)
    guess = get_guess_from_user(pick_usd)

    return interval[0] < guess < interval[1]
