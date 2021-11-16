import random
import math

class Node:

    def __init__(self,key):
        self.p = None
        self.right = None
        self.left = None
        self.key = key


class Tree:
    root = None

    def __init__(self):
        self.root = None



#### QUERY OPERATIONS ON THE TREE ####

def TreeSearch(x,k):
    if x == None or x.key == k:
        return x
    if k < x.key:
        return TreeSearch(x.left, k)
    else:
        return TreeSearch(x.right, k)


def TreeMinimum(x):
    while x.left != None:
        x = x.left
    return x


def TreeMaximum(x):
    while x.right != None:
        x = x.right
    return x


def TreeSuccessor(x):
    if x.right != None:
        return TreeMinimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        y = y.p
    return y


def TreePredecessor(x):
    if x.left != None:
        return TreeMaximum(x.left)
    y = x.p
    while y != None and x == y.left:
        x = y
        y = y.p
    return y


def InorderTreeWalk(x):
    if x != None:
        InorderTreeWalk(x.left)
        print(x.key, end=" "),
        InorderTreeWalk(x.right)



def PreorderTreeWalk(x):
    if x != None:
        print(x.key, end=" "),
        PreorderTreeWalk(x.left)
        PreorderTreeWalk(x.right)

def PostorderTreeWalk(x):
    if x != None:
        PostorderTreeWalk(x.left)
        PostorderTreeWalk(x.right)
        print(x.key, end=" "),




#### MODIFYING OPERATIONS ####


def Insert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z


def Transplant(T,u,v):
    if u.p == None:
        T.root = v
    else:
        if u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
    if v != None:
        v.p = u.p

def TreeDelete(T,z):
    if z.left == None:
        Transplant(T, z, z.right)
    else:
        if z.right == None:
            Transplant(T, z, z.left)
        else:
            y = TreeMinimum(z.right)
            if y.p != z:
                Transplant(T, y, y.right)
                y.right = z.right
                y.right.p = y
            Transplant(T, z, y)
            y.left = z.left
            y.left.p = y


def build_tree(a_list, i, j, x,  parent):
    if i <= j:
        q = math.ceil((j+i)/2)
        x.p = parent
        x.key = a_list[q]
        if i <= q-1:
            x.left = Node('END')
        if q+1 <= j:
            x.right = Node('END')
        build_tree(a_list, i, q-1, x.left, x)
        build_tree(a_list, q+1, j, x.right, x)



if __name__ == "__main__":
    T = Tree()
    T1 = Tree()
    # Insert(T, Node('J'))
    # Insert(T, Node('E'))
    # Insert(T, Node('A'))
    # Insert(T, Node('D'))

#    print(random.sample(range(20), 10))
#    L = [5, 12, 8, 1, 19, 2, 9, 14, 13, 3]
    L2 = [11, 8, 1, 6, 4, 12, 19, 10, 9, 13]
    for i in range(10):
       Insert(T, Node(L2[i]))
 #      Insert(T1, Node(L[i]))

    #res = TreeSearch(T.root, 2)
    #if res != None:
#		print 'Found an element of key ', res.key
#	else:
#		print 'No element found'

#	print 'Minimum of tree is ', TreeMinimum(T.root).key
#	print 'Maximum of tree is ', TreeMaximum(T.root).key

#	print 'Successor of', T.root.key, ' is ', TreeSuccessor(T.root).key
#	print 'Successor of ', T.root.left.right.key, ' is ', TreeSuccessor(T.root.left.right).key

#	print 'Predecessor of', TreeSuccessor(T.root).key, ' is ', TreePredecessor(TreeSuccessor(T.root)).key
#	print 'Predecessor of', TreeSuccessor(T.root.left.right).key, ' is ', TreePredecessor(TreeSuccessor(T.root.left.right)).key

    print('\nInorder:')
    InorderTreeWalk(T.root)
    #
    #
    # #InorderTreeWalk(T.root)
    print('\n\nPreorder:')
    PreorderTreeWalk(T.root)
    print('\n\nPostorder:')
    PostorderTreeWalk(T.root)
    # TreeDelete(T, T.root)
    # print('Preorder')
    # PreorderTreeWalk(T1.root)
    print('\n\nThat is all folks.')
    #root = Node('End')
    #parent = None
    #build_tree(['NA', 1, 2, 3, 4, 5, 6, 7, 8], 1, 8, root, parent)
    #PreorderTreeWalk(root)

