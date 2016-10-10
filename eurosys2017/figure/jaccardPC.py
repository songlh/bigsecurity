import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

if __name__ == '__main__':
	sDataFile = '../data/jaccardPC.result'
	fData = open(sDataFile, 'r')

	XList = []
	YList = []

	while True:
		line = fData.readline()
		if not line:
			break

		tmpList = line.split()

		strTmp = ' '.join(tmpList[1:])
		listTmp = ast.literal_eval(strTmp)
		XList.append(listTmp[-1])

		YList.append(listTmp[-2])

	fData.close()

	fig, ax = plt.subplots()
	ax.plot(XList, YList, 'b--', label = 'jaccardPC', linewidth=2.0)

	#majorLocator = MultipleLocator(10)
	#ax.xaxis.set_major_locator(majorLocator)

	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(18)

	plt.xlabel('FPR', fontsize=24)

	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(18)  

	plt.ylabel('TPR', fontsize=24)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)

	xmin = 0 #XList[0]  - 0.05
	xmax = 1.0 #XList[-1] + 0.05

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
	fig.savefig('jaccardPC.png')
	plt.close(fig)