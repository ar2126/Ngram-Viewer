"""
    Prompts user for a text file, and creates a list of YearCount objects for each year and the total count of words.
    User enters a year to search for, shows the total occurrences of words for that year and traces a graph
    author: Aidan Rubenstein
"""
from wordData import *
import simplePlot
import operator

def printedWords(words):
    """
        Creates a list containing the total occurrences of words for each year in the form of a YearCount object
        precondition: a dictionary of words is passed in
        postcondition: list containing cumulative YearCount objects is returned
    """
    list = []
    final = []
    dict = {}
    keys = words.keys()
    for i in keys:
        t = words.get(i)
        for temp in range(len(t)):
            list.append(t[temp])
    for q in range(len(list)):
        count = 0
        search = list[q].year
        for d in range(len(list)):
            if search == list[d].year:
                count += list[d].count
        dict[search] = count
    for z in dict:
        final.append(YearCount(z, dict[z]))
    final = sorted(final, key=operator.attrgetter('year'))
    return final

def wordsForYear(year, yearList):
    """
        Searches for the total occurences in a year as given by the user
        precondition: a desired year and the list of years is passed in
        postcondition: int of count is returned if the year exists, or 0 if the year does not exist
    """
    count = 0
    for i in range(len(yearList)):
        if int(yearList[i].year) == year:
            count += yearList[i].count
        else:
            count += 0
    return count


def main():
    """
        Promts user for text file name and desired year and creates a graph of the word trends
    """
    user = input("Enter word file: ")
    desire = int(input("Enter year: "))
    years = printedWords(readWordFile(user))
    print("Total printed words in ", desire, ": ", wordsForYear(desire, years))
    labels = "Year", "Total Words"
    plot = simplePlot.plot2D('Number of printed words over time', labels)
    for yc in years:
        point = yc.year, yc.count
        plot.addPoint(point)
    plot.display()

if __name__ == '__main__':
    main()