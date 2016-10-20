import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import ast
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

with open('../data/peSizeCorrelation.stat') as f:
	lines = f.read().splitlines()


sizeLogList = []
countLogList = []

total = 0
numList = []

for line in lines:
	tmpList = line.split()

	strTmp = ' '.join(tmpList[1:])
	tupleStat = ast.literal_eval(strTmp)
	numSqrt = tupleStat[0]
	numSum = tupleStat[1]
	numNum = tupleStat[2]
	total += numNum
	numList.append(numNum)

	sizeLogList.append(float(tmpList[0]))
	countLogList.append(int(numNum)/1000000.0)


print sum(numList[9:36]) * 1.0 / total 


fig, ax = plt.subplots()
#ax.plot(sizeLogList, countLogList, 'b--', label = 'Submissions', linewidth=2.0)
#ax.plot(pesizeLogList, pecountLogList, 'r-.', label = 'PE Submissions', linewidth=2.0)
ax.plot(sizeLogList, countLogList, 'b-o')

majorLocator = MultipleLocator(10)
ax.xaxis.set_major_locator(majorLocator)

for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(18)

#plt.xlabel('File Size (log2-based)', fontsize=24)

for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(18)  

ax.set_xticklabels(['', 'KB', 'MB', 'GB'])

plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)

xmin = sizeLogList[0]  - 1
xmax = sizeLogList[-1] + 1

ax.set_xlim(xmin, xmax)

#legend = ax.legend(loc='upper left', fontsize='large')
plt.xlabel('File Size', fontsize=24)
plt.ylabel('# of PE submissions (in million)', fontsize=24)

plt.gcf().subplots_adjust(left=0.20)

ax.grid(True)

#plt.show()

fig.savefig('pesize.pdf')
fig.savefig('pesize.png')
plt.close(fig)