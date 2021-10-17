from os import system, name


def clear():
    if name == 'nt':
        x = system('cls')
    else:
        x = system('clear')