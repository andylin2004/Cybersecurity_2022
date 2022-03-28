#!/bin/python3

import sys

def fileManipulator(textFilename: str, keyFilename: str):
    result = []

    with open(textFilename, 'rb') as infile, open(keyFilename, 'rb') as keyFile:
        fileBytes = infile.read()
        xorFilter = keyFile.read()
        for i in range(len(fileBytes)):
            b = b'\x05'
            x = int.from_bytes(b, byteorder='big')
            x = fileBytes[i] ^ xorFilter[i%len(xorFilter)]
            result.append(x.to_bytes(1, byteorder='big'))
    
    return result

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'encode':
            with open(sys.argv[4], 'wb') as outfile:
                for i in fileManipulator(sys.argv[2], sys.argv[3]):
                    outfile.write(i)
        elif sys.argv[1] == 'decode':
            result = ''
            for i in fileManipulator(sys.argv[2], sys.argv[3]):
                b = i
                x = int.from_bytes(b, byteorder='big')
                result += chr(x)
            
            print(result)