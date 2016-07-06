import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FixedLocator
import numpy as np

with open('../data/subcountry.stat') as f:
	lines = f.read().splitlines()


countryList = []

for line in lines:
	tmpList = line.split()
	if cmp(tmpList[0], 'on') == 0 :
		continue

	if cmp(tmpList[0], 'ZZ') == 0:
		continue

	countryList.append(int(tmpList[1]))

countryList.reverse()
total = sum(countryList)


with open('../data/pesubcountry.stat') as f:
	lines = f.read().splitlines()


pecountryList = []

for line in lines:
	tmpList = line.split()
	if cmp(tmpList[0], 'on') == 0 :
		continue

	if cmp(tmpList[0], 'ZZ') == 0:
		continue

	pecountryList.append(int(tmpList[1]))

pecountryList.reverse()
petotal = sum(countryList)

accumList = []
peaccumList = []
rateList = []
for i in range(0, 101, 2):
	accumList.append(sum(countryList[0:(int)(i*1.0/100*len(countryList))]) * 1.0/total * 100)
	peaccumList.append(sum(pecountryList[0:(int)(i*1.0/100*len(pecountryList))]) * 1.0/petotal * 100)
	rateList.append(i)

fig, ax = plt.subplots()
ax.plot(rateList, accumList, 'b-x', linewidth=2.0, label = 'Submissions', markersize=5, mew=2)

major_ticks = np.arange(0, 101, 10) 


xmin = -1
xmax = 101
ax.set_xlim(xmin, xmax)
#xticks = ax.xaxis.get_major_ticks()
#xticks[0].label1.set_visible(False)
ax.set_xticks(major_ticks)
plt.ylabel('% of Submissions', fontsize=18)

ymin = 0
ymax = 101
ax.set_ylim(ymin, ymax)
plt.xlabel('% of countries',  fontsize=18)
ax.xaxis.set_tick_params(labelsize=16)
ax.yaxis.set_tick_params(labelsize=16)


ax.grid(True)
#plt.show()
fig.savefig('country.pdf')
plt.close(fig)