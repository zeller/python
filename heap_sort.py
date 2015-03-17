import random

def heapify(a):
    """Create a heap from a subset of an array, in place

    """
    count = len(a)
    start = (count - 2) / 2
    while start >= 0:
        siftdown(a, start, count-1)
        start = start - 1

def siftdown(a, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        s = root
        if a[s] > a[child]:
            s = child
        if child+1 <= end and a[s] > a[child+1]:
            s = child + 1
        if s != root:
            swap(a, root, s)
            root = s
        else:
            return
            
def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    
def heapsort(a):
    length = len(a)
    heapify(a)
    print "a = %s" % a
    for i in xrange(0, length-1):
        swap(a, 0, length-1-i)
        siftdown(a, 0, length-1-i-1)
        print "i = %s" % i
        print "a = %s" % a

N = 100

for i in xrange(0, 10000):
    array_size = random.randint(1, N)
    a = [random.choice(range(0, N)) for _ in xrange(array_size)]
    a_sorted = sorted(a, reverse=True)
    heapsort(a)
    assert(a_sorted==a)
