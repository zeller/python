import random

class circular_array(list):
    def __init__(self, N=100):
        number_space = range(0, N)
        array_size = random.randint(1, N)
        break_point = random.randint(0, array_size)
        a = sorted([random.choice(number_space) for _ in xrange(array_size)])
        a = a[break_point:] + a[:break_point]
        super(circular_array, self).__init__(a)

def binary_search(a, x, start=0, stop=None):
    if stop is None: stop = len(a)
    print "Searching from indexes %s to %s for %s in %s" % (start, stop, x, a)

    while start < stop:
        mid = start+(stop-start)//2
        print "start = %s, stop = %s, mid = %s" % (start, stop, mid)
        if a[mid] < x:
            start = mid + 1
        else:
            stop = mid

    if a and a[start] == x:
        return start
    else:
        return None

def break_point(a):
    if not isinstance(a, circular_array):
        raise Exception("Not a circular_array!")
    if len(a) == 0:
        raise Exception("Cannot find break point of empty circular_array!")
    if len(a) == 1 or a[0] < a[len(a) - 1]: return 0

    print "Searching for break point in circular array %s" % a

    start = 0
    stop = len(a) - 1
    while stop >= start:
        mid = (start + stop) // 2
        print "start = %s, stop = %s, mid = %s" % (start, stop, mid)
        if start == stop:
            return mid
        elif a[mid - 1] > a[mid]:
            return mid
        elif a[mid] > a[mid + 1]:
            return mid + 1
        elif a[mid] == a[start] and a[mid] == a[stop]:
            start = start + 1
        elif a[mid] > a[stop]:
            start = mid + 1
        else:
            stop = mid - 1
    assert(False)

for i in range(1, 10000):
    a = circular_array(10)

    bp = break_point(a)
    print "break_point = %s, a[break_point] = %s" % (bp, a[bp])
    test_point = random.randint(1, len(a)) - 1
    print "test_point = %s" % test_point
    s = a[bp:] + a[:bp]
    print "Sorted = %s" % s
    assert(sorted(s)==s)
    index = binary_search(s, s[test_point])
    print "Found %s at %s" % (s[index], index)
    assert(s[index]==s[test_point])
