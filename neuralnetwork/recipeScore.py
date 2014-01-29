import cPickle as pickle
from database import DatabaseProxy
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import dummy
import numpy as np
from CooccurenceMatrix import CooccurenceMatrix
from NN import NN
db = DatabaseProxy()
recipe_vectors = pickle.load(open("../recipe_vec.dict", "rb"))
ingredients = pickle.load(open("../ingre.dict", "rb"))
recipes = db.getScoredRecipes()

nn = NN(recipes, recipe_vectors, 'nnet2')
# nn.train('nnet2')

# err = cross_validation.cross_val_score(linear_model.LinearRegression(), np.array(X), np.array(Y), cv=5, scoring="mean_squared_error")
# err2 = cross_validation.cross_val_score(dummy.DummyRegressor(), np.array(X), np.array(Y), cv=5, scoring="mean_squared_error")

# lin_model = linear_model.LinearRegression()
# lin_model.fit(np.array(X), np.array(Y))

co = CooccurenceMatrix()
good = co.getCombinedIngredientVector(['chocolate', 'marshmallows'])
bad = co.getCombinedIngredientVector(['brusselssprouts'])
meh = co.getCombinedIngredientVector(['rum'])
meh = co.getCombinedIngredientVector(['beer'])
worst = co.getCombinedIngredientVector(['beer', 'flour', 'vinegar'])

print nn.predict(good)
print nn.predict(bad)
print nn.predict(meh)
print nn.predict(worst)
