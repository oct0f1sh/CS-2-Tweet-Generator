from flask import Flask, request
from flask_restful import Resource, Api
from markov_chain import MarkovChain
import re


app = Flask(__name__)
api = Api(app)


def split_text_file(corpus):
    f = open(corpus, 'r', encoding='utf-8')
    words = f.read().lower().replace('\n', ' ')
    words = re.sub('[^a-z]+', ' ', words)
    words = words.split(' ')
    return words


class Tweet(Resource):
    def get(self):
        if request.args['num'] is not None:
            num_of_words = int(request.args['num'])
        else:
            num_of_words = 20
        chain = MarkovChain(split_text_file('surgery.txt'))
        sentence = []

        sentence.append(chain.generate_random_sentence(num_of_words - 1))

        return ' '.join(sentence)


api.add_resource(Tweet, '/')

if __name__ == '__main__':
    app.run(debug=True)
