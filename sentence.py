# Generate a sentence of n length from a word source

def allWords(files):
    words = []
    for f in files:
        words.extend(wordsFromFile(f))
    return words

def wordsFromFile(f):
    import re

    text = open(f, 'r').read()
    words = re.split('\W+', text)
    return [sanitize(w) for w in words]

def sanitize(word):
    return word.lower()

def wordCount(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts

def sampleWord(sortedProbabilities):
    import random
    limit = sortedProbabilities[-1][0]
    choice = round(random.uniform(0, limit), 6)
    for freq, word in sortedProbabilities:
        if choice < freq:
            return word

def probability(word, freqDist):
    numWords = 0
    for _, freq in freqDist.items():
        numWords += freq
    return round(freqDist[word] / numWords, 6)

def probabilities(freqDist):
    probabilities = []
    prob = 0
    for word, freq in freqDist.items():
        prob = round(prob + probability(word, freqDist), 6)
        probabilities.append((prob, word))
    return sorted(probabilities)

def sentence(length, words):
    freqDist = wordCount(words)
    sortedProbabilities = probabilities(freqDist)
    sentence = []
    for i in range(length):
        sentence.append(sampleWord(sortedProbabilities))
    return ' '.join(sentence) + '.'

if __name__ == "__main__":
    import sys
    sentenceLength = sys.argv[1]
    files = sys.argv[2:len(sys.argv)]
    words = allWords(files)
    sent = sentence(int(sentenceLength), words)
    print(sent)
