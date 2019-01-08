import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from matplotlib.backends.backend_pdf import PdfPages

import sys
import os
from os.path import isfile, join
from os import listdir

sDirectory = sys.argv[1]
DataFiles = [f for f in listdir(sDirectory) if isfile(join(sDirectory, f))]

DataFiles.sort()

for datafile in DataFiles:
	#print datafile
	XLabels = []
	precisionList = []

	with open(join(sDirectory, datafile)) as f:
		lines = f.read().splitlines()

	for line in lines:
		tmpList = line.split()
		XLabels.append(tmpList[0])
		precisionList.append(float(tmpList[1]))

	fig, ax = plt.subplots()
	ax.plot(range(len(precisionList)), precisionList, 'b-x', mew=2, markersize = 8, linewidth=2.0)

	ymin = 0.4
	ymax = 0.9
	ax.set_ylim(ymin, ymax)

	xmin = -1
	xmax = len(precisionList) + 1
	ax.set_xlim(xmin, xmax)

	#ax.set_xticks(range(len(precisionList)))
	ax.set_xticklabels([10, 50, 100, 500, 1000, 5000, 10000])

	ax.xaxis.set_tick_params(labelsize=22)
	ax.yaxis.set_tick_params(labelsize=22)

	plt.xlabel('# of Samples in Training Set', fontsize=28)
	plt.ylabel('Accuracy', fontsize=28)
	plt.gcf().subplots_adjust(bottom=0.20)
	plt.gcf().subplots_adjust(left=0.20)
	#plt.show()

	fig.savefig(datafile.split('.')[0] + '.pdf')
	fig.savefig(datafile.split('.')[0] + '.png')
	plt.close(fig)