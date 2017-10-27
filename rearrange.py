import random
import sys

sys.argv.pop(0)
random.shuffle(sys.argv)
print(sys.argv)
