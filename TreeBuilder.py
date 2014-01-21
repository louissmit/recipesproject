__author__ = 'Henning'

import numpy
from Tree import Tree


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
        self.W1 = numpy.random.normal(0,0.001,(dim,2*dim))
        self.W2 = numpy.random.normal(0,0.001,(2*dim,dim))
        self.b1 = numpy.random.normal(0,0.001,(dim,1))
        self.b2 = numpy.random.normal(0,0.001,(2*dim,1))



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



    def combine(self, v1, v2):
        #this is actually the activation function of the neural net
        #it is used to combine the representation of 2 subtrees (a subtree could be a terminal node)
        v_concat = numpy.concatenate((v1,v2),axis=0)
        v3 = numpy.dot(self.W1,v_concat)+self.b1
        #applying non-linearity
        for i in xrange(len(v3)):
            v3[i] = numpy.tanh(v3[i])

        return v3

    def reconstruct(self, v3):
        #this function reconstruct 2 child nodes given the parent node
        v12 = numpy.dot(self.W2,v3)+self.b2
        #applying non-linearity
        for i in xrange(len(v12)):
            v12[i] = numpy.tanh(v12[i])


        v1 = v12[0:self.dim]
        v2 = v12[self.dim:]

        return (v1,v2)

    def getReconstructionError(self, subtree):
        (v1, v2) = self.reconstruct(self.combine(subtree.child1.v,subtree.child2.v))

        w1 = (subtree.child1.n_kids+0.0)/(subtree.child1.n_kids+subtree.child2.n_kids)
        w2 = (subtree.child2.n_kids+0.0)/(subtree.child1.n_kids+subtree.child2.n_kids)

        d1 = numpy.linalg.norm(v1-subtree.child1.v)
        d2 = numpy.linalg.norm(v2-subtree.child2.v)

        return d1*w1 + d2*w2


    def train(self, subtree):
        err = self.getReconstructionError(subtree)




    def test(self):
        print 'Ahh'
        print self.vocab['hallo']
        print 'Combine'
        print self.combine(self.vocab['hallo'],self.vocab['gott'])
        print 'Recon'
        print self.reconstruct(self.vocab['hallo'])

        t1 = Tree()
        t1.root(self.vocab['hallo'])
        t2 = Tree()
        t2.root(self.vocab['gott'])
        t3 = Tree()
        t3.create(t1,t2,self.combine(t1.v,t2.v))

        print '#kids ',t3.n_kids

        print 'err', self.getReconstructionError(t3)







dim = 5
labeled = [(['hallo','mein','gott'],5),(['hallo','meine','gott'],5),(['hallo','mein','gotts'],5)]
unlabeled = [['hallo','mein','gott'],['hallo','meins','gott'],['hallo','mein','gotta']]

t = TreeBuilder(5,labeled,unlabeled)
t.test()