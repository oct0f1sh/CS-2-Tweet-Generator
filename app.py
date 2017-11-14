from flask import Flask, request
from flask_restful import Resource, Api
from markov_chain import MarkovChain


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
        num_of_words = 20
        if request.args['num'] is not None:
            num_of_words = int(request.args['num'])
        histogram = MarkovChain(split_text_file('surgery.txt'))
        sentence = []

        for _ in range(0, num_of_words):
            sentence.append(histogram.get_random_weighted_word())

        return ' '.join(sentence)


api.add_resource(Tweet, '/')

if __name__ == '__main__':
    app.run(debug=True)
