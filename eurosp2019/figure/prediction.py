import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def loadData(sDataFile):
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

	return XList, YList


sBernoulli = '../data/bernoulli.result'
sJaccard = '../data/jaccard.result'
sPC = '../data/PC.result'
sJaccardPC = '../data/jaccardPC.result'

fig, ax = plt.subplots()

XList, YList = loadData(sBernoulli)
ax.plot(XList, YList, 'b--', label = 'Bernoulli', linewidth=2.0)

XList, YList = loadData(sJaccard)
ax.plot(XList, YList, 'g-', label = 'Jaccard', linewidth=2.0)

XList, YList = loadData(sPC)
ax.plot(XList, YList, 'r:', label = 'Bernoulli with PC', linewidth=2.0)

XList, YList = loadData(sJaccardPC)
ax.plot(XList, YList, 'k-.', label = 'Jaccard with PC', linewidth=2.0)

XList = range(0, 1000, 20)
XList = [num * 1.0 / 1000 for num in XList]
YList = range(0, 1000, 20)
YList = [num * 1.0 / 1000 for num in YList]
ax.plot(XList, YList, 'k-.', label = 'Random Guess', linewidth=2.0)



legend = ax.legend(loc='lower right', fontsize='large')

for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(18)

plt.xlabel('FPR', fontsize=24)

for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(18)  

plt.ylabel('TPR', fontsize=24)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)

xticks = ax.xaxis.get_major_ticks()
xticks[0].label1.set_visible(False)

xmin = 0 #XList[0]  - 0.05
xmax = 1.0 #XList[-1] + 0.05

ax.set_xlim(xmin, xmax)

ymin = 0.0
ymax = 1.0
ax.set_ylim(ymin, ymax)

#plt.show()

fig.savefig('predict.png')
fig.savefig('predict.pdf')
plt.close(fig)
