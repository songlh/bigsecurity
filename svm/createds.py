import sys
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
	sRawDirectory = sys.argv[1]
	sOutputDirectory = sys.argv[2]
	numFamilyIndex = int(sys.argv[3])

	datafiles = [f for f in listdir(sRawDirectory) if isfile(sRawDirectory, f)]
	
	positiveList = []
	negativeList = []

	for datafile in datafiles:
		tmpList = datafile.split()