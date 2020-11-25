
#Tree Data Structure and ADT - Abstract Data Types
#Implement Trees  with Lists
#Implement Trees using OOP 
#Implement Priority Queue
#Interview Problems

#----- PROPERTIES -----
#-A tree data structure has a ROOT, BRANCHES, and LEAVES
#-Has ROOT at TOP and LEAVES on BOTTOM
#-All the children of one node are independent of the children of another node
#-Each leaf node is unique
#-Example: a file system, directories/folders/files

#------ NODE ------ (name of node = key, info in node = payload)
#-A node is a fundamental part of a tree. 
#...it can have a NAME - which we we call the "key"
#-A node may also have additional information -- aka "payload"
#-While the payload information is not central to many tree algorithms,
#...it is often ctitical in applications that make use of trees

#------ EDGE ------ (edges connect nodes - a node can only have 1 incoming edge - but may have several outgoing edges)
#An edge is another fundamental part of a tree
#An edge connects two nodes to show that there is a relationship between them
#Every node (except the root) is connected by exactly one incoming edge from another node
#Each node may have several outgoing edges 

#------ PATH ------ (nodes connected by edges)
#A path is an ordered list of nodes that are connected by edges
#For example: Mammal -> Carnivora -> Felidae -> Felis

#------ CHILDREN ------
#The set of nodes "c" that have incoming edges from the same node are said to be children of that node
#(my understanding - children can be thought of as the pointers to the outgoing nodes )

#------ PARENT ------
#A node is the parent of all the nodes it connects to with outgoing edges

#------ SIBLING ------
#Nodes in the tree that are children of the same parent are said to be siblings

#------ SubTREE ------
#A SubTree is a set of nodes and edges comprised of a parent and all the descendants of that parent

#------ LEAF NODE ------
#A leaf node is a node that has no children 

#------ LEVEL ------
#The level of a node "n" is the number of edges on the path from the root node to n.

#------ HEIGHT ------
#The height of a tree is equal to the maximum level of any node in the tree

#Full definition of a Tree
#- A tree consists of a set of ndoes and a set of edges that connect pairs of nodes. 
#----A tree has the following propoerties:----
#One node of thre tree is designated as the root node.
#Every node n, except the root node, is connected by and edge form exactly oen other node p, where p is the parent of n
#A unique path traverses from the root to each node
#If each node in the tree has a maximum of two children, we say that the tee is a binary teee

#Recursive Definition of a tree
#--A tree is either empty or consists of A-root and zero-or-more Subtrees, each of which is also a tree
#The root of each subtree is connected to the root of the parent tree by an edge





#---------- TREE - LIST of LISTS IMPLEMENTATION------------------
# Basic: Representing Tree as a LIST of LISTS -> [ [ ], [ ], [ ] ]
#In a list-of-lists tree, we will store the value of the root node as the first element of the list
#The second element of the list will itself be a list that represents the left subtree
#The third element of the list will be another list the represents the right subtree

def BinaryTree(r):              
    return [ r, [], [] ]

def insertLeft(root,newBranch):    #To  insert a left child, we first obtain a list (which could possibly be empty) that corresponds to the current left-child
    t = root.pop(1)                #Then, we add the new-left-child, installing the current-left-child as the left-child of the new one. 
                                    #This is basically allowing us to splice a new node into the tree at any position
    if len(t) > 1:
        root.insert(1,[ newBranch, t, [] ]) 
    else:
        root.insert(1, [ newBranch, [], [] ])

    return root


def insertRight(root,newBranch):    #To  insert a left child, we first obtain a list (which could possibly be empty) that corresponds to the current left-child
    t = root.pop(2)                #Then, we add the new-left-child, installing the current-left-child as the left-child of the new one. 
                                    #This is basically allowing us to splice a new node into the tree at any position
    if len(t) > 1:
        root.insert(2,[ newBranch, [], t ]) 
    else:
        root.insert(2, [ newBranch, [], [] ])

    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]
    
# #------------Example Trying Stuff Out-----------------
# r = BinaryTree(3)
# print(r)
# #insertLeft(r,4)
# print(insertLeft(r,4))

# x = ['rootX',  ['leftX',[], [] ],   ['rightX', [], [] ]   ]

# y = ['root',  ['leftY'],   ['rightY', [], [] ]   ]

# a = x.pop(1)
# print(a)
# print(x)
# if len(a) > 1:  #has more branches, not the only leaf
#     x.insert(1, ['newBranchX', a, [] ] )
# else:
#     x.insert(1, ['newBranchX', [], [] ] )
# print(x)

# print('\n')

# b = y.pop(1)
# print(b)
# print(y)
# if len(b) > 1:  #has more branches, not the only leaf
#     y.insert(1, ['newBranchY', b, [] ] )
# else:
#     y.insert(1, ['newBranchY', [], [] ] )
# print(y)

# #-------------------------------------------------------






#=================== TREE - OOP -> Nodes and References ===============================
#We define a class that has attributes for the root value, and the left and right subtrees
#Use this method for the remainder of the section

class BinaryTree(object):
    #The attributes left and right will become references to other instances of the binary tree
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:  #if there is no left child
            self.leftChild = BinaryTree(newNode)    #we create a new-tree with given node and make it the leftChild of the root
        else:               #if there already is a left child, we want to make it the left-child of the new left-child
            newLeft = BinaryTree(newNode) #so we create a new left-child tree
            newLeft.leftChild = self.leftChild    #we make the current-leftchild as the left-child of this new-left-child
            self.leftChild = newLeft  #We assign the new leftChild to be the current left-child
        
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            newRight = BinaryTree(newNode)
            newRight.rightChild = self.leftChild
            self.rightChild = newRight

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())

r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())

#===================#===================#===================#===================

#================ TREE - OOP -> Nodes and References ===============================
#We define a class that has attributes for the root value, and the left and right subtrees
#Use this method for the remainder of the section

class BinaryTree(object):
    #The attributes left and right will become references to other instances of the binary tree
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:  #if there is no left child
            self.leftChild = BinaryTree(newNode)    #we create a new-tree with given node and make it the leftChild of the root
        else:               #if there already is a left child, we want to make it the left-child of the new left-child
            newLeft = BinaryTree(newNode) #so we create a new left-child tree
            newLeft.leftChild = self.leftChild    #we make the current-leftchild as the left-child of this new-left-child
            self.leftChild = newLeft  #We assign the new leftChild to be the current left-child
        
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            newRight = BinaryTree(newNode)
            newRight.rightChild = self.leftChild
            self.rightChild = newRight

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())

r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())

#===================#===================#===================#===================

#---------- TREE TRAVERSALS ------------
#Name in order w.r.t ROOT node.
# PRE ORDER - visit root first, then left subtree, then right subtree
# ... we visit the root node first, then recursively do a preorder traversal of the left subtree, followed by a recursive preorder traversal of the right subtree
# IN ORDER - visit left subtree first, then root, then right subtree
# ... we recursively do an inorder traversal on the left subtree, visit the root node, and finally do a recursive inorder traversal of the right subtree
# POST ORDER - left subtree first, then right subtree, then root
# ... we do a postorder traversal of the left subtree and then right subtree followed by a visit to the root node

#Implementing as an external Function, instead of method of BinaryTree() Class 

def preOrder(tree): 
    if tree != None:                    #if tree exists
        print(tree.getRootVal())        #get the root of the tree
        preOrder(tree.getleftChild())   #Do preOrder on the leftChild of the three
        preOrder(tree.getrightChild())  #Then do preOrder on the rightChild of the three

def postOrder(tree):   
    if tree != None:                     #if tree exists
        postOrder(tree.getLeftChild())   #do postOrder on leftChild of tree
        postOrder(tree.getRightChild())  #After that do postOrder on RightChild of tree
        print (tree.getRootVal())        #Then get the value of the root of the tree

def inOrder(tree):
    if tree != None:                    #if tree exists
        inOrder(tree.getLeftChild())    #do inOrder on the leftChild of the tree
        print(tree.getRootVal())        #After that get the root of the tree
        inOrder(tree.getRightChild())   #After that do inOrder on the rightChild of the tree


#This is implementing it as a method of a class
def preOrder(self):             
    print(self.key)                 #Get root of the tree (root is used interchangeably as key)
    if self.leftChild:              #if leftChild exists:
        self.leftChild.preOrder()   #Do a recursive preOrder on it => get its leftChild and do preOrder again
    if self.rightChild:             #Same thing for RightChild
        self.rightChild.preOrder()


