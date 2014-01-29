from couchquery import Database
import time
import os

class DatabaseProxy:
	def __init__(self):
		self.db = Database('http://localhost:5984/recipes')
		self.db.sync_design_doc('recipes', os.path.join(os.path.dirname(__file__), 'queries'))

	def fetchRecipes(self, sample=False):
		start = time.time()

		if sample:
			recipes = self.db.views.recipes.getSample()
		else:
			recipes = self.db.views.recipes.getValidRecipes()

		end = time.time()

		print "database call completed in" + (end - start)
		return recipes

	def getScoredRecipes(self):
		return self.db.views.recipes.getScoredRecipes()

	def getRecipe(self,id):
		return self.db.get(id)