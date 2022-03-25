#!/bin/python3

import sys

def fileManipulator(isDecode: bool, textFilename: str, keyFilename: str, outFilename: str):
    with open(textFilename, 'rb') as infile, open(outFilename, 'wb') as outfile, open(keyFilename, 'rb') as keyFile:
        fileBytes = infile.read()
        xorFilter = keyFile.read()
        for i in range(len(fileBytes)):
            b = b'\x05'
            x = int.from_bytes(b, byteorder='big')
            x = fileBytes[i] ^ xorFilter[i%len(xorFilter)]
            outfile.write(x.to_bytes(1, byteorder='big'))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileManipulator(sys.argv[1] == 'decode', sys.argv[2], sys.argv[3], sys.argv[4])