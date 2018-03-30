import string
import re
import urllib2
from bs4 import BeautifulSoup

CRITICS = []

alphabet_array = []

def make_alphabet():
    for c in string.ascii_lowercase:
        alphabet_array.append(c)

make_alphabet()

reviewer_list_baseurl = "https://www.rottentomatoes.com/critics/authors/?letter=a"

# for letter in alphabet_array:
#     reviewer_list_one_letter = reviewer_list_baseurl + letter
#     page = urllib2.urlopen(reviewer_list_one_letter)
#     soup = BeautifulSoup(page, 'html.parser')
#     print soup

page = urllib2.urlopen(reviewer_list_baseurl)
soup = BeautifulSoup(page, 'html.parser')

for idee in soup.findAll(attrs={'class':'critic-names'}):
    string = str(idee)
    isoString = string[42:70]
    print isoString
    # print string[var+8]
    # for i in range(30):
    #     if i != '\"':
    #         print string[i]
