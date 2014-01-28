import nltk
stemmer = nltk.PorterStemmer()

def process(i_name):
    i_name = i_name.lower()
    i_name = i_name.split()

    blacklist = ['frozen', 'grated', 'plain', 'chopped', 'sliced', 'diced', 'freshly', 'fresh', 'ground', 'bottled', 'canned', 'regular', 'thin', 'thinly', 'canned', 'small', 'large', 'skinned', 'peeled', 'boneless', 'skinless', 'roasted', 'glutenfree']
    tokick = list()

    for w in i_name:
        if w in blacklist:
            tokick.append(w)

    for w in tokick:
        i_name.remove(w)

    i_name = ''.join(i_name)

    i_name = ''.join(e for e in i_name if e.isalnum())
    i_name = stemmer.stem(i_name)
    return i_name
