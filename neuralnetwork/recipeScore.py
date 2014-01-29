import cPickle as pickle
from database import DatabaseProxy
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import dummy
import numpy as np

db = DatabaseProxy()
recipe_vectors = pickle.load(open("../recipe_vec.dict", "rb"))
ingredients = pickle.load(open("../ingre.dict", "rb"))

X = []
Y = []

recipes = db.getScoredRecipes()
for id, recipe in recipes.items():
	rating = recipe["score"]
	id = int(id)
	if id in recipe_vectors:
		X.append(recipe_vectors[id])
		Y.append(rating)

err = cross_validation.cross_val_score(linear_model.LinearRegression(), np.array(X), np.array(Y), cv=5, scoring="mean_squared_error")
err2 = cross_validation.cross_val_score(dummy.DummyRegressor(), np.array(X), np.array(Y), cv=5, scoring="mean_squared_error")

lin_model = linear_model.LinearRegression()
lin_model.fit(np.array(X), np.array(Y))
predX = ingredients["potato"] + ingredients["marshmallow"]
print predX
prediction  = lin_model.predict(predX)
# print prediction
# print err
# print err2
# print len(X)
# print len(recipe_vectors)
