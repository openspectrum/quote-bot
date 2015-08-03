# Generate a sentence of n length from a word source

from words import words
from markov import *
import parts_of_speech

non_ending_words =  parts_of_speech.articles + parts_of_speech.prepositions + parts_of_speech.conjunctions

def sentence(length, markov_dist):
    prefix = choose_next_prefix(markov_dist)
    sentence = list(prefix)
    limit = length - len(prefix)
    counter = 0
    while (counter <= limit):
        prefix = choose_next_prefix(markov_dist, prefix)
        sentence.append(prefix[-1])
        if (counter == limit) and (sentence[-1] in non_ending_words):
            limit += 1
        counter += 1

    sentence[0] = capitalize(sentence[0])
    return ' '.join(sentence) + '.'

def capitalize(word):
    return word[0].upper() + word[1:len(word)]

if __name__ == "__main__":
    import sys
    import pickle
    sentence_length = sys.argv[1]
    files = sys.argv[2:len(sys.argv)]
    prefix_length = 2

    if len(files) == 1 and files[0].split('.')[-1] == "pickle":
        markov_dist = pickle.load(open(files[0], "rb"))
    else:
        corpus = words(files)
        markov_dist = markov(corpus, prefix_length)

    for i in range(10):
        sent = sentence(int(sentence_length), markov_dist)
        print(sent)
