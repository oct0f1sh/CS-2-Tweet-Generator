from dictogram import Dictogram
import random
import re


class MarkovChain(dict):
    def __init__(self, corpus):
        if type(corpus) is str:
            corpus = self.open_file(corpus)
        super(MarkovChain, self).__init__()
        self.types = 0
        self.tokens = 0

        if corpus is not None:
            for index in range(len(corpus) - 1):
                if index != len(corpus) - 1:
                    self.add_count(corpus[index], corpus[index + 1])

    def add_count(self, word_1, word_2):
        self.tokens += 1

        if len(self) == 0:
            self[word_1] = Dictogram([word_2])
            self.types += 1
            return

        if word_1 in self:
            self[word_1].add_count(word_2)
            # self[self.index(word_1)][1].add_count(word_2)
            return

        self[word_1] = Dictogram([word_2])
        self.types += 1

    def generate_random_sentence(self, length):
        randy = random.randint(0, len(self) - 1)
        sentence = ['the']
        for _ in range(length):
            sentence.append(self.get_next_word(sentence[-1]))
        return ' '.join(sentence)

    def get_next_word(self, word):
        if word in self.keys():
            dictogram = self.get(word)
            randy = random.randint(0, len(dictogram) - 1)
            iterator = 0
            for key, value in dictogram.items():
                if randy <= iterator:
                    return key
                else:
                    iterator += value

    @staticmethod
    def open_file(corpus):
        f = open(corpus, 'r', encoding='utf-8')
        words = f.read().lower().replace('\n', ' ')
        words = re.sub('[^a-z]+', ' ', words)
        words = words.split(' ')
        return words


if __name__ == '__main__':
    chain = MarkovChain('surgery.txt')
    for _ in range(10):
        for i in range(5, 10):
            print(chain.generate_random_sentence(i))