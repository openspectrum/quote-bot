import re

chars_to_strip = "\"()"

def words(files):
    words = []
    for f in files:
        words.extend(words_from_file(f))
    return words

def words_from_file(f):
    text = open(f, 'r').read()
    words = re.split('\s*', text)
    return [sanitize(w) for w in words]

def sanitize(word):
    return word.strip(chars_to_strip)

if __name__ == "__main__":
    import sys
    sentence_length = sys.argv[1]
    files = sys.argv[2:len(sys.argv)]
    words = words(files)
