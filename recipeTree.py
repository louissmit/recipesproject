# -*- coding: utf-8 -*-

class recipeTree:
    # def __init__(self):
        # self.root = OperationNode()

    def parseTree(self, fileLoc):
        text_tree = open(fileLoc)
        children_list = []
        for line in text_tree:
            tabs = line.count('\t')
            print tabs
            if len(children_list) == tabs:
                print children_list
                children_list[tabs].append([])
            children_list[tabs].append(line)
        print children_list


class OperationNode:
    def __init__(self, operation):
        self.operation = operation
        self.children = []

class IngredientNode:
    def __init__(self, name):
        self.name = name