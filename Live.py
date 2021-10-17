from colorama import Fore, Back, Style, init
from time import sleep
import MemoryGame
import GuessGame
import CurrencyRouletteGame
import MainScores
from MainScores import score_server
from Utils import screen_cleaner
from Score import add_score

init()

MIN_DIFFICULTY = 1
MAX_DIFFICULTY = 5


def welcome(name):
    screen_cleaner()
    print(f'{Style.BRIGHT}{Fore.CYAN}Hello {Fore.YELLOW}{name}{Fore.CYAN} and welcome to World of Games.')
    print('Here you can find many cool games to play.')


def load_game():
    print(f'''{Fore.GREEN}\nPlease choose a game to play: {Style.RESET_ALL}
    1. Memory Game - A sequence of numbers will appear for 1 second and you have to guess the sequence back
    2. Guess Game - Guess a number and see if your machine generated the same number
    3. Currency Roulette - Try and guess the value of a random amount of USD in ILS
    4. Check your scores
    5. Exit''')
    game = int
    game_str = ''
    while game_str != '5':
        game_str = input('\nPick your game > ')
        if game_str == '4':
            exec(open("MainScores.py").read())
            break
        if game_str == '5':
            break

        try:
            game = int(game_str)
        except:
            print(f'''{Fore.RED}\nPlease pick a valid game.{Style.RESET_ALL}''')
            continue

        if 0 < game < 5:
            break
        else:
            print(f'''\n{Fore.RED}Please pick a valid game.{Style.RESET_ALL}''')

    while game_str != '4' and game_str != '5':
        difficulty_str = input(f'\nPick a difficulty from {MIN_DIFFICULTY} to {MAX_DIFFICULTY} > ')
        difficulty: int

        try:
            difficulty = int(difficulty_str)
        except:
            print(f'''\n{Fore.RED}Please pick a valid difficulty.{Style.RESET_ALL}''')
            continue

        if MIN_DIFFICULTY <= difficulty <= MAX_DIFFICULTY:
            break
        else:
            print(f'''\n{Fore.RED}Please pick a valid difficulty.{Style.RESET_ALL}''')

    if game_str != '4' and game_str != '5':
        print(
            f'\n{Back.GREEN}{Fore.BLACK}You selected game #{game} and difficulty level {difficulty}.{Style.RESET_ALL}')
        sleep(2.0)
        load(game, difficulty)
    else:
        if game_str == '5':
            print(f'\n{Back.GREEN}{Fore.BLACK}~ Bye bye ~{Style.RESET_ALL}')
            exit(0)


def load(game, difficulty):
    games = {
        1: MemoryGame.play,
        2: GuessGame.play,
        3: CurrencyRouletteGame.play
    }

    win = games.get(game, 'Invalid game.')(difficulty)
    if win:
        print(f'''\n{Fore.GREEN}You won!{Style.RESET_ALL}''')
        add_score(difficulty)
    else:
        print(f'''\n{Fore.RED}You lost.{Style.RESET_ALL}''')
