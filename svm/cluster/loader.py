
import sys


def loadssdeepFile(sFileName):
	ff = open(sFileName, 'r')

	ssdeepList = []
	md5List = []

	while True:
		line = ff.readline()
		if not line:
			break

		ssdeepList.append(line.split()[-1])
		md5List.append(line.split()[0])


	ff.close()

	return ssdeepList, md5List

if __name__ == '__main__':
	sFileName = sys.argv[1]
	ssdeepList = loadssdeepFile(sFileName)

	numIndex = 0

	for ssdeep in ssdeepList:
		print ssdeep
		numIndex += 1

		if numIndex == 10:
			break

