
#Stacks - Queues - Deques
#They are linear structures
#Similar to arrays but each differs by how it adds and removes items

#----- Stacks -----
#A stack is an ordered collection of items where the addition of new items
#--and the removal of existing items always takes place at the same end
#This end is commonly referred to as the 'top'
#The opposite end is known as the 'base'
#Items stored closer to base have been in the stack the longest
#The most recently added item is the one that is in position to be removed first
#--known as LIFO - last in first out
#Provides an ordering based on lenght of time in the collection
#Newer items are near the top and older items are near the base

#Stacks are fundamentally important as they can be used to reverse the order of items.
#The-order-of-insertion is the reverse of the-order-of-removal
#examples: web browser has a back button 
# :as we navigate from webpage the URLs go to the stack

#----- IMPLEMENTATION OF STACK CLASS ------
#Properties and Methods
    #Stack abstract datatype is an ordered collection of items - LIFO - from 'top' end
    #Stack() - creates new stack that is empty - needs no parameters and returns empty stack
    #push(item) - adds new item to top of stack, takes in (item), returns nothing
    #pop(item) - removes item from top of stack, takes nothing, returns item. Stack is modified
    #peek() - returns the top item from stack but does not remove it. No param. Stack is not modified
    #isEmpty() - tests to see if stack is empty. Needs no param. Returns boolean
    #size() - returns number of items on stack. Needs no param. Returns integer

class Stack(object):

    def __init__(self):
        self.items = []  #using list as the base of a stack. List behaves very much like a stack
                         #key step
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items())

s = Stack()
print(s.isEmpty())

s.push(1)
s.push('two')
print(s.peek())

#We took advantge of built-in list datatype of python to understand and build stack


#-----------------------------------------------------------------------

#----- Queues -----
#Queue is an ordered collection of items where the addition of items happens at one end, called 'rear'
#--and the removal of existing items occurs at other end, called the 'front' 
#Addition - rear  --------- Removal - front
#As an element enters the queue, it starts at the rear and makes its way toward the front, waiting
#--until that time when it is the next element to be removed

#The most recently added item in the queue must wait at the end of the collection.
#The item that has been in the collection the longest is at the front.
#This ordering principle is called FIFO - first in first out
#ex: waiting in line for a ticket 

#----- IMPLEMENTATION OF QUEUE CLASS ------
    #Queue() - creates new queue that is empty, needs no param, returns empty queue
    #EnQueue(item) - adds item to rear of the queue. Needs item, returns nothing
    #DeQueue() - removes front item from queue. Needs item and returns nothing
    #isEmpty() - tests to see if queue is empty. Needs no param, returns boolean value
    #size() - returns number of items in queue. Needs no param, returns integer

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item) #.insert(0,item) for list inserts item at index 0
    
    def dequeue(self):
        self.items.pop()
    
    def size(self):
        return len(self.items)

q = Queue()
print(q.size()) #returns size = 0
q.enqueue(1) #adds 1 to front of list
q.enqueue(2) #adds 2 to front of list
q.dequeue()  #pops item that was put in first - so 1




#-----------------------------------------------------------------------

#----- Dequeues -----
#Dequeue - also known as a double ended queue, is an ordered collection of items (similar to queue)
#It has two ends, a front and a rear, and items remain positioned in the collection
#Unrestrictive nature of adding and removing items
#New items can be added at either the front or the rear 
#Existing items can be removed from either end
# -- This hybrid linear structure provides all the capabilities of stacks and queues in a single data structure
#Does not require enforcement of FIFO or LIFO


#----- IMPLEMENTATION OF DEQUE CLASS ------
#Items can be added and removed from either end
    #Deque() - creates new deque that is empty, needs no param, returns empty deque
    #addFront(item) - adds new item to front of the deque. Needs item, returns nothing
    #addRear(item) - adds new item to rear of the deque. Needs item, returns nothing
    #removeFront(item) - removes front item from the deque. Needs no param, returns item, deque modified
    #removeRear(item) - removes rear item from the deque. Needs no param, returns item, deque modified
    #isEmpty() - tests to see if deque is empty. Needs no param, returns boolean value
    #size() - returns number of items in deque. Needs no param, returns an integer

class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item) #add at the last index
    
    def addRear(self,item):
        self.items.insert(0,item)  #add at the first index

    def removeFront(self): #remove from the last index
        self.items.pop()

    def removeRear(self): #remove from the first index
        self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

d = Deque()
d.addFront('hello')
d.addRear('World')
print(d.size())
print( str(d.removeFront()) + ' ' + str(d.removeRear()) )
print(d.size())
print(d.isEmpty())


#-----------------------------------------------------------------------
#INTERVIEW PROBLEMS 


#Balanced Parentheses Check:
#Given a string of opening and closing parenthesis, check whether it's balanced.

def balance_check(s):
    
    #Edge case check
    if len(s)%2 != 0:
        return False
    
    opening = set('({[')
    matches = set([ ('(',')') , ('[',']') , ('{','}') ])

    stack = []  #Stack is an abstract concept - using list as a basis for stack in python

    for paren in s:             #for each parentheses in s
        
        if paren in opening:       #if it's open parenthesis
            stack.append(paren)     #append it to the list
        
        else:           #else if its closed parenthesis--
            
            if len(stack)==0:      #this is a check for closing parentheses as the first item
                return False
           
            last_open = stack.pop()     #get the most-recently-inserted open-parenthesis
            
            if (last_open,paren) not in matches:    #if mostrecentlyinserted open-parenthesis, closed parenthesis NOT in matches_set 
                return False
                 
    return len(stack) == 0

#Use of Stacks - LIFO method
#Stack is an abstract concept - using list as basis of stack



#IMPLEMENTING a QUEUE with 2 STACKS

class Queue2Stacks(object):

    def __init__(self):
        self.InStack = []
        self.OutStack = []

    def enQueue(self,item):
        self.InStack.append(item) 
    
    def deQueue(self,item):
        
        if not self.OutStack:
            while self.Instack:
                self.OutStack.append(self.InStack.pop())
        
        return self.OutStack.pop()