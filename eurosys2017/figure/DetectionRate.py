import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def loadDetectionRate(sDataFile):
	fData = open(sDataFile, 'r')

	XList = []
	YList = []

	while True:
		line = fData.readline()
		if not line:
			break

		tmpList = line.split()
		
		XList.append(float(tmpList[0]))
		YList.append(int(tmpList[1]))

	fData.close()

	return XList, YList

if __name__ == '__main__':
	sAllDataFile = '../data/detection.stat'
	sVendorDataFile = '../data/vendorDetectionRate.stat'
	sUserDataFile = '../data/hotUserDetectionRate.stat'

	XALL, YALL = loadDetectionRate(sAllDataFile)
	XVendor, YVendor = loadDetectionRate(sVendorDataFile)
	XUser, YUser = loadDetectionRate(sUserDataFile)


	YALL = [num * 1.0/sum(YALL) for num in YALL]
	YVendor = [num * 1.0/sum(YVendor) for num in YVendor]
	YUser = [num * 1.0/sum(YUser) for num in YUser]
	#total = sum(YList)
	#YList = [num * 1.0/total for num in YList]

	#print YList[5:]
	#print sum(YList[5:])

	fig, ax = plt.subplots()
	#ax.plot(XALL, YALL, 'b-o', label = 'All') #, mew=2, markersize = 8, linewidth=2.0)
	ax.plot(XVendor, YVendor, 'b-o', label = 'Vendor')
	ax.plot(XUser, YUser, 'g:o', label = 'User')


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

	xmin = XALL[0]  - 0.05
	xmax = XALL[-1] + 0.05

	ax.set_xlim(xmin, xmax)

	ymin = 0.0
	ymax = 0.6
	ax.set_ylim(ymin, ymax)

	legend = ax.legend(loc='upper right', fontsize='large')
	#plt.ylabel('VirusTotal reports (in million)', fontsize=18)

	#fig.canvas.draw()

	#labels = [item.get_text() for item in ax.get_xticklabels()]
	#labels[1] = '-1'
	#labels[2] = '0'

	#ax.set_xticklabels(labels)

	#plt.show()
	fig.savefig('DetectionRate.pdf')
	fig.savefig('DetectionRate.png')
	plt.close(fig)
	#fig.savefig('IDReputation.png')
	#plt.close(fig)