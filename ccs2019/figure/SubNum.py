import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

if __name__ == '__main__':
	sDataFile = '../data/subTotalHisNum.stat'
	fData = open(sDataFile, 'r')

	XList = []
	YList = []
	errList = []


	tmpSqrt = 0
	tmpSum = 0
	tmpNum = 0

	total = 0

	numList = []

	while True:
		line = fData.readline()
		if not line:
			break

		tmpList = line.split()

		x = int(tmpList[0])
		strTmp = ' '.join(tmpList[1:])
		tupleStat = ast.literal_eval(strTmp)

		#tmpSqrt += tupleStat[0]
		#tmpSum += tupleStat[1]
		#tmpNum += tupleStat[2]

		#if x % 5 == 0:
		#	XList.append(x)
		#	YList.append(float(tmpSum * 1.0/tmpNum))
		#	errList.append(compCI.compCI(tmpSqrt, tmpSum, tmpNum))

		#	tmpSqrt = 0
		#	tmpSum = 0
		#	tmpNum = 0

		XList.append(int(tmpList[0]))

		strTmp = ' '.join(tmpList[1:])
		tupleStat = ast.literal_eval(strTmp)
		numSqrt = tupleStat[0]
		numSum = tupleStat[1]
		numNum = tupleStat[2]

		YList.append(float(numSum * 1.0/numNum))
		errList.append(compCI.compCI(numSqrt, numSum, numNum))

		total += numNum
		numList.append(numNum)
	fData.close()

	for i, num, in enumerate(numList):
		print i, num, num * 1.0/total


	
	#if tmpNum > 1:
	#	XList.append(XList[-1] + 5)
	#	YList.append(float(tmpSum * 1.0/tmpNum))
	#	errList.append(compCI.compCI(tmpSqrt, tmpSum, tmpNum))


	fig, ax = plt.subplots()
	ax.errorbar(XList, YList, yerr=errList , markersize = 8, linewidth=0.5 ) #, fmt='-o')

	majorLocator = MultipleLocator(10)
	ax.xaxis.set_major_locator(majorLocator)

	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(14)

	plt.xlabel('Historical Submission Number', fontsize=24)

	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(18)  

	plt.ylabel('Detection Ratio', fontsize=24)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)

	xmin = XList[0]  - 5
	xmax = XList[-1] + 5

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
	fig.savefig('SubNum.png')
	fig.savefig('SubNum.pdf')
	plt.close(fig)