__author__ = 'Maaike'


import glob
import json
import nltk
import pickle
import numpy
from matplotlib.mlab import PCA
from ingreProcessor import process


#recipes = glob.glob('/Users/louissmit/Dropbox/recipeproject/recipes/*.json')
recipes = glob.glob('C:\\Users\\Maaike\\PycharmProjects\\recipesproject\\recipes\\*.json')

ingre = pickle.load(open("whitelist.set","rb"))
ingre = list(ingre)

matrix = numpy.zeros((len(ingre),len(ingre)))

#stemmer = nltk.PorterStemmer()

for rec in recipes:
    file = open(rec)
    f = json.load(file)
    ingrds = f["Ingredients"]

    ingr_in_recipe = set()

    for ingdr in ingrds:
        i_name = ingdr["Name"]
        if not i_name == None:
            i_name = process(i_name)
            if i_name in ingre:
                ingr_in_recipe.add(i_name)

    for ing1 in ingr_in_recipe:
        for ing2 in ingr_in_recipe:
            if not ing1 == ing2:
                i1 = ingre.index(ing1)
                i2 = ingre.index(ing2)
                matrix[i1][i2]+=1



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

out = open("cooccur.mat","wb")
pickle.dump(matrix,out)

out2 = open("normalized_ingr_vec.mat","wb")
pickle.dump(matrix2,out2)
print matrix