import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
import math
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


if __name__ == '__main__':
	sDataFile = '../data/subPEID.stat'
	numRobert = 0
	numVendor = 0
	numExpert = 0
	numNormal = 0
	numOne = 0

	total = 0
	totalID = 0
	f = open(sDataFile, 'r')

	while True:
		line = f.readline()
		if not line:
			break

		tmpList = line.split()
		num = int(tmpList[1])

		total += num

		if cmp(tmpList[0], 'unknown') == 0:
			continue

		if num >= 1000000:
			numRobert += 1
		elif num >= 10000:
			numVendor += 1
		elif num >= 100:
			numExpert += 1
		elif num > 1:
			numNormal += 1
		else:
			assert(num == 1)
			numOne += 1

	f.close()
	totalID	= numRobert + numVendor + numExpert + numNormal + numOne


	ind = np.arange(5)
	YList = [numOne, numNormal, numExpert, numVendor, numRobert]
	YList = [math.log(num, 2) for num in YList]
	XList = ['(0,]', '(1,)', '[10^2,)', '[10^4,)', '[10^6,)']
	width = 0.5
	fig, ax = plt.subplots()
	rects = ax.bar(ind, YList, width, color='b')

	datemin = 0 - 0.2
	datemax = 5 + 0.2

	ax.set_xlim(datemin, datemax)

	ax.xaxis.set_tick_params(labelsize=16)
	ax.yaxis.set_tick_params(labelsize=16)

	plt.xticks(ind+width/2, XList)

	#plt.show()
	plt.xlabel('# of Submissions', fontsize=18)
	plt.ylabel('# of IDs (log scale)', fontsize=18)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)


	#print XList
	#print ind + width/2
	plt.xticks(ind+width/2, XList)

	plt.show()
	fig.savefig('IDDistribution.pdf')
	fig.savefig('IDDistribution.png')
	plt.close(fig)

