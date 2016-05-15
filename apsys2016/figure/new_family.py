import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime, timedelta

from matplotlib.backends.backend_pdf import PdfPages

with open('./new.family.result') as f:
	lines = f.read().splitlines()

dateList = []
numList =[]

for line in lines:
	tmpList = line.split()
	dateList.append(datetime.strptime(tmpList[0], "%m/%d/%Y").date())
	numList.append(int(tmpList[1]))

newList = []
newList.append(numList[0])

index = 1

while index < len(numList):
	newList.append(numList[index] - numList[index-1])
	index += 1

days = mdates.DayLocator(interval=2)

fig, ax = plt.subplots()
ax.plot(dateList, newList, 'r-',  label='PE Malwares', linewidth=2.0)
#legend = ax.legend(loc='upper left', fontsize='large')
plt.ylabel('# of new malware families appeared', fontsize=18)

ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%y'))
datemin = dateList[0]  - timedelta(days=1)
datemax = dateList[-1] + timedelta(days=1)

ax.set_xlim(datemin, datemax)
xticks = ax.xaxis.get_major_ticks()
xticks[0].label1.set_visible(False)

ax.grid(True)
fig.autofmt_xdate(rotation=90)
#plt.show()

#pdf = PdfPages('nov.pdf')
#pdf.savefig(plt.gcf())
fig.savefig('new_family.pdf')
plt.close(fig)
