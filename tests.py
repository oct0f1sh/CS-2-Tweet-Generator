from histogram import CorpusHistogram

nice = CorpusHistogram('short_text.txt', False)

results = {'one': 0,
           'two': 0,
           'red': 0,
           'blue': 0,
           'fish': 0
           }

for _ in range(0, 100):
    word = nice.get_random_weighted_word()

    if word == 'one':
        results['one'] += 1
    elif word == 'two':
        results['two'] += 1
    elif word == 'red':
        results['red'] += 1
    elif word == 'blue':
        results['blue'] += 1
    else:
        results['fish'] += 1

print(results)
