import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

if __name__ == '__main__':
	sDataFile = '../data/peSizeCorrelation.stat'
	fData = open(sDataFile, 'r')

	XList = []
	YList = []
	errList = []

	numList = []
	while True:
		line = fData.readline()
		if not line:
			break

		tmpList = line.split()

		XList.append(float(tmpList[0]))

		strTmp = ' '.join(tmpList[1:])
		tupleStat = ast.literal_eval(strTmp)
		numSqrt = tupleStat[0]
		numSum = tupleStat[1]
		numNum = tupleStat[2]
		numList.append(numNum)

		YList.append(float(numSum * 1.0/numNum))
		#print tmpList[0], YList[-1]
		errList.append(compCI.compCI(numSqrt, numSum, numNum))

	fData.close()

	print numList[9:36]
	print sum(numList[9:36]) * 1.0 / sum(numList)

	fig, ax = plt.subplots()
	ax.errorbar(XList, YList, yerr=errList, fmt='-o')

	majorLocator = MultipleLocator(10)
	ax.xaxis.set_major_locator(majorLocator)

	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(18)

	ax.set_xticklabels(['', '1KB', '1MB', '1GB'])
	plt.xlabel('File Size', fontsize=24)

	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(18)  

	plt.ylabel('Detection Ratio', fontsize=24)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)

	xmin = XList[0]  - 1
	xmax = XList[-1] + 1

	ax.set_xlim(xmin, xmax)

	ymin = 0.0
	ymax = 1.0
	ax.set_ylim(ymin, ymax)

	#fig.canvas.draw()

	#labels = [item.get_text() for item in ax.get_xticklabels()]
	#labels[1] = '-1'
	#labels[2] = '0'

	#ax.set_xticklabels(labels)

	#plt.show()
	fig.savefig('size.png')
	fig.savefig('size.pdf')
	plt.close(fig)