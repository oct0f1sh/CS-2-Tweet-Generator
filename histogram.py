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
    def __init__(self, corpus, write_to_file):
        self.histogram = {}
        self.initialize_file()
        self.write_to_file = write_to_file
        self.get_histogram(corpus)

    def get_histogram(self, source_text):
        '''Reads the source text and generates/returns the completed histogram'''
        start_time = time.time()
        f = open(source_text, 'r', encoding='utf-8')
        self.log_item('Histogram for {}:'.format(source_text))
        words = f.read().lower().replace('\n', ' ')
        words = re.sub('[^a-z]+', ' ', words)
        words = words.split(' ')

        self.check_word_in_histogram(words)

        elapsed_time = time.time() - start_time

        for sorted_item in sorted(self.histogram.items(), key=lambda item: item[1]):
            item_text = '\"{}\" appears {} times'.format(sorted_item[0], sorted_item[1])
            self.log_item(item_text)

        item_text = '\nElapsed time: {} seconds'.format(elapsed_time)
        self.log_item(item_text)

        f.close()

    def unique_words(self, histogram):
        '''Checks the length of the histogram and returns that number as the number of unique words'''
        length = len(histogram)
        item_text = '\nThere are {} unique words.\n'.format(length)
        self.log_item(item_text)
        return length

    def frequency(self, word):
        '''Searches the histogram for the given word and returns/logs the count'''
        word_info = self.histogram.get(word)

        if word_info is None:
            return

        item_text = '\"{}\" appears {} times.\n'.format(word, word_info)
        self.log_item(item_text)

        return word_info

    def check_word_in_histogram(self, words):
        '''Checks if word is in histogram
        if word is in histogram then it will increase the count by one
        if word is not in histogram then it will add it and initialize count to 0
        i don't really understand why this works but tony showed it to me'''
        info_histogram = {}
        tony_is_weird = info_histogram.get
        for word in words:
            info_histogram[word] = tony_is_weird(word, 0) + 1
        self.histogram = info_histogram

    def log_item(self, item):
        '''Writes item to log.txt'''
        print(item)
        if self.write_to_file:
            f = open('log.txt', 'a')
            f.write('\n{}'.format(item))
            f.close()

    def initialize_file(self):
        '''Clear previous log file'''
        f = open('log.txt', 'w')
        f.write('')
        f.close()


nice = CorpusHistogram('surgery.txt', True)
nice.unique_words(nice.histogram)
nice.frequency('fig')
