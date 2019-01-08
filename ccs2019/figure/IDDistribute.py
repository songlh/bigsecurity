import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
import math
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


if __name__ == '__main__':
	sDataFile = '../data/subPEID.stat'
	numMillion = 0
	num10Thousand = 0
	numHundred = 0
	numTen = 0
	numOne = 0
	numZero = 0

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

		if num > 1000000:
			numMillion += 1
		elif num > 10000:
			num10Thousand += 1
		elif num > 100:
			numHundred += 1
		elif num > 10:
			numTen += 1
		elif num > 1:
			numOne += 1
		else:
			assert(num == 1)
			numZero += 1

	f.close()

	totalID	= numMillion + num10Thousand + numHundred + numTen + numOne + numZero


	ind = np.arange(6)
	YList = [numZero, numOne, numTen, numHundred, num10Thousand, numMillion]
	YList = [math.log(num, 10) for num in YList]

	print YList

	XList = ['1', '1-10', '10-100', '100-10k', '10k-1m', '1m-']
	width = 0.5
	fig, ax = plt.subplots()
	rects = ax.bar(ind, YList, width, color='b')

	datemin = 0 - 0.2
	datemax = 6 #+ 0.2

	ax.set_xlim(datemin, datemax)

	datemin = 0 
	datemax = 5.9

	ax.set_ylim(datemin, datemax)

	ax.xaxis.set_tick_params(labelsize=16)
	ax.yaxis.set_tick_params(labelsize=16)

	plt.xticks(ind+width/2, XList)

	ind = np.arange(6)
	plt.yticks(ind, ['0', '10', '10^2', '10^3', '10^4', '10^5'])

	#plt.show()
	plt.xlabel('# of Submissions', fontsize=18)
	plt.ylabel('# of IDs (log scale)', fontsize=18)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)


	#print XList
	#print ind + width/2
	plt.xticks(ind+width/2, XList)

	#plt.show()
	fig.savefig('IDDistribution.pdf')
	fig.savefig('IDDistribution.png')
	plt.close(fig)

