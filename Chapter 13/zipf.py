"""
Exercise 13-9
"""

import string
import collections
import matplotlib.pyplot as plt


def read_file(filename, skip_header=True):
    """
    Makes a histogram that contains the words from a file.

	filename: string
	skip_header: boolean, default=True
   
	returns: map from each word to the number of times it appears.
	"""
    hist = collections.Counter()

    with open(filename, encoding="utf8") as fin:
        # skip the header
        if skip_header:
            skip_gutenberg_header(fin)
        # update
        for line in fin:
            hist.update(
                [word.strip(string.punctuation + string.whitespace).lower() for word in line.replace('-', ' ').split()])

    return hist


def skip_gutenberg_header(fp):
    """
    Reads from fp until it finds the line that ends the header.

	fp: open file object
	"""
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def freq_and_rank(hist):
    freq = list(hist.values())
    freq.sort(reverse=True)
    rank = 1
    for f in freq:
        yield rank, f
        rank += 1


def plot_ranks(hist, scale='log'):
    """
    Plots frequency vs. rank.

    hist: map from word to frequency
    scale: string 'linear' or 'log'
    """
    t = freq_and_rank(hist)
    rs, fs = zip(*t)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=3)
    plt.show()


def main():
    hist = read_file('../data/emma.txt')
    for rank, freq in freq_and_rank(hist):
        print(rank, freq)
    plot_ranks(hist)


if __name__ == '__main__':
    main()
