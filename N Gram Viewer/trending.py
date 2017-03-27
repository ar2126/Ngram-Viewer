"""
Finds the top 10 and bottom trending words based on a given start and end year
author: Aidan Rubenstein
"""
from wordData import *
import operator

class WordTrend(struct):
    _slots = ((str, 'word'), (float, 'trend'))

def trending(words, startYr, endYr):
    """
        Iterates through the words dictionary and finds the count value at or after the first instance of startYr and
        endYr and creates a WordTrend instance of the word and its trend. This instance is then put into a list
        precondition: dictionary of words, start year, and end year are given
        postcondition: list of WordTrend objects is returned

    """
    keys = words.keys()
    word = []
    for i in keys:
        top = 0
        bottom = 0
        for q in words[i]:
            if q.year == startYr and q.count >= 1000:
                top = q.count
            if q.year == endYr and q.count >= 1000:
                bottom = q.count
        if top != 0 and bottom != 0:
            word.append(WordTrend(i, top/bottom))
    word = sorted(word, key=operator.attrgetter('trend'))
    return word

def main():
    """
        Prints the top 10 and bottom 10 values in the word list retrieved from trending
    """
    user = input("Enter word file: ")
    startYr = int(input("Enter starting year: "))
    endYr = int(input("Enter ending year: "))
    word = trending(readWordFile(user), startYr, endYr)
    print("\nTop 10 words from ", startYr, " to ", endYr, ":")
    if len(word) >= 10:
        for i in range(10):
            print(word[i].word)
    else:
        for i in range(len(word)):
            print(word[i].word)
    print("\nBottom 10 words from ", startYr, " to ", endYr, ":")
    if len(word) >= 10:
        for i in range(len(word)-1, len(word)-11, -1):
            print(word[i].word)
    else:
        for i in range(len(word)-1, -1, -1):
            print(word[i].word)

if __name__ == '__main__':
    main()
