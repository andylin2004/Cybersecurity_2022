from monocypher import *

def guessKeyLength(fileName: str):
    bestLength = 0
    lowAvgDistance = 2
    fileContent = open(fileName, 'r').read()

    for i in range(1,17):
        buckets = []
        distance = 0
        for _ in range(i):
            buckets.append("")

        for v in range(len(fileContent)):
            buckets[v%i]+= fileContent[v]

        for v in buckets:
            print(v)
            distance += getRotationSpecs(v)["distance"]
            print(decode(v))

        distance /= i
        
        if distance < lowAvgDistance:
            lowAvgDistance = distance
            bestLength = i
        
        

    print(bestLength)

if __name__ == "__main__":
    guessKeyLength("crypt.txt")