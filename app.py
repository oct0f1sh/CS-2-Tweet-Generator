from flask import Flask, request
from flask_restful import Resource, Api
from markov_chain import MarkovChain
import re


app = Flask(__name__)
api = Api(app)


class Tweet(Resource):
    def get(self):
        if request.args['num'] is not None:
            num_of_words = int(request.args['num'])
        else:
            num_of_words = 20
        chain = MarkovChain('surgery.txt')
        sentence = []

        sentence.append(chain.generate_random_sentence(num_of_words - 1))

        return ' '.join(sentence)


api.add_resource(Tweet, '/')

if __name__ == '__main__':
    app.run(debug=True)
