import svmpy
from os import listdir
from os.path import isfile, join
import sys

if __name__ == '__main__':
	sDirectory = sys.argv[1]
	sTrain = join(sDirectory, 'train.txt')
	sTest = join(sDirectory, 'test.txt')

	samples = []

	fTrain = open(sTrain, 'r')
	while True:
		line = fTrain.readline()
		if not line:
			break
		samples.append(line.split()[1])


	fTrain.close()

	samples = samples[0:5] + samples[10000:10005]
	labels = [0,0,0,0,0,1,1,1,1,1]

	trainer = svmpy.SVMTrainer(svmpy.Kernel.ssdeep_kernel(), 0.1)
	predictor = trainer.train(samples, labels)
