import cPickle as pickle
from embedding import get_embedding

from vocabulary import getVocabulary
from database import fetchRecipes

# ingredients = pickle.load(open('ingredients.p', "rb"))
# ingredients = [ing for ing, occ in ingredients if occ > 30]
# get_embedding(ingredients)
getVocabulary(fetchRecipes())

