# Generate a quote of n length from a word source

import parts_of_speech

non_ending_words =  parts_of_speech.articles + parts_of_speech.prepositions + parts_of_speech.conjunctions
non_ending_punctuation = [',', ';', ':', '–', '-']

def quote(length, next_chunk):
    chunk = next_chunk()
    quote = list(chunk)
    limit = length - len(chunk)
    counter = 0
    while (counter <= limit):
        chunk = next_chunk()
        quote.append(chunk[-1])
        if (counter == limit) and is_incomplete(quote):
            limit += 1
        counter += 1

    quote[0] = capitalize(quote[0])
    return ' '.join(quote) + '.'

def is_incomplete(quote):
    return (quote[-1] in non_ending_words) or (quote[-1][-1] in non_ending_punctuation)

def capitalize(word):
    return word[0].upper() + word[1:len(word)]
