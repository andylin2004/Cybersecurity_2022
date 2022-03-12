#!/bin/python3

import sys
from frequency import frequency
from distance import distance

def getRotationSpecs(fileName: str):
    lowDistance = 2.0
    base = frequency("alice.txt")
    frequencyInput = frequency(fileName)
    isBestReversed = False
    bestRotBy = 0
    temp = frequencyInput[chr(65)]

    # cycle through all 26 reversed permutations here
    for i in range(26):
        for v in range(65, 90):
            anotherTemp = frequencyInput[chr(v+1)]
            frequencyInput[chr(v+1)] = temp
            temp = anotherTemp

        frequencyInput[chr(65)] = temp

        candidate = distance(base, frequencyInput)
        if lowDistance > candidate:
            lowDistance = candidate
            isBestReversed = False
            bestRotBy = i

    for v in range(65, 90):
        anotherTemp = frequencyInput[chr(v+1)]
        frequencyInput[chr(v+1)] = temp
        temp = anotherTemp

    frequencyInput[chr(65)] = temp

    # reverse ordering here

    for i in range(13):
        temp = frequencyInput[chr(65+i)]
        frequencyInput[chr(65+i)] = frequencyInput[chr(90-i)]
        frequencyInput[chr(90-i)] = temp

    # cycle through all 26 reversed permutations here
    for i in range(27):
        for v in range(65, 90):
            anotherTemp = frequencyInput[chr(v+1)]
            frequencyInput[chr(v+1)] = temp
            temp = anotherTemp

        frequencyInput[chr(65)] = temp

        candidate = distance(base, frequencyInput)
        if lowDistance > candidate:
            lowDistance = candidate
            isBestReversed = True
            bestRotBy = i
    
    return {"isBestReversed": isBestReversed, "bestRotBy": bestRotBy, "distance": lowDistance}

def decode(fileName: str):
    rotationSpecs = getRotationSpecs(fileName)
    isBestReversed = rotationSpecs["isBestReversed"]
    bestRotBy = rotationSpecs["bestRotBy"]
    result = ""

    file = open(fileName, "r")
    for line in file:
        for char in line:
            if char.isalpha():
                # just to make my life sane, because I hate having to deal with lower and upper cases
                isUpper = char.isupper()
                char = char.upper()
                if isBestReversed:
                    # wrap over; we start from 90 because we are inversing things
                    if ord(char) - bestRotBy < 65:
                        char = chr(90 - (65 - (ord(char) - bestRotBy)))
                    else:
                        char = chr(90 - (ord(char)-bestRotBy))
                else:
                    # wrap over
                    if ord(char) + bestRotBy >= 90:
                        char = chr(65 + (ord(char) + bestRotBy - 90))
                    else:
                        char = chr(ord(char)+bestRotBy+1)
                if not isUpper:
                    char = char.lower()
            result += char

    result = result.strip()
    return result

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        print(decode(sys.argv[1]))
