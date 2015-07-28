# Generate a sentence of n length from a word source

def allWords(files):
    allWords = []
    for f in files:
        text = open(f, 'r').read()
        words = text.split()
        allWords.extend(words)
    return allWords


if __name__ == "__main__":
    import sys
    files = sys.argv[1:len(sys.argv)]
    print(allWords(files))
