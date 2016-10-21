import ast
import compCI
import numpy as np 
import matplotlib.pyplot as plt
import math
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


if __name__ == '__main__':

	group1 = [2483, 575, 503, 456, 443, 381, 356, 356, 356 ]
	group2 = [4192, 762, 635, 588, 580, 534, 526, 526, 526 ]
	group3 = [5   ,  4 ,   3,   2,   2,   2,   2,   2,   2 ]
	group4 = [10000 , 9999, 9998 , 9997 , 9997 , 9997 , 9997 , 9997 , 9997 ]
	group5 = [8688 , 7727, 6630, 5462, 4699, 3690, 3103, 3028, 3028]
	group6 = [5807, 3915, 1590, 373, 18, 1, 1, 1, 1]
	group7 = [5429, 3651, 2703, 1615,726,400, 369, 362, 362]
	group8 = [2721, 1400,  871,  642, 549, 420, 399, 396, 396]
	group9 = [8500, 8199, 8012, 7808,  7597, 7327, 7171, 7150 , 7150]
	group10 = [8075, 7241, 6343, 5193, 4382, 3800, 3506, 3480, 3480]

	group1 = [math.log(num, 10) for num in group1]
	group2 = [math.log(num, 10) for num in group2]
	group3 = [math.log(num, 10) for num in group3]
	group4 = [math.log(num, 10) for num in group4]
	group5 = [math.log(num, 10) for num in group5]
	group6 = [math.log(num, 10) for num in group6]
	group7 = [math.log(num, 10) for num in group7]
	group8 = [math.log(num, 10) for num in group8]
	group9 = [math.log(num, 10) for num in group9]
	group10 = [math.log(num, 10) for num in group10]


	XList = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]      

	fig, ax = plt.subplots()
	ax.plot(XList, group1, 'b-o', label = 'Group 1')
	ax.plot(XList, group2, 'g--o', label = 'Group 2')
	ax.plot(XList, group3, 'r-.o', label = 'Group 3')
	ax.plot(XList, group4, 'c:o', label = 'Group 4')
	ax.plot(XList, group5, 'm-o', label = 'Group 5')
	ax.plot(XList, group6, 'y--o', label = 'Group 6')
	ax.plot(XList, group7, 'k-.o', label = 'Group 7')
	ax.plot(XList, group8, 'b:o', label = 'Group 8')
	ax.plot(XList, group9, 'g-o', label = 'Group 9')
	ax.plot(XList, group10, 'r--o', label = 'Group 10')

	majorLocator = MultipleLocator(0.1)
	ax.xaxis.set_major_locator(majorLocator)

	for tick in ax.xaxis.get_major_ticks():
		tick.label.set_fontsize(18)

	plt.xlabel('Distance Threshold', fontsize=20)

	for tick in ax.yaxis.get_major_ticks():
		tick.label.set_fontsize(18)  

	ax.yaxis.set_ticks(np.arange(1, 5))

	ind = np.arange(1,5)
	plt.yticks(ind, [ '10', '10^2', '10^3', '10^4'])

	plt.ylabel('# of Clusters (log scale)', fontsize=20)
	plt.gcf().subplots_adjust(bottom=0.15)
	plt.gcf().subplots_adjust(left=0.15)

	xmin = 0
	xmax = XList[-1] + 0.05

	ax.set_xlim(xmin, xmax)

	ymin = 0.0
	ymax = 4.5
	ax.set_ylim(ymin, ymax)



	legend = ax.legend(loc='upper left', fontsize='large', fancybox=True)
	legend.get_frame().set_alpha(0.5)


	#plt.show()

	fig.savefig('cluster.pdf')
	fig.savefig('cluster.png')
	plt.close(fig)