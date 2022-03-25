#!/bin/python3

with open('testfile01.txt', 'wb') as file:
    bytes = [65,66,97,98,10,72,101,108,108,111,32,119,111,114,108,100,10]
    for i in range(len(bytes)):
        file.write(bytes[i].to_bytes(1, byteorder='big'))