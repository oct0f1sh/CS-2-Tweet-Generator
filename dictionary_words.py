import random
import sys


def dictionary_words(num_of_words):
    words = []
    f = open('/usr/share/dict/words', 'r', encoding='utf-8')

    for line in f:
        words.append(line)

    for _ in range(0, num_of_words):
        randy = random.randint(0, len(words))
        random_word = words[randy]
        # takes the newline off the end of each word
        print(random_word[0:-1])

    f.close()


dictionary_words(int(sys.argv[1]))
