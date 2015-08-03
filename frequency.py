import random

decimal_limit = 6

def probabilities(words):
    freq_dist = frequencies(words)
    probabilities = []
    prob = 0
    for word, freq in freq_dist.items():
        prob = round(prob + probability(word, freq_dist), decimal_limit)
        probabilities.append((prob, word))
    return sorted(probabilities)

def probability(word, freq_dist):
    numWords = 0
    for _, freq in freq_dist.items():
        numWords += freq
    return round(freq_dist[word] / numWords, decimal_limit)

def frequencies(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts

def make_word_walker(sorted_probabilities):
    history = []
    limit = sorted_probabilities[-1][0]

    def word_walker():
        choice = round(random.uniform(0, limit), decimal_limit)
        for freq, word in sorted_probabilities:
            if choice < freq:
                history.append(word)
                return (word,)
    return word_walker

if __name__ == '__main__':
    import sys
    import pickle
    from words import words

    files = sys.argv[1:]
    corpus = words(files)
    dist = probabilities(corpus)
    pickle_file = "freq.pickle"
    pickle.dump(dist, open(pickle_file, "wb"))
    print("Probability distribution pickled to " + pickle_file + ".")
