"""
    Prompts the user for a data file and a year to search. The result returns 5 data points from the indicated year
    and creates a box and whisker plot
    author: Aidan Rubenstein
"""
from wordData import *
from boxAndWhisker import *
import operator

def summaryFromWords(words, year):
    """
        Takes a dictionary of YearCount objects and the indicated year, searches for the year and creates a sorted
        list of the year and count values from the dictionary. The 5 values are found and returned with the help of
        helper functions
        precondition: dictionary with YearCount objects and user-generated year are passed
        postcondition: tuple containing 5 values to make a box and whisker are returned
    """
    dict = {}
    for i in words:
        for q in words[i]:
            if q.year == year:
                if len(i) not in dict.keys():
                    dict[len(i)] = q.count
                else:
                    dict[len(i)] += q.count
    sort = sorted(dict.items(), key = operator.itemgetter(0))
    print(sort)
    count = 0
    temp = []
    for k,l in sort:
        count += 1
        temp.append(k)
    ind = count//2
    med = getMedian(ind, sort)
    ind1 = ind//2
    q1 = getQ1(ind1, sort)
    ind2 = ind + ind1
    q3 = getQ3(ind2, sort)
    large = temp[-1]
    small = temp[0]
    return small, q1, med, q3, large

def getMedian(index, list):
    """
        Gets the value of med by searching through list
        precondition: index to compare and the list of indices and counts is passed
        postcondition: value of med is returned
    """
    count = 0
    for k, l in list:
        count += l
        if count < index:
            continue
        else:
            med = k
            break
    return med

def getQ1(index, list):
    """
        Gets the value of q1 by searching through list
        precondition: index to compare and the list of indices and counts is passed
        postcondition: value of q1 is returned
    """
    count = 0
    for k, l in list:
        count += l
        if count < index:
            continue
        else:
            q1 = k
            break
    return q1

def getQ3(index, list):
    """
        Gets the value of q3 by searching through list
        precondition: index to compare and the list of indices and counts is passed
        postcondition: value of q3 is returned
    """
    count = 0
    for k, l in list:
        count += l
        if count < index:
            continue
        else:
            q3 = k
            break
    return q3

def main():
    user = input("Enter word file: ")
    year = int(input("Enter year: "))
    a, b, c, d, e = summaryFromWords(readWordFile(user), year)
    print("minimum: ", a)
    print("1st quartile: ", b)
    print("median: ", c)
    print("3rd quartile: ", d)
    print("maximum: ", e)
    boxAndWhisker(a, b, c, d, e)

if __name__ == '__main__':
    main()