import random

def markov(words, prefix_size=2):
    distribution = {}
    prefix = tuple(words[0:prefix_size])
    for word in words[prefix_size:]:
        if prefix in distribution:
            distribution[prefix].append(word)
        else:
            distribution[prefix] = [word]
        prefix = prefix[1:] + (word,)
    return distribution

def make_prefix_walker(markov_dist):
    def prefix_walker(prefix=None):
        if prefix == None:
            prefix = random.choice(tuple(markov_dist.keys()))
        next_word = random.choice(markov_dist[prefix])
        return prefix[1:] + (next_word,)
    return prefix_walker

if __name__ == '__main__':
    import sys
    import pickle
    from words import words

    files = sys.argv[1:]
    corpus = words(files)
    dist = markov(corpus)
    pickle_file = "markov.pickle"
    pickle.dump(dist, open(pickle_file, "wb"))
    print("Markov distribution pickled to " + pickle_file + ".")
