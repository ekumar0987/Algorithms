#!/usr/bin/env python

import Trees as t
import random
import sys

bst = t.Trees()
#lst = [ int(1000 * random.random()) for i in xrange(20)]
lst = [2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98]

print lst
for i in lst:
    bst.root = bst.insert(i, bst.root)

print bst.root.key

bst.print_graph()

print "Tree Minimum", bst.find_min(bst.root).key
print "Tree Maximum", bst.find_max(bst.root).key
print "Tree Depth", bst.depth(bst.root)
print "Tree Size", bst.size(bst.root)

bst.delete(27, bst.root)

bst.print_graph()

print "Printing post order traversal..."
lst2 = [5, 4, 6, 7]
bst2 = t.Trees()
for i in lst2:
    bst2.root = bst2.insert(i, bst2.root)

#bst2.print_graph()
bst2.print_post_order(bst2.root)

print "Has path sum ", bst2.has_path_sum(18, bst2.root)

paths = []
print "Printing list paths from root to leaf", bst2.print_paths(bst2.root, paths, 0)

print "Printing nodes at level..."
list_of_lists = []
bst2.print_nodes_on_level(bst2.root, list_of_lists, 0)
print list_of_lists	

print "Mirroring tree..."
bst.mirror(bst.root)
bst.print_graph()

print "Checking if a tree is BST..."
print bst.isBST(bst.root, -sys.maxsize, sys.maxsize)
print bst2.isBST(bst2.root, -sys.maxsize, sys.maxsize)

print "Checking if 2 trees are the same..."
print bst2.sametree(bst.root, bst.root)
print bst2.sametree(bst.root, bst2.root)


	

