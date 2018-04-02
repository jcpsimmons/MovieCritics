from bs4 import BeautifulSoup
import sys
import os
import csv

# open csv

def csvOpen(filename):
    with open('CriticScores.csv', 'r') as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            name_list.append(row)
    name_list = name_list[0]


# make dictionary (multiple entries)

# BS4 loop to scrape number of reviews

# save into CSV
