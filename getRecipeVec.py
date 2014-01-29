__author__ = 'Maaike'


import pickle
import numpy
from ingreProcessor import process


class vectorFetcher:

    def __init__(self):
        self.ingredients = list(pickle.load(open('whitelist.set', 'rb')))
        self.matrix = pickle.load(open('normalized_ingr_vec.mat', 'rb'))

    def getVector(self, name):
        i_name = process(name)
        if not i_name in self.ingredients:
            print 'Yo Louis, I dont have a vector for that ingredient'
            return None
        index = self.ingredients.index(i_name)
        return self.matrix[index,:]
