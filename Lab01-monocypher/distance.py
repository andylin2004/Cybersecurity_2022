#!/bin/python3

from math import sqrt
import sys
from frequency import frequency

def distance(dict1: dict, dict2: dict):
    total = 0
    
    for file1Letter, file2Letter in zip(dict1, dict2):
        total += (dict1[file1Letter] - dict2[file2Letter]) ** 2
    
    return sqrt(total)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        file1Freq = frequency(sys.argv[1])
        file2Freq = frequency(sys.argv[2])

        print(distance(file1Freq, file2Freq))