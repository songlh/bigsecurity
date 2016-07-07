import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from matplotlib.backends.backend_pdf import PdfPages

with open('../data/size.stat') as f:
	lines = f.read().splitlines()


sizeLogList = []
countLogList = []


for line in lines:
	tmpList = line.split()
	sizeLogList.append(int(tmpList[0]))
	countLogList.append(int(tmpList[1])/1000000.0)

with open('../data/pesize.stat') as f:
	lines = f.read().splitlines()


pesizeLogList = []
pecountLogList = []


for line in lines:
	tmpList = line.split()
	pesizeLogList.append(int(tmpList[0]))
	pecountLogList.append(int(tmpList[1])/1000000.0)


with open('../data/pemssize.stat') as f:
	lines = f.read().splitlines()


pemssizeLogList = []
pemscountLogList = []


for line in lines:
	tmpList = line.split()
	pemssizeLogList.append(int(tmpList[0]))
	pemscountLogList.append(int(tmpList[1])/1000000.0)

fig, ax = plt.subplots()
#ax.plot(sizeLogList, countLogList, 'b--', label = 'Submissions', linewidth=2.0)
#ax.plot(pesizeLogList, pecountLogList, 'r-.', label = 'PE Submissions', linewidth=2.0)
ax.plot(pemssizeLogList, pemscountLogList, 'b-', label = 'PE Malwares', linewidth=2.0)

legend = ax.legend(loc='upper left', fontsize='large')
plt.xlabel('File size (log2 based)', fontsize=18)
plt.ylabel('# of malwares (in million)', fontsize=18)

plt.gcf().subplots_adjust(left=0.20)

ax.grid(True)

#plt.show()

fig.savefig('size.pdf')
plt.close(fig)