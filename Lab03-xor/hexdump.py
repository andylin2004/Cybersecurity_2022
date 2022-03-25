#!/bin/python3

import sys


def hexdump(fileName: str):
    with open(fileName, 'rb') as file:
        fileContents = file.read()
        resultString = ''
        for i in fileContents:
            if len(hex(i)[2:]) < 2:
                resultString += '0'
            resultString += hex(i)[2:] + ' '
        resultString.strip()
        return resultString

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(hexdump(sys.argv[1]))