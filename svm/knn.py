import sys
import ssdeep
from os import listdir
from os.path import isfile, join
import operator

def ssdeep_distance(s1, s2):
	#print s1, s2
	match = ssdeep.compare(s1, s2)

	return 1.0 - match * 1.0 / 100

def loadSamples(sFileName):

	samples = []
	f = open(sTrain, 'r')
	while True:
		line = f.readline()
		if not line:
			break

		if cmp('None', line.split()[1]) == 0:
			continue

		samples.append(line.split()[1])

	labels = [0]*(len(samples)/2) + [1] * (len(samples)/2)

	return samples, labels 

def getNeighbors(trainSamples, testInstance, k):
	scores = []
	for index, sample in enumerate(trainSamples):
		scores.append((ssdeep_distance(sample, testInstance), index))

	scores.sort(key=operator.itemgetter(0))

	return scores[0:k]

def getResponse(trainLabels, neighbors):

	#print neighbors[0][0]
	if neighbors[2][0] == 1:
		return -1

	votes = {}

	for neighbor in neighbors:
		if trainLabels[neighbor[1]] in votes:
			votes[trainLabels[neighbor[1]]] += 1
		else:
			votes[trainLabels[neighbor[1]]] = 1

	sortedVotes = sorted(votes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]


if __name__ == '__main__':
	sDirectory = sys.argv[1]
	sTrain = join(sDirectory, 'train.txt')
	sTest = join(sDirectory, 'test.txt')

	trainSamples, trainLabels = loadSamples(sTrain)
	testSamples, testLabels = loadSamples(sTest)

	numIndex = 0


	miss = 0
	correct = 0
	wrong = 0

	while numIndex < len(testSamples):
		neighbors = getNeighbors(trainSamples, testSamples[numIndex], 3)
		respose = getResponse(trainLabels, neighbors) 
		
		if respose == -1:
			miss +=1

		elif respose == testLabels[numIndex]:
			correct += 1
		else:
			wrong += 1

		#print miss, correct, wrong

		numIndex += 1
		if numIndex == 10000:
			print miss, correct, wrong

	print miss, correct, wrong
