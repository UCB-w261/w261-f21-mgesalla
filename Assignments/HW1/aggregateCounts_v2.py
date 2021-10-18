#!/usr/bin/env python
"""
This script reads word counts from STDIN and aggregates
the counts for any duplicated words.

INPUT & OUTPUT FORMAT:
    word \t count
USAGE (standalone):
    python aggregateCounts_v2.py < yourCountsFile.txt

Instructions:
    For Q7 - Your solution should not use a dictionary or store anything   
             other than a single total count - just print them as soon as  
             you've added them. HINT: you've modified the framework script 
             to ensure that the input is alphabetized; how can you 
             use that to your advantage?
"""

# imports
import sys
################# YOUR CODE HERE #################
temp_word = ""
temp_count = 0

for line in sys.stdin:
    word,count = line.split()  
    if word == temp_word:
        count = int(count) + int(temp_count)
    temp_word = word
    temp_count = count
    print(temp_word,temp_count) 
################ (END) YOUR CODE #################
