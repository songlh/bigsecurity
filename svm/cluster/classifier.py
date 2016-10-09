from config import *
import loader
from bintrees import AVLTree
import shutil
import os
from os import listdir
from os.path import isfile, join
import sys
import distance

class Distance:
	def __init__(self, dist, index):
		self.dist = dist
		self.index = index

	def __lt__(self, other):
		if self.dist < other.dist:
			return True

		if self.dist == other.dist and self.index < other.index:
			return True

		return False

	def __le__(self, other):
		if self.dist < other.dist:
			return True

		if self.dist == other.dist and self.index <= other.index:
			return True

		return False

	def __eq__(self, other):
		if self.dist == other.dist and self.index == other.index:
			return True

		return False

	def __ne__(self, other):
		if self.dist != other.dist or self.index != other.index:
			return True

		return False

	def __gt__(self, other):
		if self.dist > other.dist:
			return True

		if self.dist == other.dist and self.index > other.index:
			return True

		return False

	def __ge__(self, other):
		if self.dist > other.dist:
			return True

		if self.dist == other.dist and self.index >= other.index:
			return True

		return False 

	def __str__(self):
		return str(self.index) + ': ' + str(self.dist)


class classifier:
	# multiset for storing sorted distances: insert/delete operation - O(log N)
	# vector<multiset<Distance, Cmp> > P;
	# 2d vector for storing distances matrix
	# vector<unordered_map<int, Distance> > C;
	# vector for storing flags for marking currently active clusters
	# vector<int> II;
	# 2d vector for storing lists of titles in clusters
	# vector<vector<int> > A;

	# The way of separating clusters, either by
	# specifying the number of clusters K, or by
	# specifying a threshold T
	# int cutoffType;

	# number of classes to cluster
	# int numCluster;

	# seperating threshold
	# double threshold;

	# distance function
	# double distanceType;

	# number of rows of features
	# int N;

	# bitset representation of features
	# vector<bitset<FEATURE_SIZE> > features;

	# all-pair distance of features, either compute on-the-fly,
	# or read from file
	# vector<vector<float> > Dist;
	# vector<unordered_map<int, float> > Dist;
	def __init__(self, dist, md5List):
		#self.features = bfs
		self.Dist = dist
		self.N = len(self.Dist)
		self.md5List = md5List

	def setCluster(self, k):
		self.cutoffType = BY_NUMBER
		self.numCluster = k
		self.threshold = 10 * MIN_DIST

	def setThreshold(self, t):
		self.cutoffType = BY_THRESHOLD
		self.threshold = t
		self.numCluster = 1

	def initContainer(self):
		self.C = [None] * self.N
		self.P = [None] * self.N
		self.II = [0] * self.N
		self.A = [None] * self.N

		self.populate_distance()


	def populate_distance(self):
		added = 0
		for i in range(self.N):
			E_temp = self.Dist[i]
			V_temp = {}
			Q_temp = AVLTree()


			for key in range(len(E_temp)):
				j = key
				D_temp = Distance(E_temp[key], key)
				V_temp[key] = D_temp

				if key != i:
					Q_temp[D_temp] = D_temp

				added += 1

			self.C[i] = V_temp
			self.II[i] = 1
			self.P[i] = Q_temp

			A_i = []
			A_i.append(i)
			self.A[i] = A_i

	def clustering(self, linkage_criteria):
		#print '    Initialization ...\n'
		self.initContainer()
		#print '    Merging clusters ...\n'

		min_dist = MIN_DIST

		for n in range(self.N - self.numCluster):
			min_dist = MIN_DIST
			min_index = 0

			for k in range(self.N-1):
				if self.II[k] == 1 and len(self.P[k]) > 0:
					dist = self.P[k].min_key().dist
					if dist < min_dist:
						min_dist = dist
						min_index = self.P[k].min_key().index

			if min_dist > self.threshold:
				break

			k1 = min_index
			k2 = self.P[k1].min_key().index

			N_k1 = len(self.A[k1])
			N_k2 = len(self.A[k2])

			self.P[k1].clear()

			for l in range(len(self.A[k2])):
				self.A[k1].append(self.A[k2][l])

			self.II[k2] = 0

			#update distance for merged clustering
			for m in range(self.N):
				if len(self.C[m]) > 0:
					if self.II[m] != 0 and m != k1 and k1 in self.C[m] and k2 in self.C[m]:
						del self.P[m][self.C[m][k1]]
						del self.P[m][self.C[m][k2]]

						if linkage_criteria == SINGLE_LINKAGE:
							if self.C[m][k1].dist < self.C[m][k2].dist:
								self.C[m][k1].dist = self.C[m][k1].dist
							else:
								self.C[m][k1].dist = self.C[m][k2].dist

							self.C[k1][m].dist = self.C[m][k1].dist

						if linkage_criteria == COMPLETE_LINKAGE:
							if self.C[m][k1].dist > self.C[m][k2].dist:
								self.C[m][k1].dist = self.C[m][k1].dist
							else:
								self.C[m][k1].dist = self.C[m][k2].dist

							self.C[k1][m].dist = C[m][k1].dist

						if linkage_criteria == AVG_LINKAGE:
							self.C[m][k1].dist = (N_k1 * self.C[m][k1].dist + N_k2 * self.C[m][k2].dist)/(N_k1 + N_k2)
							self.C[k1][m].dist = self.C[m][k1].dist

						self.P[m][self.C[m][k1]] = self.C[m][k1]
						self.P[k1][self.C[k1][m]] = self.C[k1][m]

		print '  The min distance betwee clusters less than', min_dist

	def printClusters(self, size_threshold):
		print 'Output Clusters with size at least', size_threshold

		class_num = 0

		for i in range(self.N):
			if self.II[i] == 1:
				if len(self.A[i]) >= size_threshold:
					class_num += 1
					print 
					print 'Cluster', class_num, 'has', len(self.A[i])
					self.A[i].sort()

					for j in range(len(self.A[i])):
						print self.A[i][j],

					print

if __name__ == '__main__':
	sFileName = sys.argv[1]
	threshold = 0.9
	ssdeepList, md5List = loader.loadssdeepFile(sFileName)
	ssdeepList = ssdeepList[0:100]
	md5List = md5List[0:100]

	Dist = distance.all_pair_distance(ssdeepList, len(ssdeepList))

	classf = classifier(Dist, md5List)
	classf.setThreshold(threshold)
	classf.clustering(SINGLE_LINKAGE)
	classf.printClusters(1)