#!/usr/bin/env python

import Bnode
import os

class Bst:
    def __init__(self):
        self.head = None

    def insert(self, data):
        self.head = self._insert(self.head, data)

    def _insert(self, node, data):
        if not node:
            print "created new node", data
            new_node = Bnode.Bnode(data)
            return new_node

        if data <= node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node

    def print_pre(self):
        self._print_pre(self.head)

    def _print_pre(self, node):
        if not node:
            return

        print node.data
        self._print_pre(node.left)
        self._print_pre(node.right)

    def print_graph(self):
        #bfile = open(r"F:\Projects\Algorithms\Python\Data Structures\bst.viz", "w")
        bfile = open(r"bst.dot", "w")
        bfile.write('digraph "bst" {\n')
        self._print_graph(bfile, self.head)
        bfile.write('}')
        bfile.close()
		#os.system(r"C:\Program Files (x86)\Graphviz2.38\bin\dot F:\Projects\Algorithms\Python\Data Structures\bst.viz -Tpng -o F:\Projects\Algorithms\Python\Data Structures\bst.png")
        os.system("dot -Tpng bst.dot > output.png")

    def _print_graph(self, bfile, node):
        if not node:
            return

        if node.left:
            bfile.write('\t"' + str(node.data) + '" -> "' + str(node.left.data) + '"\n')
            self._print_graph(bfile, node.left)
        if node.right:
            bfile.write('\t"' + str(node.data) + '" -> "' + str(node.right.data) + '"\n')
            self._print_graph(bfile, node.right)














