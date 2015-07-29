# Generate a sentence of n length from a word source

from words import words
from probability import probabilities
from sample_word import sample_word

def sentence(length, words):
    sorted_probabilities = probabilities(words)
    sentence = []
    for i in range(length):
        sentence.append(sample_word(sorted_probabilities))
    sentence[0] = capitalize(sentence[0])
    return ' '.join(sentence) + '.'

def capitalize(word):
    return word[0].upper() + word[1:len(word)]

if __name__ == "__main__":
    import sys
    sentence_length = sys.argv[1]
    files = sys.argv[2:len(sys.argv)]
    words = words(files)
    sent = sentence(int(sentence_length), words)
    print(sent)
