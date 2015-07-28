# Generate a sentence of n length from a word source

def allWords(files):
    allWords = []
    for f in files:
        text = open(f, 'r').read()
        words = text.split()
        allWords.extend(words)
    return allWords

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
