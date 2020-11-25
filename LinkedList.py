

#Singly Linked List - A singly linked list, in its simplest form, is a collection of nodes
#--that collectively form a linear sequence.

#Each node stores a reference to an object that is an element of that sequence, 
#--as well as a reference to the next node of the list

#Linked together by pointers

#Head - The list instance maintans a member named head that identifies the first node of the list
#Tail - In some applications another member named tail that identifies the last node of the list
#First node - Head ---- Last node - Tail
#We can identify the tail as the node having None as its next reference
#TRAVERSING - This process of going through the nodes and checking them is called TRAVERSING the linked list
#Each node is represented as a unique object, with that instance storing a reference to its element and a reference to the next node (or None)

#Inserting an element at the head of a singly linked list
#--An important property of a linked list is that it does not have a predetermined fixed size
#--It uses space proportionally to its current number of elements

#INSERT/ADD a new element at the head of the list:
    #We create a new node
    #Set the data of new-node to the new_element
    #Set the new-node's reference link to refer to the current head
    #Set the list's head to point to the new node         

#We can also INSERT/ADD an element at the tail of the list, provided we keep a reference to the tail node
    #Create a new node
    #Assign its next reference to None
    #Set the next-reference of current-tail to point to this new node
    #Then update the tail reference itself to this new node

#REMOVING an element from the head of a singly linked list is essenitally the reverse operation of inserting a new element at the head

#We cannot easily delete the last node of a singly linked list 
#Even if we maintain a tail reference directly to the last node of the list, we must be able to access the node before the last node in order to remove the last node 
#But we cannot reach the node before the tail by following next links from the tail
#If we want to support such an operation efficiently, we will need to make out list doubly linked

#Learned about add/remove elements in singly linked lists

#Pros:
#Constant time insertions and deletions in any positions.
#They can also continue to expand without space 
#whereas Arrays will always require linear time complexity
#whereas Arrays (dynamic) need to create a new array with twice capacity 

#Cons:
#To access an element need to take O(k) time to go from head to kth element
#whereas arrays have constant time access

#IMPLEMENTING a NODE class and create a Singly linked list

class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c 


#------------------------------------------
#DOUBLY LINKED LISTS

#In a doubly linked list, we define a linked list in which each node keeps an explicit reference 
#--to the node before it AND a reference to the node after it.
#These lists allow a greater variety of constant-O(1)-time update operations, including insertions and deletions
#We continue to use the term "next" for the reference to the node that follows another
#We have a new term "prev" for  reference to the node that precedes it.

#Sentinel Nodes
#We add special nodes at both ends of the list
# A 'header' node at the beginning of the list
# A 'trailer' node at the end of the list
# These 'dummy' nodes are known as 'sentinels' or 'guards'

#INSERTION
#Every insertion into our doubly linked list representation will take 
#--place between a pair of existing nodes
#When a new_element is inserted at the front of the sequence, we will simply 
#--add the newNode BETWEEN the-header AND the-node-that-is-currently-after-the-header

#DELETION
#The two neighbors of the node-to-be-deleted are linked directly to each other
#As a result, that node will no longer be considered part of the list and it can be reclaimed by the system
#Because of sentinels, the same implementation can be used when deleting the first or the last element of a sequence

#IMPLEMENTATION of DOUBLY LINKED LIST

class DoublyLinkedListNode(object):
    
    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.prev_node = None
a.next_node = b
b.prev_node = a
b.next_node = c
c.next_node = None
c.prev_node = b


#---------------------------------------------------------------------------------------
#Linked Lists INTERVIEW PROBLEMS
#---------------------------------------------------------------------------------------


# ------ Singly Linked List Cycle Check -----------
#Given a singly linked list, write a function which takes in the first node in a singly 
#linked list and returns a boolean indicating if the linkedlist contains a "cycle"
#--A cycle is when a node's next point actually points back to a previous node in the list.
#This is also sometimes known as a circular linked list


#To solve this problem, we will have two 'markers' traversing through the list - 'marker1' and 'marker2'
#We will have both markers begin at the first node and traverse through the linked list
#However, the marker2 will move two nodes ahead for every one node that marker1 moves
#By this logic, eventually the marker2 will overlap with marker1 and they will equal each other
#If there is no cycle then marker2 should be able to continue to the end, never equaling the first marker

class SLLNode(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None


def cycle_check(node):

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True

    return False


# ------ Linked List Reversal -----------
#Write a function to reverse a linked list in place. 
#The function will take in the head of the list as input and return new head of list
#Want to do this in place

#Since we want to do this in place, we want to make the function operate in O(1) space
#--meaning we don't want to create a new list, so we will simply use the current nodes
#Time wise, we can perform the reversal in O(n) time

#We can reverse the list by changing the next pointer of each node. 
#Each node's next pointer should point to the previous node

#In one pass from head to tail of our input list, we will point each node's next
#...pointer to the previous element

class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None


def reverse (head):
    #Set up current, previous, and next nodes
    current = head
    prevnode = None
    nextnode = None

    while current:          #while current (head) is-not-equal-to None
        
        nextnode = current.nextnode   #copy to save
        current.nextnode = prevnode
        
        prevnode = current
        current = nextnode

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

print(reverse(a))


# ------ Linked List Nth-to-Last Node -----------

class Node(object):
    
    def __init__(self,value):
        self.value = value
        self.nextnode = None

def Nth_to_last(n, head_node):

    left_pointer = head_node
    right_pointer = head_node

    for x in range(n-1):

        #Edge Case - if there are not enough nodes. 
        if not right_pointer.nextnode:  #if it's not null basically
            raise LookupError('Error: n is larger than the linked list')

        right_pointer = right_pointer.nextnode
    
    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer




