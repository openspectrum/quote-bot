def sample_word(sorted_probabilities):
    import random
    limit = sorted_probabilities[-1][0]
    choice = round(random.uniform(0, limit), 6)
    for freq, word in sorted_probabilities:
        if choice < freq:
            return word
