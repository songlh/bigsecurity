import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FixedLocator
import numpy as np

phiList = [10, 100, 1000]
overlapList = [79.37152483, 95.48188252, 99.70590609]



#for i in rateList:
#	print i, accumList[i]

fig, ax = plt.subplots()
ax.plot(phiList, overlapList, 'r-x', linewidth=2.0, markersize=14, mew=4)


#major_ticks = np.arange(0, 101, 10) 


xmin = 9
xmax = 1100
ax.set_xlim(xmin, xmax)
#xticks = ax.xaxis.get_major_ticks()
#xticks[0].label1.set_visible(False)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(18) 
ax.set_xscale("log", nonposx='clip')
plt.xlabel('$\phi$', fontsize=24)

#ymin = 0
#ymax = 101
#ax.set_ylim(ymin, ymax)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(18) 
plt.ylabel('Degree of overlap (%)',  fontsize=24)

plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.grid(True)
#plt.title('Cumulative frequencies')
#plt.show()
fig.savefig('overlap.pdf')
plt.close(fig)