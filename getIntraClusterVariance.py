__author__ = 'Maaike'

import json
import glob
from ingreProcessor import process

recipes = glob.glob('C:\\Users\\Maaike\\PycharmProjects\\untitled\\recipes\\*.json')

ingredients = dict()
cuisines = dict()
meanrep = dict()

for rec in recipes:
    file = open(rec)
    f = json.load(file)
    ingrds = f["Ingredients"]

    cuisine = f["Category"]

    if cuisine == None:
        print 'empty cuisine encountered'
    else:
        if cuisines.has_key(cuisine):
            cuisines[cuisine]+=1
        else:
            cuisines[cuisine]=1

    #for ingdr in ingrds:
    #    i_name = ingdr["Name"]
    #    if not i_name == None:
    #        i_name = process(i_name)
    #        if not i_name == "":
    #            if ingredients.has_key(i_name):
    #               ingredients[i_name]+=1
    #            else:
    #                ingredients[i_name]=1

print cuisines
