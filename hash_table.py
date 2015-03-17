import random

class hashtable():
    def __init__(self, M):
        self.table = [0]*M
        for i in xrange(0, M):
            self.table[i] = []
    def __getitem__(self, key):
        index = hash(key) % M
        hits = [v for k, v in self.table[index] if k == key]
        if len(hits) >= 1:
            return hits[len(hits)-1]
        else:
            raise KeyError(key)
    def __setitem__(self, key, value):
        index = hash(key) % M
        self.table[index].append((key, value))
    def __str__(self):
        return str(self.table)
        
N = 10000
array_size = random.randint(1, N)
S = [(random.choice(range(0, N)), random.choice(range(0, N))) for _ in xrange(array_size)]

for n in xrange(1, 10):
    M = n*N
    table = hashtable(M)
    dictionary = dict()
    for k, v in S:
        table[k] = v
        dictionary[k] = v
    print table
    for k, v in S:
        print "table[%s] = %s, expecting %s" % (k, table[k], dictionary[k])
        assert(table[k] == dictionary[k])

