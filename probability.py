def probabilities(words):
    freqDist = wordCount(words)
    probabilities = []
    prob = 0
    for word, freq in freqDist.items():
        prob = round(prob + probability(word, freqDist), 6)
        probabilities.append((prob, word))
    return sorted(probabilities)

def probability(word, freqDist):
    numWords = 0
    for _, freq in freqDist.items():
        numWords += freq
    return round(freqDist[word] / numWords, 6)

def wordCount(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts
