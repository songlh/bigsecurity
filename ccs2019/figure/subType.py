import matplotlib.pyplot as plt
import matplotlib.dates as mdates


from datetime import datetime, timedelta

from matplotlib.backends.backend_pdf import PdfPages

with open('../data/mergeType.stat') as f:
	lines = f.read().splitlines()

labelList = []
ratioList =[]


for line in lines:
	tmpList = line.split(' ')
	labelList.append(tmpList[0])
	ratioList.append(float(tmpList[1]))

fig, ax = plt.subplots()

colorList = [(0.0, 0.5, 0.0), (1.0, 1.0, 1.0), (1.0, 0.0, 0.0), (0.75, 0.75, 0), (0.25, 0.25, 0.25), (0.75, 0, 0.75), 
			(0.0, 0.75, 0.75), (0.996078431372549, 1.0, 0.7019607843137254), (0.15, 0.15, 0.15), (0.18823529411764706, 0.6352941176470588, 0.8549019607843137),
			(0.0, 0.0, 1.0), (1.0, 0.9294117647058824, 0.43529411764705883)]


plt.axes(aspect=1)

explores = [0] * len(colorList)
explores[0] = 0.05

patches, texts, autotexts = plt.pie(ratioList, explores, labelList, colors=colorList, autopct='%1.1f%%', shadow=True)

for text in texts:
	text.set_fontsize(16)

#plt.show()

fig.savefig('typePie.png')
plt.close(fig)