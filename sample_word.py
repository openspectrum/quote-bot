def sampleWord(sortedProbabilities):
    import random
    limit = sortedProbabilities[-1][0]
    choice = round(random.uniform(0, limit), 6)
    for freq, word in sortedProbabilities:
        if choice < freq:
            return word
