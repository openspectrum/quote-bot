# Generate a sentence of n length from a word source

from words import words
from probability import probabilities
from sample_word import sampleWord

def sentence(length, words):
    sortedProbabilities = probabilities(words)
    sentence = []
    for i in range(length):
        sentence.append(sampleWord(sortedProbabilities))
    return ' '.join(sentence) + '.'

if __name__ == "__main__":
    import sys
    sentenceLength = sys.argv[1]
    files = sys.argv[2:len(sys.argv)]
    words = words(files)
    sent = sentence(int(sentenceLength), words)
    print(sent)
