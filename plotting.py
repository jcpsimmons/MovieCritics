import sys
import os
import csv
import numpy as np
import matplotlib.pyplot as plt

# critic-name: [score, reviews (-1 is INIT)]
SCORES = []
REVIEWS = []

with open('reviewScoresandreviewNumbers.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        SCORES.append(row[1])
        REVIEWS.append(row[2])


# Fixing random state for reproducibility
np.random.seed(19680801)

SCORES = np.array(SCORES)
REVIEWS = np.array(REVIEWS)

N = 3
x = SCORES
y = REVIEWS
colors = np.random.rand(N)
area = np.pi * (5)**2  # 0 to 15 point radii


plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
