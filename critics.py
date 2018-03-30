import urllib2
from bs4 import BeautifulSoup


# to be replaced with scraping from the critics list?
name_list = ["armond-white", "anthony-lane", "peter-rainer", "j-r-jones"]
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


#testing

test_page = "https://www.rottentomatoes.com/critic/j-r-jones/movies"
#gets the html
page = urllib2.urlopen(test_page)
#parse to BS4 format
soup = BeautifulSoup(page, 'html.parser')
# Reviews start at line 53 end with 249
corpus = soup.select('td')
# lop off array outside of 53 - 249
### THIS NEEDS to be tidied up and some how made relative so that different pages can be taken into account
for i in range(0,53):
    del(corpus[0])
for i in range(0,(len(corpus) - 196)):
    del(corpus[196])


# 1,2,5,6,9,10
# two pair streams each counting by four, generate one, clone it and add 1 to all values, then interleave (zip) the two lists
reviewer_rating_indices = range(1, len(corpus), 4)
rottentomatoes_rating_indices = range(2, len(corpus), 4)
# new_list = index_pattern_one + index_pattern_two
# new_list.sort() # automatically stores into list.
# actually keep them as separate

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
        decrease_autonomy('j-r-jones')
    else:
        increase_autonomy('j-r-jones')

print critics



    # if str(value).find('fresh') != -1 and str(rottentomatoes_reviews[i]).find('fresh') != -1:
    #     print "agree fresh!"
    # if str(value).find('rotten') != -1 and str(rottentomatoes_reviews[i]).find('rotten') != -1:
    #     print "agree rotten!"
