#!/bin/python3

from math import sqrt
import sys
from frequency import frequency

def distance(file1: str, file2: str):
    total = 0
    file1Freq = frequency(file1)
    file2Freq = frequency(file2)

    for file1Letter, file2Letter in zip(file1Freq, file2Freq):
        total += (file1Freq[file1Letter] - file2Freq[file2Letter]) ** 2

    return sqrt(total)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        print(distance(sys.argv[1], sys.argv[2]))