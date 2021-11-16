#!/usr/bin/env python3

#####
### Main function definition
#####

def main():
    print("haha")

if __name__ == "__main__":
    main()

#####
### Tree and Node definition
#####

class Node:
    def __init__(self, key):
        self.p = None
        self.right = None
        self.left = None
        self.key = key

class Tree:
    def __init__(self):
        self.root = None

#####
### BST functions
#####

### Insertion
def insert(tree, key):
    if tree == None:
        tree = Node(key)
    elif tree.key > key:
        tree.right = insert(tree, key)
        tree.right.p = tree
    elif tree.key < key:
        tree.left = insert(tree, key)
        tree.left.p = tree
    return tree

### Deletion
def delete(tree, key):
    tree = find(tree, key)
    if tree == None:
        raise ValueError("Delete key not in tree.")
    elif tree.left == None: # no left child
        tree.p = transplant(tree.p, tree, tree.right)
    elif tree.right == None: # just a left child
        tree.p = transplant(tree.p, tree, tree.left)
    else: # two children




### Transplant
def transplant(tree, oldRoot, newRoot):
    pass

### Search
def search(tree, key):
    find(tree, key) != None

def find(tree, key):
    if tree == None or tree.key == key:
        return tree
    elif tree.key > key:
        search(tree.right, key)
    else:
        assert tree.key < key
        search(tree.left, key)

### Max
def max(tree):
    if tree == None:
        raise IndexError("Max of empty tree.")
    elif tree.right == None:
        return tree
    else:
        max(tree.right)

### Min
def min(tree):
    if tree == None:
        raise IndexError("Min of empty tree.")
    elif tree.left == None:
        return tree
    else:
        min(tree.left)


### Predecessor
def predecessor(tree, key):
    tree = find(tree, key)
    if tree == None:
        raise ValueError("Predecessor of value not in tree")
    else:
        assert tree.key == key
        if tree.left == None:
            while tree.p.left == None or tree.p.left.key != tree.k:
                if tree.p.p == None:
                    raise ValueError("Predecessor of minimum value")
                else:
                    tree = tree.p
            return tree.p.key
        else:
            assert tree.left != None
            max(tree.left)

### Successor
def successor(tree, key):
    tree = find(tree, key)
    if tree == None:
        raise ValueError("Predecessor of value not in tree")
    else:
        assert tree.key == key
        if tree.right == None:
            while tree.p.right == None or tree.p.right.key != tree.k:
                if tree.p.p == None:
                    raise ValueError("Predecessor of minimum value")
                else:
                    tree = tree.p
            return tree.p
        else:
            assert tree.right != None
            min(tree.right)

## Inorder
def inorder(tree):
    if tree != None:
        inorder(tree.left)
        print(tree.key + ", ")
        inorder(tree.right)
