# Generate a sentence of n length from a word source

import parts_of_speech

non_ending_words =  parts_of_speech.articles + parts_of_speech.prepositions + parts_of_speech.conjunctions
non_ending_punctuation = [',', ';', ':', '–', '-']

def sentence(length, next_chunk):
    chunk = next_chunk()
    sentence = list(chunk)
    limit = length - len(chunk)
    counter = 0
    while (counter <= limit):
        chunk = next_chunk()
        sentence.append(chunk[-1])
        if (counter == limit) and is_incomplete(sentence):
            limit += 1
        counter += 1

    sentence[0] = capitalize(sentence[0])
    return ' '.join(sentence) + '.'

def is_incomplete(sentence):
    return (sentence[-1] in non_ending_words) or (sentence[-1][-1] in non_ending_punctuation)

def capitalize(word):
    return word[0].upper() + word[1:len(word)]
