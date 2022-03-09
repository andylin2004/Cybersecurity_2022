#!/bin/python3

import sys
def shift(isDecode: bool, clearTextFile: str, keyFile: str):
    clearText = open(clearTextFile, "r").read().strip().upper()
    key = open(keyFile, "r").read().strip().upper()
    resultString = ""
    counter = 0
    
    for char in clearText:
        if char.isalpha():
            curMod = ord(key[counter%len(key)]) - 65
            if isDecode:
                curMod *= -1
            if ord(char) + curMod > 90:
                resultString += chr(65 + ord(char) + curMod - 91)
            elif ord(char) + curMod < 65:
                resultString += chr(90 - (64 - (ord(char) + curMod)))
            else:
                resultString += chr(ord(char) + curMod)
            print(curMod)
            counter += 1

    return resultString

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print(shift(sys.argv[1] == "decode", sys.argv[2], sys.argv[3]))