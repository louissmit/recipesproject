__author__ = 'Maaike'

import pickle
import random
import numpy

matrix = list(pickle.load(open('normalized_ingr_vec.mat','rb')))
l = numpy.arange(0,len(matrix))


def createRandomRecipe():
    out = matrix[random.choice(l)]
    for i in xrange(0,7):
        out += matrix[random.choice(l)]
    out /= numpy.linalg.norm(out)
    return out

