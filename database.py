from couchquery import Database
import time
import os

def fetchRecipes(sample=False):
	start = time.time()
	db = Database('http://localhost:5984/recipes')

	db.sync_design_doc('recipes', os.path.join(os.path.dirname(__file__), 'queries'))
	if sample:
		recipes = db.views.recipes.getSample()
	else:
		recipes = db.views.recipes.getValidRecipes()

	end = time.time()

	print "database call complete"
	print end - start
	return recipes