from collections import Counter
letters = ['a','b','a','c','c']
freq = Counter(letters).items()
print(freq)
#freq-->dict_items([('a', 2), ('b', 1), ('c', 2)]) list of tuples


# sort by most frequent
most_freq = sorted(freq, key=lambda x: x[1])
print(most_freq)
#most_freq-->[('b', 1), ('a', 2), ('c', 2)]


#sort in descending order
most_freq = sorted(most_freq, key=lambda x: x[1], reverse=True)
print(most_freq)
#most_freq-->[('a', 2), ('c', 2), ('b', 1)]

# sort my most frequent first and if multiple letters have the same freq, 
# then the later in the alpabet should come first
most_freq = sorted(most_freq, key=lambda x: (x[1], x[0]), reverse=True)
print(most_freq)
#most_freq-->[('c', 2), ('a', 2), ('b', 1)]



# sort my most frequent first and if multiple letters have the same freq, 
# then the later in the alpabet should come last
most_freq = sorted( 
    sorted(
        most_freq, 
        key=lambda x: x[0]), 
    key=lambda x:  x[1], 
    reverse=True)
print(most_freq)
#most_freq-->[('a', 2), ('c', 2), ('b', 1)]

