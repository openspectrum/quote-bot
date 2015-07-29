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

def sampleWord(source):
    import random
    index = random.randint(0, len(source) - 1)
    return source[index]

def buildSentence(length, sourceWords):
    sentence = []
    for i in range(length):
        sentence.append(sampleWord(sourceWords))
    return ' '.join(sentence) + '.'

def sentence(length, files):
    words = allWords(files)
    return buildSentence(length, words)

if __name__ == "__main__":
    import sys
    sentenceLength = sys.argv[1]
    files = sys.argv[2:len(sys.argv)]
    sent = sentence(int(sentenceLength), files)
    print(sent)
