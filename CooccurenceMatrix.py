import cPickle as pickle
from ingreProcessor import process
import numpy as np


class CooccurenceMatrix:

	def __init__(self):
		self.ingredients = list(pickle.load(open('../whitelist.set', 'rb')))
		self.matrix = pickle.load(open('../normalized_ingr_vec.mat', 'rb'))

	def getIngredientVector(self, name):
		i_name = process(name)
		if not i_name in self.ingredients:
			print 'Yo Louis, I dont have a vector for that ingredient'
			return None
		index = self.ingredients.index(i_name)
		return self.matrix[index,:]

	def getCombinedIngredientVector(self, names):
		res = self.getIngredientVector(names[0]) * 0
		for name in names:
			res += self.getIngredientVector(name)

		return res / np.linalg.norm(res)
