from listogram import Listogram
import random
import re

class MarkovChain(list):
    def __init__(self, corpus):
        super(MarkovChain, self).__init__()
        self.types = 0
        self.tokens = 0
        self.words = []

        if corpus is not None:
            for index in range(len(corpus) - 1):
                if index != len(corpus) - 1:
                    self.add_count(corpus[index], corpus[index + 1])
            self.generate_markov_chain()

    def add_count(self, word_1, word_2):
        self.tokens += 1

        if len(self.words) == 0:
            self.words.append([word_1, [word_2]])
            self.types += 1
            return

        for word in self.words:
            if word[0] == word_1:
                word[1].append(word_2)
                return

        self.words.append([word_1, [word_2]])
        self.types += 1

    def generate_markov_chain(self):
        for item in self.words:
            listogram = Listogram(item[1])
            self.append([item[0], listogram])

    def generate_random_sentence(self, length):
        randy = random.randint(0, len(self) - 1)
        sentence = [self[randy][0]]
        for _ in range(length):
            sentence.append(self.get_next_word(sentence[-1]))
        return ' '.join(sentence)

    def get_next_word(self, word):
        for word_info in self:
            if word == word_info[0]:
                randy = random.randint(0, len(word_info[1]) - 1)
                iterator = 0
                for word in word_info[1]:
                    if randy <= iterator:
                        return word[0]
                    else:
                        iterator += word[1]

def split_text_file(corpus):
    f = open(corpus, 'r', encoding='utf-8')
    words = f.read().lower().replace('\n', ' ')
    words = re.sub('[^a-z]+', ' ', words)
    words = words.split(' ')
    return words

if __name__ == '__main__':
    chain = MarkovChain(split_text_file('surgery.txt'))
    for _ in range(10):
        for i in range(5, 10):
            print(chain.generate_random_sentence(i))
