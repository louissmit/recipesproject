__author__ = '10634436'


def parse(ingredients, conProdDist=None):
    l = len(ingredients)+1
    matrix = [l+1]
    print len(matrix)
    for i in xrange(l):
        print i
        matrix[i] = [l+1]

    return matrix

a = list()
a.append('garlic')
a.append('onions')
parse(a)
