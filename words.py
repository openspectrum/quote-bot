def words(files):
    words = []
    for f in files:
        words.extend(words_from_file(f))
    return words

def words_from_file(f):
    import re

    text = open(f, 'r').read()
    words = re.split('\W+', text)
    return [sanitize(w) for w in words]

def sanitize(word):
    return word.lower()

if __name__ == "__main__":
    import sys
    sentence_length = sys.argv[1]
    files = sys.argv[2:len(sys.argv)]
    words = words(files)
