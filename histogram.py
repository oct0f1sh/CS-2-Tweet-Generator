'''
A histogram() function which takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) and
return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.

A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram.
For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.

A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text.
For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
'''


class CorpusHistogram:
    def __init__(self, corpus):
        self.histogram = []
        self.get_histogram(corpus)

    def get_histogram(self, source_text):
        f = open(source_text, 'r', encoding='utf-8')
        print('Generating histogram for {}...'.format(source_text))
        for line in f:
            words = line.replace('-', ' ').replace('#', '').replace('_', '').split(' ')
            for word in words:
                plain_word = self.remove_punctuation(word)
                self.check_word_in_histogram(plain_word)
        self.histogram = sorted(self.histogram, key=lambda k: k.get('count'), reverse=False)
        for word in self.histogram:
            if word.get('count') == 1:
                print('\"{}\" appears 1 time'.format(word.get('word')))
            else:
                print('\"{}\" appears {} times'.format(word.get('word'), word.get('count')))

    def unique_words(self):
        pass

    def frequency(self):
        pass

    def remove_punctuation(self, word):
        """
        remove_punctuation iterates through every char in 'word' and checks if it the ASCII value is in range of
        lowercase letters. Returns lowercase word with only letters.
        """
        word = list(word.lower().rstrip('\n'))
        for char in word:
            if ord(char) <= 122 and ord(char) >= 97:
                continue
            else:
                word.remove(char)
        return ''.join(word)

    def check_word_in_histogram(self, word):
        for histogram_word in self.histogram:
            if word == histogram_word.get('word'):
                histogram_word['count'] += 1
                return
        self.histogram.append({'word': word, 'count': 1})
        return


nice = CorpusHistogram('surgery.txt')
