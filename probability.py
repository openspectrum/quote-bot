def probabilities(words):
    freq_dist = word_count(words)
    probabilities = []
    prob = 0
    for word, freq in freq_dist.items():
        prob = round(prob + probability(word, freq_dist), 6)
        probabilities.append((prob, word))
    return sorted(probabilities)

def probability(word, freq_dist):
    numWords = 0
    for _, freq in freq_dist.items():
        numWords += freq
    return round(freq_dist[word] / numWords, 6)

def word_count(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts
