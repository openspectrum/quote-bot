import sys
import pickle
from words import words
from sentence import *
from markov import *

sentence_length = sys.argv[1]
files = sys.argv[2:len(sys.argv)]
prefix_length = 2

if len(files) == 1 and files[0].split('.')[-1] == "pickle":
    markov_dist = pickle.load(open(files[0], "rb"))
else:
    corpus = words(files)
    markov_dist = markov(corpus, prefix_length)

prefix_walker = make_prefix_walker(markov_dist)

for i in range(10):
    sent = sentence(int(sentence_length), prefix_walker)
    print(sent)
