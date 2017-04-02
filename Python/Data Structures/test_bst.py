#!/usr/bin/env python

import Trees as t
import random

bst = t.Trees()
#lst = [ int(1000 * random.random()) for i in xrange(20)]
lst = [2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98]

print lst
for i in lst:
    bst.root = bst.insert(i, bst.root)

print bst.root.key

bst.print_graph()

print bst.find_min(bst.root).key
print bst.find_max(bst.root).key
print bst.depth(bst.root)

bst.delete(27, bst.root)

bst.print_graph()