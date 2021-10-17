from Score import add_score
from flask import Flask

app = Flask(__name__)
@app.route("/")
def score_server():
    try:
        scores_file = open('Scores.txt', 'r')
        the_score = scores_file.read()
        scores_file.close()
        html_text = f'<html><head><title>Scores Game</title></head><body><h1>The score is:<div id=\'the_score\'>{the_score}</div></h1></body></html>'

    except:
        html_text = f'<html><head><title>Scores Game</title></head><body><body><h1><div id=\'score\' style=\'color:red\'>ERROR</div></h1></body></html>'

    return (html_text)


app.run()
