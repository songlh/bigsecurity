import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

if __name__ == '__main__':
	sDataFile = '../data/detection.stat'
	fData = open(sDataFile, 'r')

	XList = []
	YList = []
	errList = []

	while True:
		line = fData.readline()
		if not line:
			break

		tmpList = line.split()

		
		XList.append(float(tmpList[0]))
		YList.append(int(tmpList[1]))


	fData.close()

	total = sum(YList)
	YList = [num * 1.0/total for num in YList]

	fig, ax = plt.subplots()
	ax.plot(XList, YList, 'b-x', mew=2, markersize = 8, linewidth=2.0)


	majorLocator = MultipleLocator(0.1)
	ax.xaxis.set_major_locator(majorLocator)

	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(18)

	plt.xlabel('Detection Rate', fontsize=24)

	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(18)  

	plt.ylabel('Percentage of PE Submissions', fontsize=24)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)

	xmin = XList[0]  - 0.05
	xmax = XList[-1] + 0.05

	ax.set_xlim(xmin, xmax)

	ymin = 0.0
	ymax = 0.6
	ax.set_ylim(ymin, ymax)

	#fig.canvas.draw()

	#labels = [item.get_text() for item in ax.get_xticklabels()]
	#labels[1] = '-1'
	#labels[2] = '0'

	#ax.set_xticklabels(labels)

	#plt.show()
	fig.savefig('DetectionRate.pdf')
	fig.savefig('DetectionRate.png')
	#plt.close(fig)
	#fig.savefig('IDReputation.png')
	plt.close(fig)