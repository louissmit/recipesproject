__author__ = 'Henning'

import numpy


class TreeBuilder:

    
    def __init__(self, dim, labeled, unlabeled):
        #labeled is a list of tuples containing the sentence (as a list of words) and the label
        #unlabeled is a list of sentences (as a list of words)
        self.dim = dim
        self.labeled = labeled
        self.unlabeled = unlabeled

        #initializing the word representation
        self.vocab = self.initialize_vocab()
        #initializing the parameters W1,W2,b1,b2
        self.W1 =  numpy.random.normal(0,0.001,(dim,2*dim))
        self.W2 =  numpy.random.normal(0,0.001,(dim,2*dim))



    def initialize_vocab(self):
        sents = [x[0] for x in self.labeled]

        unique_words = set()
        for s in sents:
            for w in s:
                unique_words.add(w)
        for s in self.unlabeled:
            for w in s:
                unique_words.add(w)

        vocab = dict()
        for w in unique_words:
            vocab[w] = numpy.random.normal(0,0.001,(dim,1))

        return vocab






dim = 5
labeled = [(['hallo','mein','gott'],5),(['hallo','meine','gott'],5),(['hallo','mein','gotts'],5)]
unlabeled = [['hallo','mein','gott'],['hallo','meins','gott'],['hallo','mein','gotta']]

t = TreeBuilder(5,labeled,unlabeled)
print t.initialize_vocab()