def read_seed():
    seed_words = []
    i = 0
    while True:
        i += 1
        w = input(f'Enter word #{i}: ')
        if not w:
            break
        seed_words.append(w)

    return seed_words
