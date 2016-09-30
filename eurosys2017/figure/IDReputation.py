import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

if __name__ == '__main__':
	sDataFile = '../data/IDTotalFilterReputation.stat'
	fData = open(sDataFile, 'r')

	XList = []
	YList = []
	errList = []

	while True:
		line = fData.readline()
		if not line:
			break

		tmpList = line.split()

		if float(tmpList[0]) == -1.0:
			XList.append(-0.1)
		else:
			XList.append(float(tmpList[0]))

		strTmp = ' '.join(tmpList[1:])
		tupleStat = ast.literal_eval(strTmp)
		numSqrt = tupleStat[0]
		numSum = tupleStat[1]
		numNum = tupleStat[2]

		YList.append(float(numSum * 1.0/numNum))
		errList.append(compCI.compCI(numSqrt, numSum, numNum))

	fData.close()

	fig, ax = plt.subplots()
	ax.errorbar(XList, YList, yerr=errList, fmt='-o')

	majorLocator = MultipleLocator(0.1)
	ax.xaxis.set_major_locator(majorLocator)

	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(18)

	plt.xlabel('ID Reputation', fontsize=24)

	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(18)  

	plt.ylabel('Detection Ratio', fontsize=24)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)

	xmin = XList[0]  - 0.05
	xmax = XList[-1] + 0.05

	ax.set_xlim(xmin, xmax)

	ymin = 0.0
	ymax = 1.0
	ax.set_ylim(ymin, ymax)

	fig.canvas.draw()

	labels = [item.get_text() for item in ax.get_xticklabels()]
	labels[1] = '-1'
	labels[2] = '0'

	ax.set_xticklabels(labels)

	#plt.show()
	#fig.savefig('IDReputation.pdf')
	#plt.close(fig)
	fig.savefig('IDReputation.png')
	plt.close(fig)