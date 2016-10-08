import sys
import random
from os import listdir
from os.path import isfile, join
from sets import Set


def generateRandomIndex(numHash, numMax):
	hashList = []
	setHash = Set([])


	while numHash > 0:
		randIndex = random.randint(0, numMax)
		while randIndex in setHash:
			randIndex = random.randint(0, numMax)
			#print randIndex

		hashList.append(randIndex)
		setHash.add(randIndex)
		#print len(hashList)
		numHash -= 1

	return hashList




if __name__ == '__main__':

	sRawDirectory = sys.argv[1]
	sOutputDirectory = sys.argv[2]
	#numFamilyIndex = int(sys.argv[3])

	datafiles = [f for f in listdir(sRawDirectory) if isfile(join(sRawDirectory, f))]
	
	positiveList = []
	negativeList = []

	for datafile in datafiles:
		tmpList = datafile.split()

		if cmp(tmpList[0], sys.argv[3]+'.ssdeep.sample') == 0:
			f = open(join(sRawDirectory, datafile), 'r')
			while True:
				line = f.readline()
				if not line:
					break

				positiveList.append(line[:-1])
			f.close()

		else:
			f = open(join(sRawDirectory, datafile), 'r')
			while True:
				line = f.readline()
				if not line:
					break

				negativeList.append(line[:-1])
			f.close()

	print 'LOADING DONE'

	hashList1 = generateRandomIndex(10000, len(positiveList)-1)
	hashList2 = generateRandomIndex(20000, len(negativeList)-1)

	print 'RANDOM NUMBER DONE', len(hashList1), len(hashList2), len(negativeList)

	trainPositiveList = []
	testPositiveList = []

	trainNegativeList = []
	testNegativeList = []

	numIndex = 0

	while numIndex < len(positiveList):
		if numIndex in hashList1:
			trainPositiveList.append(positiveList[numIndex])
		else:
			testPositiveList.append(positiveList[numIndex])

		numIndex += 1

	print len(trainPositiveList), len(testPositiveList)
	numIndex = 0

	while numIndex < 10000:
		trainNegativeList.append(negativeList[hashList2[numIndex]])
		numIndex += 1

	numIndex = 10000
	while numIndex < 20000:
		testNegativeList.append(negativeList[hashList2[numIndex]])
		numIndex += 1

	ftrain = open(join(sOutputDirectory, 'train.txt'), 'w')
	for sample in trainPositiveList:
		ftrain.write(sample)
		ftrain.write('\n')

	for sample in trainNegativeList:
		ftrain.write(sample)
		ftrain.write('\n')

	ftrain.close()


	ftest = open(join(sOutputDirectory, 'test.txt'), 'w')
	for sample in testPositiveList:
		ftest.write(sample)
		ftest.write('\n')

	for sample in testNegativeList:
		ftest.write(sample)
		ftest.write('\n')

	ftest.close()


