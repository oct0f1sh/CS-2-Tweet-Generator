'''
A histogram() function which takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) and
return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.

A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram.
For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.

A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text.
For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
'''
import time
import re


class CorpusHistogram:
    def __init__(self, corpus):
        self.histogram = {}
        self.get_histogram(corpus)

    def get_histogram(self, source_text):
        start_time = time.time()
        f = open(source_text, 'r', encoding='utf-8')
        print('Generating histogram for {}...'.format(source_text))
        words = f.read().lower().replace('\n', ' ')
        words = re.sub('[^a-z]+', ' ', words)
        words = words.split(' ')

        self.check_word_in_histogram(words)

        elapsed_time = time.time() - start_time

        for sorted_item in sorted(self.histogram.items(), key=lambda item: item[1]):
            print('\"{}\" appears {} times'.format(sorted_item[0], sorted_item[1]))

        print('\nElapsed time: {} seconds'.format(elapsed_time))
        f.close()

    def unique_words(self, histogram):
        length = len(histogram)
        print('\nThere are {} unique words.\n'.format(length))
        return length

    def frequency(self, word):
        word_info = self.histogram.get(word)

        if word_info is None:
            return

        print('\"{}\" appears {} times.\n'.format(word, word_info))

        return word_info

    def check_word_in_histogram(self, words):
        info_histogram = {}
        tony_is_weird = info_histogram.get
        for word in words:
            info_histogram[word] = tony_is_weird(word, 0) + 1
        self.histogram = info_histogram


nice = CorpusHistogram('surgery.txt')
nice.unique_words(nice.histogram)
nice.frequency('fig')
