import numpy as np
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.xml import *

class NN:
	def __init__(self, recipes=None, recipe_vectors=None , fileName=None):
		X, Y = self.preprocessData(recipes, recipe_vectors)
		self.ds = SupervisedDataSet(len(X[0]), 1)
		i = 0
		for x in X:
			self.ds.addSample(x, Y[i])
			i+=1
		if fileName == None:
			self.net = buildNetwork(len(X[0]), len(X[0]), 1, bias=True)
		else:
			self.net = NetworkReader.readFrom(fileName)

		self.trainer = BackpropTrainer(self.net, self.ds)


	def train(self, fileName):
		while True:
			try:
				print self.trainer.trainUntilConvergence(verbose=True)
			except KeyboardInterrupt:
				NetworkWriter.writeToFile(self.net, fileName)


	def predict(self, x):
		return self.net.activate(x)


	def preprocessData(self, recipes, recipe_vectors):
		X = []
		Y = []

		for id, recipe in recipes.items():
			rating = recipe["score"]
			id = int(id)
			if id in recipe_vectors:
				X.append(recipe_vectors[id])
				Y.append(rating)

		Y = (Y - np.mean(Y)) / np.sqrt(np.var(Y))
		return X, Y
