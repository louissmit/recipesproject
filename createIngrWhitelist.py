__author__ = 'Maaike'


import pickle

meh = dict()
ingre = pickle.load(open("ingre.dict","rb"))

cutoff = 30

total = 0
whitelist = set()

hist = dict()

for k in ingre.keys():
    if ingre[k]>cutoff:
        #print k
        whitelist.add(k)
        total += 1
    if hist.has_key(ingre[k]):
        hist[ingre[k]]+=1
    else:
        hist[ingre[k]]=1


out = open("whitelist.set","wb")
pickle.dump(whitelist,out)