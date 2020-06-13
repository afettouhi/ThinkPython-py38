import bisect as bs


def get_dict():
    l = []
    fin = open("../data/words.txt")
    for line in fin:
        word = line.strip()
        l.append(word)
    d = dict.fromkeys(l)
    return d


def search_dict(d, s):
    if s in d:
        return True
    else:
        return False


def search_list(l, s):
    if s in l:
        return True
    else:
        return False


def make_word_list():
    """
    Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    word_list = []
    fin = open('../data/words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


# bisect is faster by about 0.032s, normal in using list is faster by 0.038

if __name__ == '__main__':
    d = get_dict()
    search_dict(d, "hey")
