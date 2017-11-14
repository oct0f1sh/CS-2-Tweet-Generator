# import time
# import re
# import random
#
#
# class Dictogram(dict):
#     def __init__(self, corpus):
#         self.corpus = corpus
#         self.elapsed_time = None
#         # dict.__init__(self)
#         self = self.get_histogram(corpus)
#
#     def get_histogram(self, source_text):
#         '''Reads the source text and generates/returns the completed histogram'''
#         start_time = time.time()
#         f = open(source_text, 'r', encoding='utf-8')
#         words = f.read().lower().replace('\n', ' ')
#         words = re.sub('[^a-z]+', ' ', words)
#         words = words.split(' ')
#
#         unsorted_dictogram = Dictogram.check_word_in_histogram(words)
#
#         elapsed_time = time.time() - start_time
#
#         for sorted_item in sorted(unsorted_dictogram, key=lambda item: item[1]):
#             item_text = '\"{}\" appears {} times'.format(sorted_item[0], sorted_item[1])
#             self[sorted_item[0]] = sorted_item[1]
#
#         self.elapsed_time = '\nElapsed time: {} seconds'.format(elapsed_time)
#
#         f.close()
#
#         return self
#
#     @staticmethod
#     def check_word_in_histogram(words):
#         '''Checks if word is in histogram
#         if word is in histogram then it will increase the count by one
#         if word is not in histogram then it will add it and initialize count to 0
#         i don't really understand why this works but tony showed it to me'''
#         info_histogram = {}
#         tony_is_weird = info_histogram.get
#         for word in words:
#             info_histogram[word] = tony_is_weird(word, 0) + 1
#         return info_histogram


from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
