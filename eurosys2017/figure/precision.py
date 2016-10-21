import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from operator import itemgetter


if __name__ == '__main__':
	#XList = [0.0351, 0.0188, 0.0001, 0.9995, 0.2184, 0,      0.0307, 0.0280, 0.6517, 0.2679]
	#YList = [0.8127, 0.8200, 0.8255, 0.5981, 0.7623, 0.8179, 0.8179, 0.8226, 0.6441, 0.7406]

	DataList = [(0.0351, 0.8127), (0.0188, 0.8200), (0.0001, 0.8255), (0.9995, 0.5981), (0.2184, 0.7623), (0, 0.8179), (0.0307, 0.8179), (0.0280, 0.8226), (0.6517, 0.6441) , (0.2679, 0.7406)]

	DataList.sort(key=itemgetter(0))
	XList = []
	YList = []

	for data in DataList:
		XList.append(data[0])
		YList.append(data[1])

	fig, ax = plt.subplots()
	#ax.plot(XALL, YALL, 'b-o', label = 'All') #, mew=2, markersize = 8, linewidth=2.0)
	ax.plot(XList, YList, 'b-o')

	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(18)

	plt.xlabel('% of Tailing', fontsize=24)

	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(18)  

	plt.ylabel('Classification Accuracy', fontsize=24)

	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)

	xmin = XList[0]  - 0.05
	xmax = XList[-1] + 0.05

	ax.set_xlim(xmin, xmax)
	fig.savefig('accuracy.pdf')
	fig.savefig('accuracy.png')
	plt.close(fig)

	#plt.show()