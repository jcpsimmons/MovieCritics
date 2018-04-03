from bs4 import BeautifulSoup
import sys
import os
import csv
import urllib2
import re

# critic-name: [score, reviews (-1 is INIT)]
CRITIC_DICT = {}

def findFirst(search_string, corpus):

    for count, value in enumerate(corpus):
        begin_clip = 0
        end_clip = 0
        if str(value).find(search_string) != -1:
            #now get just the full number out of this
            value = str(value)
            # reverse list
            value = value[::-1]
            for iter, char in enumerate(value):
                if bool(re.search(r'\d', char)) and end_clip == 0:
                    end_clip = iter
                    end_clip = len(value) - end_clip
            value = value[::-1]
            begin_clip = value.find('of') + 3
            value = value[begin_clip:end_clip]
            return value


def csvOpen(filename):
    with open(filename, 'r') as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            CRITIC_DICT[row[0]] = [row[1], -1]

# BS4 loop to scrape number of reviews
def scrapeNumberOfReviews(critic):
    test_page = "https://www.rottentomatoes.com/critic/" + critic + "/movies"
    page = urllib2.urlopen(test_page)
    soup = BeautifulSoup(page, 'html.parser')
    soup = soup.select('#criticsReviewsChart_main a')
    print findFirst('Showing', soup)


# save into CSV

# csvOpen('CriticScores.csv')

scrapeNumberOfReviews('armond-white')
scrapeNumberOfReviews('paul-eksteen')
scrapeNumberOfReviews('james-adams')
