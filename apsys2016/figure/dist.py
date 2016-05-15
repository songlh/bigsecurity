import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FixedLocator
import numpy as np

with open('./tag.total.result') as f:
	lines = f.read().splitlines()

numList = []

for line in lines:
	tmp = line.split()
	numList.append(int(tmp[1]))

total = sum(numList)

accumList = []
rateList = []
for i in range(0, 101, 2):
	accumList.append(sum(numList[0:(int)(i*1.0/100*len(numList))]) * 1.0/total * 100)
	rateList.append(i)


#for i in rateList:
#	print i, accumList[i]

fig, ax = plt.subplots()
ax.plot(rateList, accumList, 'r-x', markersize=6)


major_ticks = np.arange(0, 101, 10) 


xmin = -1
xmax = 101
ax.set_xlim(xmin, xmax)
#xticks = ax.xaxis.get_major_ticks()
#xticks[0].label1.set_visible(False)
ax.set_xticks(major_ticks)
plt.xlabel('% of hottest malware families', fontsize=14)

ymin = 0
ymax = 101
ax.set_ylim(ymin, ymax)
plt.ylabel('% of the total number of PE malware submissions',  fontsize=14)

ax.grid(True)
#plt.title('Cumulative frequencies')
#plt.show()
fig.savefig('cum.pdf')
plt.close(fig)