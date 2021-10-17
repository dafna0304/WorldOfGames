from Live import welcome, load_game
from Utils import screen_cleaner

screen_cleaner()
welcome(input("Enter your name: "))


while True:
    load_game()
