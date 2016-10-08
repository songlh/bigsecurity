import ssdeep
import sys
import random

def generateRandomIndex(numHash, numMax):
	hashList = []

	while numHash > 0:
		randIndex = random.randint(0, numMax)
		while randIndex in hashList:
			randIndex = random.randint(0, numMax)

		hashList.append(randIndex)
		numHash -= 1

	return hashList


def loadssdeepFile(sFileName):
	fFile = open(sFileName, 'r')

	ssdeepList = []

	while True:
		line = fFile.readline()
		if not line:
			break

		tmpList = line.split()

		if cmp(tmpList[2], 'None') == 0:
			continue

		ssdeepList.append(line)

	fFile.close()

	return ssdeepList



if __name__ == '__main__':
	sFileName = sys.argv[1]
	sOutputFile = sys.argv[2]

	lines = loadssdeepFile(sFileName)
	indexList = generateRandomIndex(20000, len(lines))

	lineList = [lines[index] for index in indexList]

	fOutput = open(sOutputFile, 'w')

	for line in lineList:
		fOutput.write(line)

	fOutput.close()


	ssdeepList = [line.split()[2] for line in lineList]

	numCount = 0

	for ssdeep1 in ssdeepList:
		for ssdeep2 in ssdeepList:
			if ssdeep.compare(ssdeep1, ssdeep2) > 0:
				numCount += 1

	print numCount


