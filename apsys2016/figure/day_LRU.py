import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime, timedelta

from matplotlib.backends.backend_pdf import PdfPages

with open('./day.LRU.result') as f:
	lines = f.read().splitlines()

dateList = []
numList =[]

for line in lines:
	tmpList = line.split()
	dateList.append(datetime.strptime(tmpList[0], "%Y-%m-%d").date())
	numList.append(float(tmpList[3]) * 100)


days = mdates.DayLocator(interval=2)

fig, ax = plt.subplots()
ax.plot(dateList, numList, 'r-x', markersize=10, mew=2)
#legend = ax.legend(loc='upper left', fontsize='large')
plt.ylabel('Cache hit rate (%)', fontsize=18)

ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%y'))
datemin = dateList[0]  - timedelta(days=1)
datemax = dateList[-1] + timedelta(days=1)

ax.set_xlim(datemin, datemax)
xticks = ax.xaxis.get_major_ticks()
xticks[0].label1.set_visible(False)


ymin = 0
ymax = 101
ax.set_ylim(ymin, ymax)

ax.grid(True)
fig.autofmt_xdate(rotation=90)
#plt.show()

#pdf = PdfPages('nov.pdf')
#pdf.savefig(plt.gcf())
fig.savefig('LRU.day.pdf')
plt.close(fig)
