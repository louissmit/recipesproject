import pickle
import numpy
import matplotlib.pyplot as plt
import operator
from matplotlib.mlab import PCA

matrix = pickle.load(open("cooccur.mat","rb"))
recipes = pickle.load(open('recipe_vec.dict',"rb"))

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

word = ['mustard','onion','sausag']
wvec = matrix2[1,:]*0

for w in word:
    wvec += matrix2[ingre.index(w),:]
wvec /= len(word)


for k in recipes.keys():
    recipes[k]=numpy.dot(recipes[k],wvec)

best = dict(sorted(recipes.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
print best