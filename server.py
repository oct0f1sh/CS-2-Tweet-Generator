from flask import Flask
from histogram import CorpusHistogram
app = Flask(__name__)


@app.route('/')
def nice():
    neat = CorpusHistogram('surgery.txt', False)
    sentence = ''
    for _ in range(0, 25):
        word = neat.get_random_weighted_word() + ' '
        sentence += word
    return sentence


if __name__ == '__main__':
    app.run(debug=True)