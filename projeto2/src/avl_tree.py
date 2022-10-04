#!/usr/bin/env python3

import csv
from anytree import NodeMixin, RenderTree
from anytree.exporter import DotExporter
from anytree.dotexport import RenderTreeGraph
import datetime


# Python code to insert a node in AVL tree

# Generic tree node class
class TreeNode(NodeMixin):
    def __init__(self, name, parent=None):
        super(TreeNode, self).__init__()
        self.name = name
        self.left = None
        self.right = None
        self.treeHeight = 1
        self.parent = parent
        self.count = 1




# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key, parent=None)
        elif key == root.name:
            root.count += 1
        elif key < root.name:
            root.left = self.insert(root.left, key)
            root.left.parent = root
        else:
            root.right = self.insert(root.right, key)
            root.right.parent = root
        # Step 2 - Update the treeHeight of the
        # ancestor node
        root.treeHeight = 1 + max(self.getTreeHeight(root.left),
                              self.getTreeHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.name:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.name:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.name:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.name:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left



        # Perform rotation
        y.left = z
        z.right = T2

        #set the parents
        y.parent = None
        if z:
            z.parent = y
        if T2:
            T2.parent = z



        # Update treeHeights
        z.treeHeight = 1 + max(self.getTreeHeight(z.left),
                           self.getTreeHeight(z.right))
        y.treeHeight = 1 + max(self.getTreeHeight(y.left),
                           self.getTreeHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        y.parent = None
        if z:
            z.parent = y
        if T3:
            T3.parent = z
        # set the parents



        # Update treeHeights
        z.treeHeight = 1 + max(self.getTreeHeight(z.left),
                           self.getTreeHeight(z.right))
        y.treeHeight = 1 + max(self.getTreeHeight(y.left),
                           self.getTreeHeight(y.right))

        # Return the new root
        return y

    def getTreeHeight(self, root):
        if not root:
            return 0
        return root.treeHeight

    def getBalance(self, root):
        if not root:
            return 0
        return self.getTreeHeight(root.left) - self.getTreeHeight(root.right)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.name, root.parent), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def search(self, key, root):
        if not root:
            return
        if key == root.name:
            return root
        self.search(key,root.left)
        self.search(key,root.right)


# Driver program to test above function
if __name__ == '__main__':
    jsonArray = []
    # read csv file
    with open('../hr-employee-attrition.csv') as f:
        reader = csv.reader(f)
        next(reader)
        lst = list(reader)

    #ordering by id
    print("Indexing by ID")
    myTree = AVL_Tree()
    root = None
    for line in lst:
        value = line[0]
        root = myTree.insert(root, value)
    for pre, _, node in RenderTree(root):
        treestr = u"%s%s" % (pre, node.name)
        print(treestr.ljust(8))

    #exports picture of the tree
    DotExporter(root).to_dotfile("../files/AvlTree.dot")
    RenderTreeGraph(root).to_picture("../files/AvlTree.png")


    #print the Age and the count of people with same age.
    for pre, _, node in RenderTree(root):
        treestr = u"%s%s" % (pre, node.name)
        print(treestr.ljust(8), node.count)

    #altura da arvore
    print(root.treeHeight)

    #search
    print("busca ",dir(myTree.search("40", root)))










