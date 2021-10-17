from os import system, name

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 1

def screen_cleaner():
    if name == 'nt':
        x = system('cls')
    else:
        x = system('clear')