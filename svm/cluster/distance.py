import sys
import ssdeep
import loader
import thread
import threading
import config
import pickle


def ssdeep_distance(s1, s2):
	match = ssdeep.compare(s1, s2)

	return 1.0 - match * 1.0 / 100



def group_distance(ssdeepList1, ssdeepList2, numStart):
	Dist = []

	print len(ssdeepList1), len(ssdeepList2)
	for i in range(len(ssdeepList1)):
		for j in range(len(ssdeepList2)):
			Dist[(i+numStart) * len(ssdeepList2) + j] = ssdeep_distance(ssdeepList1[i], ssdeepList2[j])



def all_pair_distance(ssdeepList, N):

	Dist = []

	for i in range(N):
		Dist.append([])
		for j in range(N):
			if i == j:
				Dist[i].append(0)
			elif i > j:
				Dist[i].append(Dist[j][i])
			else:
				Dist[i].append(ssdeep_distance(ssdeepList[i], ssdeepList[j]))

	return Dist
	


def print_distance(Dist, N):

	for i in range(N):
		for j in range(N):
			print "{0:0.2f}".format(Dist[i][j]),

		print

def dump_distance(Dist, sSaveName):
	pickle.dump(Dist, open(sSaveName, 'wb'))


def load_distance(sSaveName):
	return pickle.load(open(sSaveName, 'rb'))

def stat_distance(Dist, N):

	listStat = [0] * 11

	for i in range(N):
		for j in range(N):
			if Dist[i][j] == 0:
				listStat[0] += 1
			elif Dist[i][j] <= 0.1:
				listStat[1] += 1
			elif Dist[i][j] <= 0.2:
				listStat[2] += 1
			elif Dist[i][j] <= 0.3:
				listStat[3] += 1
			elif Dist[i][j] <= 0.4:
				listStat[4] += 1
			elif Dist[i][j] <= 0.5:
				listStat[5] += 1
			elif Dist[i][j] <= 0.6:
				listStat[6] += 1
			elif Dist[i][j] <= 0.7:
				listStat[7] += 1
			elif Dist[i][j] <= 0.8:
				listStat[8] += 1
			elif Dist[i][j] <= 0.9:
				listStat[9] += 1
			else:
				listStat[10] += 1

	numIndex = 0

	while numIndex < 11:
		print numIndex, listStat[numIndex], listStat[numIndex] * 1.0 / N / N


if __name__ == '__main__':
	sSaveName = sys.argv[1]
	Dist = load_distance(sSaveName)

	stat_distance(Dist, len(Dist))

