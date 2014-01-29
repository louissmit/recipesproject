__author__ = 'Maaike'


import glob
import json
import nltk
import pickle
from ingreProcessor import process

#nltk.internals.config_java('C:\\Program Files\\Java\\jre6\\bin\\java.exe')
#st = POSTagger('C:\Users\Maaike\PycharmProjects\untitled\uagger\models\english-bidirectional-distsim.tagger', 'C:\Users\Maaike\PycharmProjects\untitled\uagger\stanford-postagger.jar')
recipes = glob.glob('C:\\Users\\Maaike\\PycharmProjects\\recipesproject\\recipes\\*.json')

print len(recipes)

ingredients = dict()

stemmer = nltk.PorterStemmer()

for rec in recipes:
    file = open(rec)
    f = json.load(file)
    ingrds = f["Ingredients"]
    for ingdr in ingrds:
        i_name = ingdr["Name"]
        if not i_name == None:
            i_name = process(i_name)
            if not i_name == "":
                if ingredients.has_key(i_name):
                    ingredients[i_name]+=1
                else:
                    ingredients[i_name]=1

print ingredients

out = open("ingre.dict","wb")
pickle.dump(ingredients,out)