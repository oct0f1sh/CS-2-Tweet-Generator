from flask import Flask, request
from flask_restful import Resource, Api
from histogram import CorpusHistogram


app = Flask(__name__)
api = Api(app)


class Tweet(Resource):
    def get(self):
        num_of_words = 20
        if request.args['num'] is not None:
            num_of_words = int(request.args['num'])
        histogram = CorpusHistogram('surgery.txt', False)
        sentence = ''

        for _ in range(0, num_of_words):
            word = histogram.get_random_weighted_word() + ' '
            sentence += word

        return sentence


api.add_resource(Tweet, '/')

if __name__ == '__main__':
    app.run(debug=True)
