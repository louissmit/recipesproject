__author__ = 'Maaike'

import json
import glob
from ingreProcessor import process
import pickle, numpy
from matplotlib.mlab import PCA


#recipes = glob.glob('C:\\Users\\Maaike\\PycharmProjects\\untitled\\recipes\\*.json')
recipes = glob.glob('C:\\Users\\Maaike\\PycharmProjects\\recipesproject\\recipes\\*.json')

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

ids = dict()

for rec in recipes:
    file = open(rec)
    f = json.load(file)
    ingrds = f["Ingredients"]

    id = f["RecipeID"]

    rec_vec = matrix2[0,:]*0
    count = 0
    for ingdr in ingrds:
        i_name = ingdr["Name"]
        if not i_name == None:
            i_name = process(i_name)
            if i_name in ingre:
                rec_vec += matrix2[ingre.index(i_name),:]
                count+=1

    if count > 2:
        leng = numpy.linalg.norm(rec_vec)
        ids[id]=rec_vec/leng
        #print numpy.linalg.norm(ids[id])

f = open('recipe_vec.dict', 'wb')
pickle.dump(ids,f)

print ids