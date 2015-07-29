def pairs(words):
    pairs = []
    first_word = words[0]
    for second_word in words[1:len(words)]:
        pairs.append((first_word, second_word))
        first_word = second_word
    return pairs

if __name__ == "__main__":
    import sys
    words = sys.argv[1:len(sys.argv)]
    print(pairs(words))
