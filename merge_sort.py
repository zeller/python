import random

def merge(a, b):
    assert(sorted(a) == a)
    assert(sorted(b) == b)
    i = j = 0
    c = []
    while True:
        if i == len(a):
            return c+b[j:]
        if j == len(b):
            return c+a[i:]
        if a[i] < b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1

def split(a): 
    return a[:len(a)//2], a[len(a)//2:]

def _mergesort(a, b):
    print "a = %s" % a
    print "b = %s" % b
    if len(a) == 1 and len(b) == 1:
        return merge(a, b)
    if len(a) == 1:
        return a
    if len(b) == 1:
        return b
    a = _mergesort(*split(a))
    b = _mergesort(*split(b))
    return merge(a, b)
    
def mergesort(a):
    return _mergesort(*split(a))

N = 100

for i in xrange(0, 10000):
    array_size = random.randint(1, N)
    a = [random.choice(range(0, N)) for _ in xrange(array_size)]
    a_sorted = sorted(a)

    a = mergesort(a)
    assert(sorted(a)==a)
