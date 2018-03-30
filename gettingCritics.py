import string
import re
import urllib2
from bs4 import BeautifulSoup
import csv
import os

dirname = os.path.dirname(os.path.abspath(__file__))
csvfilename = os.path.join(dirname, 'CriticsList.csv')

CRITICS = []

alphabet_array = []

def make_alphabet():
    for c in string.ascii_lowercase:
        alphabet_array.append(c)

make_alphabet()

def get_authors_for_letter(letter):
    reviewer_list_baseurl = "https://www.rottentomatoes.com/critics/authors/?letter=" + letter

    # for letter in alphabet_array:
    #     reviewer_list_one_letter = reviewer_list_baseurl + letter
    #     page = urllib2.urlopen(reviewer_list_one_letter)
    #     soup = BeautifulSoup(page, 'html.parser')
    #     print soup

    page = urllib2.urlopen(reviewer_list_baseurl)
    soup = BeautifulSoup(page, 'html.parser')

    for idee in soup.findAll(attrs={'class':'critic-names'}):
        criticIso = ""
        string = str(idee)
        isoString = string[42:70]
        for i in isoString:
            if i != '\"':
                criticIso += i
            else:
                break
        CRITICS.append(criticIso)

for letter in alphabet_array:
    get_authors_for_letter(letter)

print CRITICS

resultFile = open(csvfilename, 'w')
wr = csv.writer(resultFile)
wr.writerows([CRITICS])
