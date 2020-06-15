import random
import string


def load_word_as_dict(filename):
    """
    Loads a file as a "memoized" dictionary mapping from word to frequency

    Return the dictionary
    """
    d = {}
    with open(filename, encoding='utf8') as fin:
        for line in fin:
            if not line.strip().startswith('#'):
                for word in line.split():
                    new_word = word.translate(
                        {ord(c): None for c in (string.punctuation + string.whitespace)}).lower().encode("utf-8")
                    if new_word not in d:
                        d[new_word] = 1
                    else:
                        d[new_word] += 1
    return d


def check_word_in_book(wordlist, book_wordlist):
    # l = []
    for word in book_wordlist.keys():
        if word not in wordlist.keys():
            print(word)


def choose_from_hist(hist):
    """
    Generate a hist list according to frequency
    then choose randomly one from the list

    WARN: this is low effiency
    """
    l = []
    for key, value in hist.items():
        l.extend([key] * value)  # word needs to be inside a list
    return random.choice(l)


if __name__ == '__main__':
    hist = load_word_as_dict('../data/words.txt')
    print(choose_from_hist(hist))
