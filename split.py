import secrets

from f import read_seed

with open('wordlist.txt') as f:
    wordlist = f.read().split()

assert len(wordlist) == 2048

print('Enter your seed words one by one.')
seed_words = read_seed()

seed1_words = []
seed2_words = []

for w in seed_words:
    seed_num = wordlist.index(w)

    seed1_num = secrets.randbelow(len(wordlist))
    seed1_word = wordlist[seed1_num]
    seed1_words.append(seed1_word)

    seed2_num = seed_num ^ seed1_num
    seed2_word = wordlist[seed2_num]
    seed2_words.append(seed2_word)

print('Seed A:')
for i, w in enumerate(seed1_words):
    print(f'#{i+1}: {w}')

print('\nSeed B:')
for i, w in enumerate(seed2_words):
    print(f'#{i+1}: {w}')
