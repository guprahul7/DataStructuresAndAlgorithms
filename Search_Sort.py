
#========== SEARCH ============

#Sequential Search 
#Analysis on Ordered/Unordered List

#Sequential Search - Basic searching technique, sequentially go through the data structure, comparing elements as you go along

#Example: searching for 50
    #in an unordered list - we keep going until the end unless 50 is found
    #in an ordered list - we keep going until we reach a value greater than 50, bcoz after that 50 will not exist
    
    #Analysis:      ----- BC ----- WC ----- AvgC
    
    #Unordered:    
        #Item present      1       n        n/2
        #Item absent       n       n         n
   
    #Ordered:    
        #Item present      1       n        n/2
        #Item absent       1       n        n/2

#BASIC SEQUENTIAL SEARCHING 
def seq_search(arr, elem):
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos] == elem:
            found = True
        else:
            pos += 1
    return found

def ordered_seq_search(arr, elem):
    '''Array is Ordered'''
    pos = 0
    found = False
    stopped = False
    while pos < len(arr) and not found and not stopped:
        if arr[pos] == elem:
            found = True
        else:
            if arr[pos] > elem:
                stopped = True
            else:
                pos += 1
    return found

#=============== BINARY SEARCH (must be ordered list)==================

#----- uses DIVIDE and CONQUER -----
#Taking advantage of ordered list
#Instead of searching the list in sequence, a binary search will start by examining the middle item

#Looks at middle item
#If middle item is the search_item, we are done
#If middle item is less than the search_item, then left half of list and middle item can be eliminated from further consideration
#Item must be in upper/right half
#So we repeat the process

#for i comparisons, we have n/2^i items left

# ---- IMPLEMENTING BINARY SEARCH ---- 

def binary_search(arr,elem):
    first_index = 0
    last_index = len(arr) - 1

    found = False

    while first_index <= last_index and not found:
        
        middle = (first_index + last_index)/2
        
        if arr[middle] == elem:
            found = True
        else:
            if elem < arr[middle]:
                last_index = middle - 1
            else:
                first_index = middle + 1 
        
    return found

#arr = [1,2,3,4,5,6,7,8,9,10]
#binary_search(arr, 2)
#binary_search(arr, 13)

def rec_binary_search(arr,elem):

    #For recursive algos, need to start with base case
    if len(arr) == 0:
        return False

    else:

        mid = len(arr)/2
        if arr[mid] == elem:
            return True
          
        else:
            if elem < arr[mid]:
                return rec_binary_search(arr[ :mid-1], elem)
            else:
                rec_binary_search(arr[mid+1: ], elem)
    



#================= HASH TABLE ===================

#------ HASHING ----- uses DIVIDE and CONQUER -----
    #Hashing
    #Hash Tables
    #Hash Functions
    #Collision Resolution
    #Implementing a Hash Table 

#A hash table is a collection of items which are stored in such a way as to make it easy to find them later
#Each position of the hash table, 'slot', can hold an item and is named by an integer value starting at 0
#For example: we will have a slot named 0, a slot named 1, and slot named 2 and so on
#Initially, the hash table contains no items so every slot is empty
#We can implement a hash table by using a list with each element initialized to special Python value None

#The Mapping between an-item and the slot-where-that-item-belongs-in-the-hash-table is called the hash function
#The hash function will take any item in the collection and return an integer in the range of slot names, between 0 and m-1

#Remainder method - using modulo to give position to an item

#A hash function that maps each item to a unique slot is called a perfect hash function
#Out goal is to create a hash function that minimizes the number of collisions

#The folding method - divides the item into equal-size pieces (the last piece may not be of equal size)
# These pieces are then added together to give the resulting hash value 

#Mid Square Method  

#The word 'cat' can be thought of as a sequence of ordinal values 
ord('c')

#Collision Resolution
    #One method for resolving collisions looks into the hash table and tries to find another open slot to hold the item that caused the collision
    #We could start at the original hash value position and then move in a sequential manner through the the slots until we encounter the first slot that is empty
    #This collision resolution process is referred to as open addressing in that it tries to find the next open slot of address in the hash table
    #By systematically visiting each slot one at a time, we are performing an open addressing technique called linear probing
    #The general name for the process of looking for another slot after a collision is rehashing
    #A variation of the linear probing idea is called quadratic probing
    #Instead of using a constant 'skip' value, we use a rehash function that increments the hash value by 1,3,5,7,9...
    #This means that if the first hash value is h, the sucessive values are h+1, h+4, h+9, h+16 and so on
    
    #An alternative mthod for handling the collision problem is to allow each slot to hold a reference to a collection (or chain) of items
    #CHAINING allows many items to exists at the same location in the hash table
    #When collisions happen, the item is still placed in the proper slot of the hash table



# ------ Implementation of a Hash table -----

class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        #The actual hash function
        return key % size
        pass 

    def rehash(self,oldhash,size):
        return (oldhash+1) % size
    
    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                
                if position == startslot:
                    stop = True
                
            return data

    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data) 

h = HashTable(5)
h[1] = 'one'
h[2] = 'two'
h[3] = 'three'




#===============================

#Interview Practice - Implement binary search

def binary_search(arr, n):
       
    x = arr

    if len(arr) == 1 and arr[0] == n:
        return True, ' found at: ', 0
    
    elif len(arr) == 1 and arr[0] != n:
        return False, ' not found '

    else:
        while len(arr) >= 1:

                mid = len(arr)//2
                
                if n == arr[mid]:
                    return (True, ' found at: ', x.index(n))

                else:
                    if n < arr[mid]:
                            arr = arr[ :mid]
                    else:
                            arr = arr[mid+1: ]

        return (False, 'not found')

array = [00,10,20,30,40,50,60,70,80,90]

print(binary_search(array, 00))

    