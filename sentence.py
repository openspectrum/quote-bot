# Generate a sentence of n length from a word source

from words import words
from markov import *

def sentence(length, corpus):
    prefix_length = 2
    markov_dist = markov(corpus, prefix_length)
    prefix = choose_next_prefix(markov_dist)
    sentence = list(prefix)
    for i in range(length - prefix_length):
        prefix = choose_next_prefix(markov_dist, prefix)
        sentence.append(prefix[-1])

    sentence[0] = capitalize(sentence[0])
    return ' '.join(sentence) + '.'

def capitalize(word):
    return word[0].upper() + word[1:len(word)]

if __name__ == "__main__":
    import sys
    sentence_length = sys.argv[1]
    files = sys.argv[2:len(sys.argv)]
    corpus = words(files)
    sent = sentence(int(sentence_length), corpus)
    print(sent)
