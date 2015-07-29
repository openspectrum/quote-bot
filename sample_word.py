import random

def sample_word(sorted_probabilities):
    limit = sorted_probabilities[-1][0]
    choice = round(random.uniform(0, limit), 6)
    for freq, word in sorted_probabilities:
        if choice < freq:
            return word

def choose_next_word(prev_word, probabilities_word_pairs):
    if prev_word == None:
        return random.choice(first_words(probabilities_word_pairs))
    options = [ (freq, word_pair[1])
                for freq, word_pair in probabilities_word_pairs
                if prev_word == word_pair[0] ]
    return random.choice(options)[1]

def first_words(sorted_probabilities):
    return [freq_pair[1][0] for freq_pair in sorted_probabilities]
