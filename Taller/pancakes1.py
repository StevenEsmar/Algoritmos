import itertools

original = []

def start(pancakes,condition):
    answer = []
    Pn = 0
    for e in itertools.permutations(pancakes):
        rta = flips(list(e))
        Pn = max(Pn,rta[0])
        answer.append([''.join(map(str,list(reversed(e)))),rta[0],''.join(map(str,rta[1]))])
    
    if condition == 0:
        print "Pn = {}".format(Pn)
    elif condition == 1:
        print "Pn = {}".format(Pn)
        for e in answer:
            if e[1]==Pn:
                print e[0],e[2]
    elif condition == 2:
        print "Pn = {}".format(Pn)
        for e in answer:
            print e[0],e[2]
    else:
        for e in answer:
            print e[0],e[1],e[2]

def flips(pancakes):
    level = []
    steps = 0
    if pancakes == original:
        return [steps,[" "]]
    while True:
        steps+=1
        level_old = level[:]
        level = []
        if steps <= 1:
            for i in xrange(len(pancakes)-1):
                pan = pancakes[:i]+list(reversed(pancakes[i:]))
                level.append([pan,[i]])
                if pan == original:
                    return [steps,[i]]
        else:
            for e in level_old:

                for i in xrange(len(e[0])-1):
                    if e[1][-1]!=i:
                        pan = e[0][:i]+list(reversed(e[0][i:]))
                        level.append([pan,e[1]+[i]])
                        if pan == original:
                            return [steps,e[1]+[i]]

N = 3
c = -1
original = range(N,0,-1)
start(original,c)
