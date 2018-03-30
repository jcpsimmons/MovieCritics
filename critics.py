import urllib2
from bs4 import BeautifulSoup
import csv

name_list = []

with open('CriticsList.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        name_list.append(row)
name_list = name_list[0]

critics = {}
## initialize critics key value pair with score
for name in name_list:
    critics[name] = 0.

def increase_autonomy(critic_name):
    # get the current score
    current_score = critics[critic_name]
    new_score = (1 - current_score) * 0.5
    critics[critic_name] = critics[critic_name] + new_score
    return

def decrease_autonomy(critic_name):
    # get the current score
    if critics[critic_name] > 0.:
        current_score = critics[critic_name]
        new_score = (1 - current_score) * 0.5
        critics[critic_name] = critics[critic_name] - new_score
    else:
        return
    return


def calculate_score(critic):
    scan_offset = 0
    backend_marker = 0
    test_page = "https://www.rottentomatoes.com/critic/" + critic + "/movies"
    #gets the html
    page = urllib2.urlopen(test_page)
    #parse to BS4 format
    soup = BeautifulSoup(page, 'html.parser')
    # Reviews start at line 53 end with 249
    corpus = soup.select('td')
    # lop off array outside of 53 - 249
    ### THIS NEEDS to be tidied up and some how made relative so that different pages can be taken into account

    # strip the code from the site topnav bar
    for i in range(0,50):
        del(corpus[0])

    # Needed to be nested in function so that I can break after if is met
    def offset_finder(corpus_input):
        # hunt for the first movie link
        for count, value in enumerate(corpus_input):
            if str(value).find("movie-link") != -1:
                return count - 1
                break

    scan_offset = offset_finder(corpus)

    if scan_offset is None:
        print "No reviews found."
        critics[critic] = -1.
        return



    print("scan offset is " + str(scan_offset))

    def backend_finder(corpus_input):
        for value in reversed(corpus_input):
            if str(value).find("movie-link") != -1:
                return corpus_input.index(value)
                break

    backend_marker = backend_finder(corpus)


    # for i in range(0,(len(corpus) - 196)):
    #     del(corpus[196])


    # 1,2,5,6,9,10
    # two pair streams each counting by four, generate one, clone it and add 1 to all values, then interleave (zip) the two lists
    reviewer_rating_indices = range(scan_offset - 1, backend_marker, 4)
    rottentomatoes_rating_indices = range(scan_offset, backend_marker, 4)

    critic_reviews = []
    rottentomatoes_reviews = []


    for i in reviewer_rating_indices:
        critic_reviews.append(corpus[i])
    for i in rottentomatoes_rating_indices:
        rottentomatoes_reviews.append(corpus[i])

    for i, value in enumerate(critic_reviews):
        if str(value).find('fresh') != -1:
            critic_reviews[i] = 1
        else:
            critic_reviews[i] = 0

    for i, value in enumerate(rottentomatoes_reviews):
        if str(value).find('fresh') != -1:
            rottentomatoes_reviews[i] = 1
        else:
            rottentomatoes_reviews[i] = 0

    for i, value in enumerate(critic_reviews):
        if value == rottentomatoes_reviews[i]:
            decrease_autonomy(critic)
        else:
            increase_autonomy(critic)




# calculate_score("christian-bone")
# print critics["christian-bone"]

for key in critics:
    calculate_score(key)
    print key + str(critics[key])
