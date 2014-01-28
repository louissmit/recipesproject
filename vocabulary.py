# -*- coding: utf-8 -*-
# from collections import OrderedDict
# import json
import cPickle as pickle
import re
from pprint import pprint
from nltk import word_tokenize
import nltk
import itertools
import operator
import time

def getVocabulary(recipes):
	start = time.time()
	tokens = {}
	for recipe in recipes:
		instructions = recipe['instructions']
		ingredients = recipe['ingredients']

		# sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		# sentences = sent_detector.tokenize(instructions.strip())
		# recipe_words = list(itertools.chain(*[word_tokenize(sent) for sent in sentences]))
		# recipe_words = [recipe_word.lower() for recipe_word in recipe_words]

		ingredients = [ingredient["Name"].lower() for ingredient in ingredients if ingredient["Name"] is not None]
		for ingredient in ingredients:
			ingredient = re.compile('[%s]' % '(){}\[\]<>*+;?=-').sub("",ingredient).strip()
			match = re.search(r""+ingredient,instructions,re.IGNORECASE)
			if match:
				token = match.group(0).lower()
				if tokens.has_key(token) and token!="":
					tokens[token] += 1
				else:
					tokens[token] = 1

	tokens = sorted(tokens.iteritems(), key=operator.itemgetter(1))
	tokens = [token for token in tokens if token[1] > 5]
	pprint(tokens)
	pprint(len(tokens))
	pickle.dump(tokens, open( "ingredients.p", "wb" ) )

	end = time.time()
	print end - start
	return tokens

