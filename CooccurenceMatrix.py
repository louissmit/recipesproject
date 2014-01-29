import cPickle as pickle
from ingreProcessor import process


class CooccurenceMatrix:

	def __init__(self):
		self.matrix = pickle.load(open("cooccur.mat","rb"))
		self.ingr_index = pickle.load(open("whitelist.set","rb"))

	def getIngredientVector(self, name):
		index = self.ingr_index[process(name)]
		self.matrix
