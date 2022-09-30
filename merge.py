from f import read_seed

with open('wordlist.txt') as f:
    wordlist = f.read().split()

assert len(wordlist) == 2048

print('Enter words of your seed A one by one:')
seed1_words = read_seed()

print('Enter words of your seed B one by one:')
seed2_words = read_seed()

assert len(seed1_words) == len(seed2_words)

seed_words = []

for i, (w1, w2) in enumerate(zip(seed1_words, seed2_words)):
    seed1_num = wordlist.index(w1)
    seed2_num = wordlist.index(w2)
    seed_num = seed1_num ^ seed2_num
    seed_word = wordlist[seed_num]
    seed_words.append(seed_word)

print('\nSeed:')
for i, w in enumerate(seed_words):
    print(f'#{i}: {w}')

