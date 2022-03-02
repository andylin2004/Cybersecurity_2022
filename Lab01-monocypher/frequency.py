#!/bin/python3

import sys

charDistribution = {}
file = open(sys.argv[1], "r")
for line in file:
    for char in line:
        if char not in charDistribution:
            charDistribution[char] = 0
        charDistribution[char] += 1

print(charDistribution)