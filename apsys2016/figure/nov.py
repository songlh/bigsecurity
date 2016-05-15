import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime, timedelta

from matplotlib.backends.backend_pdf import PdfPages

with open('./nov.data.txt') as f:
	lines = f.read().splitlines()

dateList = []
subList =[]
malList = []

for line in lines:
	tmpList = line.split()
	dateList.append(datetime.strptime(tmpList[0], "%m/%d/%Y").date())
	subList.append(int(tmpList[1])/1000000.0)
	malList.append(int(tmpList[2])/1000000.0)

#for date in dateList:
#	print date
days = mdates.DayLocator(interval=2)

fig, ax = plt.subplots()
ax.plot(dateList, subList, 'b--', label = 'Submissions', linewidth=2.0)
ax.plot(dateList, malList, 'r-',  label='PE Malwares', linewidth=2.0)
legend = ax.legend(loc='upper left', fontsize='large')
plt.ylabel('VirusTotal reports (in million)', fontsize=18)

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
fig.savefig('nov.pdf')
plt.close(fig)
