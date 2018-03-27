import urllib2
from bs4 import BeautifulSoup
#repl. with a way to scrape this from https://www.rottentomatoes.com/critics/authors

name_list = ["armond-white", "anthony-lane", "peter-rainer"]

critics = {}

## initialize critics key value pair with score
for name in name_list:
    critics[name] = .5

#testing

test_page = "https://www.rottentomatoes.com/critic/armond-white/movies"
#gets the html
page = urllib2.urlopen(test_page)
#parse to BS4 format
soup = BeautifulSoup(page, 'html.parser')
selection = soup.select("a.movie-link")

for i in selection:
    print i.string


# print selection[1].string
# print len(selection)

## math - if critic agrees take difference between current score and score
## in pos or negative direction depending on if pos or neg. divide
## by two and add or subtract to the score
