#!bin/python3

with open('testfile01.txt', 'rb') as infile, open('testfile02.txt', 'wb') as outfile:
    fileBytes = infile.read()
    for i in range(len(fileBytes)):
        b = b'\x05'
        x = int.from_bytes(b, byteorder='big')
        x = fileBytes[i]+1
        outfile.write(x.to_bytes(1, byteorder='big'))