import os



def parse(sentence = 'I like a green round table apple jam .'):

    os.popen("echo '"+sentence+"' > ~/stanfordtemp.txt")
    parser_out = os.popen("/home/10634436/Documents/recipe/recipesproject/comp/stanford-parser-2012-11-12/lexparser.sh ~/stanfordtemp.txt").readlines()

    copen = 0
    out = ''
    for i in parser_out:

        print i

        i2 = i.strip()
        copen += i2.count("(")
        copen -= i2.count(")")
        out += i2
        if copen== 0:
            break

    return out


def fire(parse):
    i = 5


print parse()