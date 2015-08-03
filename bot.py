import sys
import pickle
from words import words
from sentence import *
from markov import *
from frequency import probabilities, make_word_walker

sentence_length = int(sys.argv[1])
algorithm_selection = sys.argv[2]
files = sys.argv[3:len(sys.argv)]
prefix_length = 2

if len(files) == 1 and files[0].split('.')[-1] == "pickle":
    source = pickle.load(open(files[0], "rb"))
    if algorithm_selection == 'markov':
        walker = make_prefix_walker(source)
    elif algorithm_selection == 'freq':
        walker = make_word_walker(source)
else:
    corpus = words(files)
    if algorithm_selection == 'markov':
        source = markov(corpus, prefix_length)
        walker = make_prefix_walker(source)
    elif algorithm_selection == 'freq':
        source = probabilities(corpus)
        walker = make_word_walker(source)

sent = sentence(sentence_length, walker)
print(sent)
