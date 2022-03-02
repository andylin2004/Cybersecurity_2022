#!/bin/python3

import sys

charDistribution = {}
total = 0

for i in range(65,91):
    charDistribution[chr(i)] = 0

file = open(sys.argv[1], "r")
for line in file:
    for char in line.upper():
        if char in charDistribution:
            charDistribution[char] += 1
            total += 1

for i in charDistribution:
    print(i+": "+str(charDistribution[i]/total))