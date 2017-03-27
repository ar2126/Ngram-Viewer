"""
    Computes the relative frequency of English characters occurring in print
    author: Aidan Rubenstein
"""
from wordData import *
import operator

def letterFreq(words):
    """
        Creates a dictionary of every lowercase character, goes through the words dictionary and adds a value to
        each letter that appears. Dictionary is then sorted and a running string is then created and concatenated

        precondition: dictionary from wordData is passed
        postcondition: string containing the sorted lexicon is returned
    """
    word = ''
    wordDict = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for a in alpha:
        wordDict[a] = 0
    keys = words.keys()
    for i in keys:
        count = totalOccurrences(i, words)
        for b in i:
            wordDict[b] += count
    final = sorted(wordDict.items(), key=operator.itemgetter(1))
    for k, v in final:
        word += k
    return word[::-1]

def main():
    user = input("Enter word file: ")
    print("Letters sorted by decreasing frequency: ", letterFreq(readWordFile(user)))

if __name__ == '__main__':
    main()