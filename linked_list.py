class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node

class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print node.data
            node = node.next

N = 10
array_size = random.randint(1, N)
S = [random.choice(range(0, N)) for _ in xrange(array_size)]
vals = linked_list()
for s in S:
    vals.add_node(s)

print S
print ""
vals.list_print()
    
