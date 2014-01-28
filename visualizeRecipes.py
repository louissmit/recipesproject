__author__ = 'Maaike'

import pickle
import random
import json

recipes = pickle.load(open('recipe_vec.dict', 'rb'))

n_rec = 500

random_dict = dict()

def getRecipeName(id):
    r = json.load(open('C:\\Users\\Maaike\\PycharmProjects\\untitled\\recipes\\'+str(id)+'.json'))
    r_name = r["Title"]
    r_name = ''.join(e for e in r_name if e.isalnum())
    r_name = r_name.split()
    return "_".join(r_name)

for i in xrange(0,n_rec):
    k = random.choice(recipes.keys())
    random_dict[k] = recipes[k]

print len(random_dict.keys()), getRecipeName(3)


f = open('C:\\Users\\Maaike\\PycharmProjects\\untitled\\text sne\\testdata\\recipevec.txt','w')

for k in random_dict.keys():
    stra = ' '.join(map(str, random_dict[k]))
    print getRecipeName(k), stra
    print >>f, getRecipeName(k), stra




