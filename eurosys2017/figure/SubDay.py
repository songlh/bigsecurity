import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime, timedelta

from matplotlib.backends.backend_pdf import PdfPages

dateList = []
subList =[]
peList = []

with open('../data/subByDay.stat') as f:
	lines = f.read().splitlines()

for line in lines:
	tmpList = line.split()
	dateList.append(datetime.strptime(tmpList[0], "%m/%d/%Y").date())
	subList.append(int(tmpList[1])/1000000.0)

with open('../data/peSubByDay.stat') as f:
	lines = f.read().splitlines()





#for date in dateList:
#	print date
days = mdates.DayLocator(interval=2)

fig, ax = plt.subplots()
ax.plot(dateList, subList, 'b--', label = 'Submissions', linewidth=2.0)
ax.plot(dateList, peList, 'r-.', label = 'PE Submissions', linewidth=2.0)
ax.plot(dateList, malList, 'g-',  label='PE Malwares', linewidth=2.0)
legend = ax.legend(loc='upper left', fontsize='large')
plt.ylabel('VirusTotal reports (in million)', fontsize=18)

ax.xaxis.set_major_locator(days)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%y'))
datemin = dateList[0]  - timedelta(days=1)
datemax = dateList[-1] + timedelta(days=1)

ax.set_xlim(datemin, datemax)
xticks = ax.xaxis.get_major_ticks()
xticks[0].label1.set_visible(False)
ax.xaxis.set_tick_params(labelsize=16)
ax.yaxis.set_tick_params(labelsize=16)

#plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.20)

ax.grid(True)
fig.autofmt_xdate(rotation=90)
#plt.show()

#pdf = PdfPages('nov.pdf')
#pdf.savefig(plt.gcf())
fig.savefig('nov.pdf')
plt.close(fig)
