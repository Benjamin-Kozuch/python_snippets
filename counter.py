from collections import Counter

letters = ['A','B','A','C','C']

frequency = Counter(letters).items()

print(frequency)