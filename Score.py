from os import path
from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    # if Scores.txt does not exist create it
    if not path.isfile(SCORES_FILE_NAME):
        scores_file = open(SCORES_FILE_NAME, 'w+')
        scores_file.write('0')
        scores_file.close()

    points_of_winning: int
    with open(SCORES_FILE_NAME) as scores_file:
        points_of_winning = int(scores_file.read())
        scores_file.close()

    if difficulty == 0:
        return points_of_winning

    points_of_winning += difficulty * 3 + 5
    with open(SCORES_FILE_NAME, 'w') as scores_file:
        scores_file.write(str(points_of_winning))
        scores_file.close()

    # return points_of_winning
    return
