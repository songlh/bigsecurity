import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FixedLocator
import numpy as np

with open('../data/lifeTime.stat') as f:
	lines = f.read().splitlines()

labelList = []
subList = []
peList = []

for line in lines:
	tmp = line.split()
	labelList.append(tmp[0])
	subList.append(int(tmp[1]))
	peList.append(int(tmp[2]))

subTotal = sum(subList)
peTotal = sum(peList)

accumList = []
peaccumList = []
rateList = []

for i in range(1, len(subList) + 1):
	accumList.append(sum(subList[0:i]) * 1.0/subTotal * 100)
	peaccumList.append(sum(peList[0:i]) * 1.0/peTotal * 100)
	rateList.append(i-1)
	



fig, ax = plt.subplots()
ax.plot(rateList, accumList, 'b-x', linewidth=2.0, label = 'Submissions',  markersize=5, mew=2)
ax.plot(rateList, peaccumList, 'r--x', linewidth=2.0, label = 'PE Submissions', markersize=5, mew=2)
plt.xticks(rateList, labelList, rotation='vertical')

legend = ax.legend(loc='lower right', fontsize='large')
xmin = -0.1
xmax = 7.1
ax.set_xlim(xmin, xmax)


ymin = 0
ymax = 101
ax.set_ylim(ymin, ymax)
plt.ylabel('% of (PE) Submissions', fontsize=18)

yticks = ax.yaxis.get_major_ticks()
yticks[0].label1.set_visible(False)

ax.xaxis.set_tick_params(labelsize=16)
ax.yaxis.set_tick_params(labelsize=16)
plt.xlabel('Life Time',  fontsize=18)
plt.gcf().subplots_adjust(bottom=0.25)

#plt.show()
fig.savefig('lifetime.pdf')
plt.close(fig)