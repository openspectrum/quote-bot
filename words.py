def words(files):
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

if __name__ == "__main__":
    import sys
    sentenceLength = sys.argv[1]
    files = sys.argv[2:len(sys.argv)]
    words = words(files)
