#!/bin/python3

import sys
from frequency import frequency
from distance import distance

def decode(fileName: str):
    lowDistance = 2
    base = frequency("alice.txt")
    frequencyInput = frequency(fileName)
    isBestReversed = False
    bestRotBy = 0
    result = ""
    temp = frequencyInput[chr(65)]

    for i in range(26):
        for i in range(65, 90):
            anotherTemp = frequencyInput[chr(i+1)]
            frequencyInput[chr(i+1)] = temp
            temp = anotherTemp

        frequencyInput[chr(65)] = temp

        if lowDistance > distance(base, frequencyInput):
            lowDistance = distance(base, frequencyInput)
            isBestReversed = False
            bestRotBy = i

    # reverse ordering here

    for i in range(13):
        temp = frequencyInput[chr(65+i)]
        frequencyInput[chr(65+i)] = frequencyInput[chr(90-i)]
        frequencyInput[chr(90-i)] = temp

    for i in range(26):
        if lowDistance > distance(base, frequencyInput):
            lowDistance = distance(base, frequencyInput)
            isBestReversed = True
            bestRotBy = i

    file = open(fileName, "r")
    for line in file:
        lineResult = ""
        for char in line:
            if char.isalpha():
                if isBestReversed:
                    if ord(char) - bestRotBy < 65:
                        lineResult += chr(90 - (65 - (ord(char) - bestRotBy)))
                    else:
                        lineResult += chr(90-bestRotBy)
                else:
                    if ord(char) + bestRotBy > 90:
                        lineResult += chr(65 + (ord(char) + bestRotBy-90))
                    else:
                        lineResult += chr(65+bestRotBy)

            result += lineResult
            lineResult = ""

    return result


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        print(decode(sys.argv[1]))
