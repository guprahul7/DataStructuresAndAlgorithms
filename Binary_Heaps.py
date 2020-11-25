
#===================#===================#===================#===================

#====== Priority Queues with Binary Heaps ==========
#One important variation of a queue is called a prioirty queue
#A priority queue acts like a queue in that you dequeue an item by removing it from the front
#However, in a priority queue the logical order of items inside a queue is determined by their priority
#--The highest priority items are the front of the queue
#--The lowest priority items are at the back
#When you enqueue an item on a priority queue, the new item may move all the way to the front

#The classic way to implement a priority queue is using a data structure called a binary heap
#A binary heap will allow us both enqueue and dequeue items in O(logN)
#--The binary heap has two common variations:
    #   Min Heap - smallest key always at front
    #   Max Heap - larget key always at front

#-------- IMPLEMENTING a MIN HEAP in this example --------
#Basic Operations for our Binary Heap
#   BinaryHeap() creates a new, empty, binary heap
#   insert(k) adds a new item to the heap
#   findMin() returns the item with the minimum key value, leaving item in the heap
#   delMin() returns item with minimum key value, removing item from the heap
#   isEmpty() returns true if the heap is empty, false otherwise
#   size() returns the number of items in the heap
#   buildHeap(list) builds a new heap from a list of keys


#In order to make our heap work efficiently, we will take advantage of the logarithmic nature of the binary tree to represent our heap
#In order to guarantee logarithmic performance, we must keep our tree balanced
#A balanced binary tree has roughly the same number of nodes in the left and right subtrees of the root
#In our heap implementation we keep the tree balanced by creating a complete binary tree    
#A complete binary tree is a tree in which each level has all of its nodes.
  

#An entire binary heap can be represented by a single list, 
#The constructor will initialize a list and an attribute current size

class BinHeap:              #begin implementation by a simple constructor
    def __init__(self):
        self.heapList = [0] #has a single 0 as the first element for integer division purposes
        self.currentSize = 0


#Insert it the heap  

def percUp(self, i):
    while i//2 > 0:
        if self.heapList[i] < self.heapList[i//2]:
            tmp = self.heapList[i//2]               #these three instructions are for swapping the variable with the parent
            self.heapList[i//2] = self.heapList[i]
            self.heapList[i] = tmp
        i = i//2

def insert(self,k):
    self.heapList.append(k)
    self.currentSize = self.currentSize + 1
    self.percUp(self.currentSize )


#======= Needs Review!!! BINARY HEAP INCOMPLETE -- Read the notebook/watch again, and study =======================


