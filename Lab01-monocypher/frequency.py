#!/bin/python3

import sys

def frequency(fileName: str):
    charDistribution = {}
    total = 0

    for i in range(65,91):
        charDistribution[chr(i)] = 0

    file = open(fileName, "r")
    for line in file:
        for char in line.upper():
            if char in charDistribution:
                charDistribution[char] += 1
                total += 1
    
    for letter in charDistribution:
        charDistribution[letter] /= total
        
    return charDistribution

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        charDistribution = frequency(sys.argv[1])

        for letter in charDistribution:
            print(letter+": "+str(charDistribution[letter]))