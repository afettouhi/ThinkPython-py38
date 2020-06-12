def avoids(word, forbid_string):
    return set(forbid_string).isdisjoint(set(word))


# a combination of five forbidden letters that excludes the smallest number of words also means a combination
# contains the least amount of words
def avoids_count_modified(word):
    forbid_string = input("Please enter a forbidden string: ")
    return sum(avoids(word, forbid_string) for c in word)


print(avoids("Apple", "abcdA"))
