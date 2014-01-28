# -*- coding: utf-8 -*-

# from nltk.tree import Tree
# from nltk.treetransforms import chomsky_normal_form
from discodop.tree import Tree
from discodop.treedraw import test
from discodop.treetransforms import binarize
from discodop.grammar import doubledop
from discodop.parser import Parser
from discodop.parser import DEFAULTSTAGE
from discodop.parser import DictObj

class recipeTree:
	def __init__(self):
		# self.root = OperationNode("serve")
		# t = Tree("(S (COMBINE (MASH potato carrot onion) (STEAM rice)))")
		t = Tree.parse('(S (NP 0) (VP 1))', parse_leaf=int)
		sent = "Mary walks".split()
		# vp = Tree('VP', [Tree('V', ['saw']), Tree('NP', ['him'])])
		# t = Tree('S', [Tree('NP', ['I']), vp])
		t = binarize(t)
		grammar = doubledop([t], [sent], numproc=1)
		stage = DictObj(DEFAULTSTAGE, grammar=grammar)
		parser = Parser([stage])
		parser.parse("John walks".split())

		t.draw()

		# t.subtrees()

	def parseTree(self, fileLoc):
		text_tree = open(fileLoc, 'r')
		children_list = []
		for line in text_tree:
			tabs = line.count('\t')
			if len(children_list) <= tabs:
				children_list.append(list())
			children_list[tabs].append(line.rstrip().lstrip())
		print children_list
		print self.serializeSubTree(children_list)

		# while len(children_list) > 0:
		# 	candidate_children = children_list.pop(0)
		# 	root = candidate_children[0]
		# 	print candidate_children
		# 	if not len(candidate_children) > 2:
		# 		left_child = candidate_children[0]
		# 		right_child = candidate_children[1]
		# 		# node = OperationNode(candidate_parent.pop(-1), left_child, right_child)

	def serializeSubTree(self, children_list):
		res = ""
		if len(children_list) > 0:
			candidate_children = children_list.pop(0)
			root = candidate_children[0]
			res = "\n(" + root + self.serializeSubTree(children_list) + ")"
		return res

class OperationNode:
	def __init__(self, operation, left_child, right_child):
		self.operation = operation
		self.left_child = left_child
		self.right_child = right_child

class IngredientNode:
	def __init__(self, name):
		self.name = name