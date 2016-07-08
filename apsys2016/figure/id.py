import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FixedLocator
import numpy as np
#import statistics


with open('../data/subid.stat') as f:
	lines = f.read().splitlines()


idList = []

for line in lines:
	tmpList = line.split()
	if cmp(tmpList[0], 'None') == 0:
		continue

	idList.append(int(tmpList[1]))

#print np.mean(np.array(idList))
#print np.median(np.array(idList))

idList.reverse()

total = sum(idList)

with open('../data/pesubid.stat') as f:
	lines = f.read().splitlines()


peidList = []

for line in lines:
	tmpList = line.split()
	if cmp(tmpList[0], 'None') == 0:
		continue

	peidList.append(int(tmpList[1]))

peidList.reverse()

petotal = sum(peidList)


with open('../data/peMSSubID.stat') as f:
	lines = f.read().splitlines()


pemsidList = []

for line in lines:
	tmpList = line.split()
	if cmp(tmpList[0], 'None') == 0:
		continue

	pemsidList.append(int(tmpList[1]))

pemsidList.reverse()

pemstotal = sum(pemsidList)

accumList = []
peaccumList = []
pemsaccumList = []
rateList = []

for i in range(0, 101, 2):
	accumList.append(sum(idList[0:(int)(i*1.0/100*len(idList))]) * 1.0/total * 100)
	peaccumList.append(sum(peidList[0:(int)(i*1.0/100*len(peidList))]) * 1.0/petotal * 100)
	pemsaccumList.append(sum(pemsidList[0:(int)(i*1.0/100*len(pemsidList))]) * 1.0/pemstotal * 100)
	rateList.append(i)

#print accumList
#print peaccumList

fig, ax = plt.subplots()
ax.plot(rateList, pemsaccumList, 'b-x', linewidth=2.0, label = 'Submissions', markersize=5, mew=2)
#ax.plot(rateList, peaccumList, 'r--x', linewidth=2.0, label = 'PE Submissions', markersize=5, mew=2)

major_ticks = np.arange(0, 101, 10) 


xmin = -1
xmax = 101
ax.set_xlim(xmin, xmax)
#xticks = ax.xaxis.get_major_ticks()
#xticks[0].label1.set_visible(False)
ax.set_xticks(major_ticks)
plt.ylabel('CDF of Malwares', fontsize=18)

ymin = 0
ymax = 101
ax.set_ylim(ymin, ymax)
plt.xlabel('% of all VirusTotal ID',  fontsize=18)
ax.xaxis.set_tick_params(labelsize=16)
ax.yaxis.set_tick_params(labelsize=16)


ax.grid(True)
#plt.show()
fig.savefig('id.pdf')
plt.close(fig)