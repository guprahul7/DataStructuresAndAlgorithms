
#Low level arrays - Dynamic Arrays
#Lists - Tuples - Strings  ---- #all support indexing
#slicing lists don't create new objects - they just reference 
#Shallow copy - references the same elements in the original list
#Deep copy = contents of list are mutable, meaning a new list with new elements, 

#Dynamic Array - don't need to specify how large an array is. Keeps chunks of storage for arrays. 
# You can change the size of the array

#Create new array B - Store elements of A in B - reassign reference A to new array
#How large of new array to create - common rule is twice-the-capactiy of the existing array-that-has-been-filled

#-----------------------------------------------------------------------
#Implementing Dynamic Array - Dynamic Array Exerciese

#using ctypes as a raw array-holder

# class M(object):
    
#     def public(self):
#         print('use tab to see me')

#     def _private(self):
#         print ('you wont be able to tab to see me')
# m = M()
# print(m._private())
# print(m.public())
    
import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0          #count of elements in the array
        self.capacity = 1   #array capacity, default is 1
        self.A = self.make_array(self.capacity) #using make_array function to make array of default capacity 1

    def __len__(self):  #to return number of elements stored in the array
        return self.n

    def __getitem__(self,k):    #return the elements at index k.
        if not 0 <= k <= self.n:
            return IndexError('k is out of bounds')
        return self.A[k]

    def append(self,elem):      #appending element to array
        if self.n == self.capacity:    #if count = capacity, then resize to double capacity
            self._resize(2*self.capacity) #2x if capacity isn't enough

        self.A[self.n] = elem    #adding element to array, at position self.n 
        self.n +=  1            #since self.n is occupied, now incrementing it
    
    def _resize(self,new_cap):      #making new array B with new capacity
        B = self.make_array(new_cap)

        for k in range(self.n):     #copying array A to B
            B[k] = self.A[k]
        
        self.A = B             #assigning B back to A
        self.capactiy = new_cap #making the capacity to newcapacity

    def make_array(self, new_cap): #returns an array with the new_cap capacity
        return (new_cap * ctypes.py_object)() #ctypes library makes the raw array

arr = DynamicArray()
arr.append(1)
print(len(arr))
arr.append(2)
print(len(arr))
print(arr[0],arr[1])


#AMORTIZATION 
#Algorithm of appending 
#--Allocate memory for a larger array of size(typically twice) the old array
#--Copy contents of old array to new array
#--Free the old array
#Complexity of O(1), only cost is at doubling which reduces for larger array sizes



#-----------------------------------------------------------------------



#Interview questions are not like theory array questions
#check if two strings are anagrams or not
#anagrams - strings w same number of letters
import re  

string1 = 'clint eastwood'
string2 = 'old west actions'

#-- Method 1 -- use a dictionary to count # of times seen

#Clean up strings
s1 = string1.replace(' ','').lower()
s2 = string2.replace(' ','').lower()

#edge case check
if len(s1) != len(s2):
    isAnagram = 0
# for x in s1:
#     if x not in s2:
#         isAnagram = 0

count = {}

for x in s1:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1  
    print(count)

for x in s2:
    if x in count:
        count[x] -= 1
    else:
        count[x] = 1

for k in count:
    if count[k] != 0:
        print('false')

# #Method 2
# string1 = 'clint eastwood'
# string2 = 'old west action'
# string1 = string1.replace(' ','').lower()
# string2 = string2.replace(' ','').lower()

# if sorted(string1) == sorted(string2):
#     print('Yes Anagrams')
# else:
#     print('No not anagrams')


#My method
# def Anagram_Check(str1, str2):
#     isAnagram = 1 
#     for x in str1:
#         if x not in str2:
#             isAnagram = 0
#         else:
#             if len(re.findall(x,str1)) != len(re.findall(x,str2)):
#                 if x != ' ':
#                     isAnagram = 0
#             else:
#                 continue
                
#     if isAnagram:
#         print('Yes, anagrams')
#     else:
#         print('No, not anagrams')

#Anagram_Check(string1,string2)



#re.findall(pattern, phrase) - wherever it finds pattern, it puts it in a list and returns list
#sorted(list) - sorts 
#sorted(string) - (for strings, it sorts and returns individual letters in a list)


# ---------------------------------------------------------


#Given an integer array, output all UNIQUE pairs that sum up to a specific value k

#Using two sets -- one for seen, one for target
def pair_sum(arr, k):

    #edge case check
    if len(arr)<2:
        return None

    #Sets for tracking - if element already exists in set, it will not add it.  
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num,target),max(num,target)) )
    
    print(output, ' ' , len(output))

pair_sum([1,3,2,2], 4)



# ---------------------------------------------------------

#Given two arrays - check for the missing numbers

#Method 1 -- sum and difference
# def finder(arr1, arr2):
#     num = sum(arr1) - sum(arr2)
#     print(num, ' is the missing number')

#finder([1,2,3,4,5,6,7] , [3,7,2,1,4,6])

# --- Method 2 -- sort and zip
# def finder2(arr1,arr2):
#     arr1.sort()
#     arr2.sort()
#     for num1, num2 in zip(arr1,arr2):
#         if num1 != num2:
#             return num1
#     return arr1[-1]

# x = [1,2,3,4,5,6,7,8]
# y =  [3,7,2,1,4,6,5]
# print(x.sort(),'\n', y.sort())
# z = list(zip(x,y))
# print(z)


# ---- default dict - normal python dictonary where if key does not already exist, it will add the key
#learn a little bit about default dict
import collections
def finder3(arr1,arr2):
    d = collections.defaultdict(int) 

    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num]==0:
            return num
        else: d[num] -= 1
        
    print(d.items())

finder3([1,2,3,4,5,6,7],[3,7,2,1,4,6])


# -- XOR approach -- (hv to look into this)
#list1+list2 will simply concatenate values of list1 and list2
def finder4(arr1,arr2):
    result = 0
    
    #perform XOR between numbers in array
    for num in arr1+arr2:
        result ^= num
        print(result)

    print(result)

finder4([1,2,3,4,5,6,7] , [3,7,2,1,4,6])


# ---------------------------------------------------------

#Largest Continuous Sum
#Given an array of integers (pos and neg), find the largest continuous sum

def large_cont_sum(arr):
    if len(arr) == 0:
        return 0
    
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)
    
    return (max_sum)


# ---------------------------------------------------------

#--- Sentence Reversal -------

x = '   this is    the best   '
lst = x.split()
lst = lst[-1::-1]
print(lst)

def reverse_word(s):
    words = []
    length = len(s)
    spaces = [' ']

    i=0
    while i < length:

        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i+=1

            words.append(s[word_start:i])

        i += 1

    return " ".join(reversed(words)) #.join method is useful
             

# ---------------------------------------------------------

#String Compression 

#Using Hashtable
s = ''.join(sorted(string_sorted))
r = ''
count = {}
for x in s:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

for x in count:
    r = r + str(x) + str(count[x])

print(r)


# -- Compress a string -- using iterable
def compress(s):
    r = ''
    length = len(s)

#Edge Case Check
    if l == 0:
        return ''
    if l == 1:
        return s+'1'
    
    #last = s[0]
    cnt = 1
    i = 1  #to start at second string

    while i < length:
        if s[i] == s[i-1]: #compare current-term and before-term
            cnt +=1        #if equal increase count
        else:                   #if not equal add it to string
            r = r + s[i-1] + str(cnt)   #the term + the count
            cnt = 1                 #reset count for new term

        i += 1              #move to next term
    r = r + s[i-1] + str(cnt)   #for last sequence of terms, #as last sequence 
                                #otherwise would not enter else-loop and wouldn't be counted

    return r

# ---------------------------------------------------------

#Unique characters in a string
def unique(s):
    d = {}
    for x in s:
        if x in d:
            print('False') #return False
        else:
            d[x] = 1
    print('true')

# s = 'abcdee'
# unique(s)


def uni_char(s):
    if len(set(s)) == len(s):
        print('True')
    else:
        print('False')

def uni_char2(s):
    chars = set()
    for x in s:
        if x in chars:
            return False
        else:
            char.add(x)  #.add() function for set.
    return True


    #UNIQUE - sets, tuples, dictionary
    #set - to update/ have one occurence 
    #dict  - to keep count
    #tuple - can't modify



#==================