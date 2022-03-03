#!/bin/python3

import sys
from frequency import frequency
from distance import distance

def decode(fileName: str):
    distance = 2
    base = frequency("alice.txt")
    frequencyInput = frequency(fileName)

    for i in range(26):
        distance = min(distance, distance(base, frequencyInput))
    
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        print(decode(sys.argv[1]))