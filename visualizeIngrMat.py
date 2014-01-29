__author__ = 'Maaike'

import pickle
import numpy
import matplotlib.pyplot as plt
from matplotlib.mlab import PCA

matrix = pickle.load(open("cooccur.mat","rb"))

#normalize vectors to unit length

for i in xrange(0,len(matrix)):
    length = numpy.linalg.norm(matrix[i,:])
    for j in xrange(0,len(matrix[i,:])):
        matrix[i,j]=(matrix[i,j]+0.0)/length


res = PCA(matrix)

matrix2 = res.Y[:,0:50]

for i in xrange(0,len(matrix2)):
    length = numpy.linalg.norm(matrix2[i,:])
    for j in xrange(0,len(matrix2[i,:])):
        matrix2[i,j]=(matrix2[i,j]+0.0)/length


#lets find the k-nearest neighbours of some example
ingre = pickle.load(open("whitelist.set","rb"))
ingre = list(ingre)

print 'THIS IS THE FIRST INGR',len(matrix2),len(ingre)

f = open('C:\\Users\\Maaike\\PycharmProjects\\untitled\\text sne\\testdata\\ingrevec2.txt','w')

for i in xrange(0,len(matrix2)):
    stra = ' '.join(map(str, matrix2[i,:]))
    print >>f, ingre[i], stra
