import sys
import ast
import math

t_table = [ (1, 12.71) ,\
			(2, 4.303),\
			(3, 3.182),\
			(4, 2.776),\
			(5, 2.571),\
			(6, 2.447),\
			(7, 2.365),\
			(8, 2.306),\
			(9, 2.262),\
			(10,2.228),\
			(11,2.201),\
			(12,2.179),\
			(13,2.160),\
			(14,2.145),\
			(15,2.131),\
			(16,2.120),\
			(17,2.110),\
			(18,2.101),\
			(19,2.093),\
			(20,2.086),\
			(21,2.080),\
			(22,2.074),\
			(23,2.069),\
			(24,2.064),\
			(25,2.060),\
			(26,2.056),\
			(27,2.052),\
			(28,2.048),\
			(29,2.045),\
			(30,2.042),\
			(40,2.021),\
			(50,2.009),\
			(60,2.000),\
			(80,1.990),\
			(100, 1.984),\
			(1000,1.962)]

def tableLookup(num):
	if num > 1000:
		return 1.96

	freedom = num - 1

	global t_table

	smallestNum = 100000
	smallestIndex = -1

	numIndex = 0

	while numIndex < len(t_table):
		item = t_table[numIndex]

		if abs(item[0] - num) < smallestNum:
			smallestNum = abs(item[0] - num)
			smallestIndex = numIndex

		numIndex += 1

	return t_table[smallestIndex][1]

def compCI(numSqrt, numSum, numNum):
	numMean = numSum * 1.0/numNum
	if numNum == 1:
		return 0

	numSD = numSqrt - 2 * numSum * numMean + numNum * numMean * numMean
	numSD = numSD / (numNum -1)

	numCI = math.sqrt(numSD) * tableLookup(numNum) / math.sqrt(numNum)

	return numCI


