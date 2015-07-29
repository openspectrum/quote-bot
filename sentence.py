# Generate a sentence of n length from a word source

from words import words
from probability import probabilities
from word_sequences import pairs
from sample_word import choose_next_word

def sentence(length, words):
    word_pairs = pairs(words)
    sorted_probabilities = probabilities(word_pairs)
    sentence = []
    prev_word = None
    for i in range(length):
        word = choose_next_word(prev_word, sorted_probabilities)
        sentence.append(word)
        prev_word = word

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
