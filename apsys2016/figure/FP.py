import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FixedLocator
import numpy as np

ratioList =     [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
fpList = [0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0,   0, 0, 0]



#for i in rateList:
#	print i, accumList[i]

fig, ax = plt.subplots()
ax.plot(ratioList, fpList, 'b-x', linewidth=2.0, markersize=14, mew=4)


#major_ticks = np.arange(0, 101, 10) 


xmin = 1
xmax = 16
ax.set_xlim(xmin, xmax)
xticks = ax.xaxis.get_major_ticks()
xticks[0].label1.set_visible(False)
xticks[-1].label1.set_visible(False)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(18) 
#ax.set_xscale("log", nonposx='clip')
plt.xlabel('$\phi/\epsilon$', fontsize=24)

ymin = - 5
ymax = 100
ax.set_ylim(ymin, ymax)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(18) 
#ax.set_yscale("log", nonposx='clip')
plt.ylabel('False positives (%)',  fontsize=24)

plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
ax.grid(True)
#plt.title('Cumulative frequencies')
#plt.show()
fig.savefig('fp.pdf')
plt.close(fig)