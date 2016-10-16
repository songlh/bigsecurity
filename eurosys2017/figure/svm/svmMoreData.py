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
	print datafile
	XLabels = []
	precisionList = []

	with open(join(sDirectory, DataFiles[0])) as f:
		lines = f.read().splitlines()

	for line in lines:
		tmpList = line.split()
		XLabels.append(tmpList[0])
		precisionList.append(float(tmpList[1]))

	fig, ax = plt.subplots()
	ax.plot(range(len(precisionList)), precisionList, 'b-x', mew=2, markersize = 8, linewidth=2.0)

	#ymin = 0.0
	#ymax = 1.0
	#ax.set_ylim(ymin, ymax)

	xmin = -1
	xmax = len(precisionList) + 1
	ax.set_xlim(xmin, xmax)

	#ax.set_xticks(range(len(precisionList)))
	ax.set_xticklabels([10, 50, 100, 500, 1000, 5000, 10000])

	ax.xaxis.set_tick_params(labelsize=16)
	ax.yaxis.set_tick_params(labelsize=16)

	plt.xlabel('# of Samples in Training Set', fontsize=24)
	plt.ylabel('Precision', fontsize=24)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)
	plt.show()

	fig.savefig(datafile + '.pdf')
	fig.savefig(datafile + '.png')
	plt.close(fig)