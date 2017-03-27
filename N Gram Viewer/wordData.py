"""
    Takes a filename and creates a dictionary based on the year and how many times said word occurred
    author: Aidan Rubensitein
"""
from rit_lib import *


class YearCount(struct):
    _slots = ((int, 'year'), (int, 'count'))

class WordTrend(struct):
    _slots = ((str, 'word'), (float, 'trend'))

def readWordFile(fileName):
    """
    Reads a text file and fills the dictionary with key-YearCount pairs
    pre-condition: fileName is passed
    post-condition: dictionary dict is filled and returned
    """
    fileName = 'data/' + fileName
    dict = {}
    for i in open(fileName):
        i = i.strip()
        list = i.split(',')
        if len(list) == 1:
            word = list[0]
            values = []
        if len(list) != 1:
            dates = i.split(',')
            values.append(YearCount(int(dates[0]), int(dates[1])))
            dict[word] = values
    return dict


def totalOccurrences(word, words):
    """
    Checks to see if a word exists, and gives the total count for that word
    pre-condition: word is given by user and dictionary words is passed
    post-condition: int count is printed to the user
    """
    count = 0
    if word in words:
        value = words.get(word)
        for i in range(len(value)):
            count += value[i].count
        return count
    else:
        return count


def main():
    yes = input("Enter word file: ")
    word = input("Find word: ")
    print("Total occurences of ", word, ": ", totalOccurrences(word, readWordFile(yes)))


if __name__ == '__main__':
    main()
