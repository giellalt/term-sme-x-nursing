#!/usr/bin/env python3

"""python script.py <fil>"""


import csv
import sys
from collections import Counter

infile = sys.argv[1]

with open(infile, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE)
    for row in spamreader:
        counts = Counter(row[7:11])
        print(counts)
