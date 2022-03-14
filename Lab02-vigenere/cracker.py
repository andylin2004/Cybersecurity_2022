from monocypher import *
import sys

def guessKeyLength(fileName: str, returnDecodedString: bool):
    bestLength = 0
    lowAvgDistance = 2
    bestBuckets = []
    textResult = ""
    fileContent = open(fileName, 'r').read()

    for i in range(1,17):
        bucket = []
        distance = 0
        for _ in range(i):
            bucket.append("")

        for v in range(len(fileContent)):
            bucket[v%i]+= fileContent[v]

        for v in bucket:
            print(v)
            distance += getRotationSpecs(v)["distance"]

        distance /= i
        
        if distance < lowAvgDistance:
            lowAvgDistance = distance
            bestLength = i
            bestBuckets = bucket
        
    if returnDecodedString:
        for i in range(len(bestBuckets)):
            bestBuckets[i] = decode(bestBuckets[i])
        
        for i in range(len(bestBuckets[0])):
            for v in range(len(bestBuckets)):
                if i < len(bestBuckets[v]):
                    textResult += bestBuckets[v][i]
        
        return textResult

    else:
        return bestLength

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(guessKeyLength(sys.argv[2], sys.argv[1] == "crack"))