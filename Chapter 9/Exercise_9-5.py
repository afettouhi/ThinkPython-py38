def uses_all(word, letters):
    required = letters.split()
    for letter in required:
        if letter not in word:
            return False
    return True


fin = open('../data/words.txt')
count1 = 0

for line in fin:
    word1 = line.strip()
    if uses_all(word1, 'a e i o u'):
        print(word1)
        count1 += 1
print(count1)

fin = open('../data/words.txt')
count2 = 0

for line in fin:
    word2 = line.strip()
    if uses_all(word2, 'a e i o u y'):
        print(word2)
        count2 += 1
print(count2)
