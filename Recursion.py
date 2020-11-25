
# ------- RECURSION -------

#Always think what the BASE CASE will look like. 
# Key to recursion problems

# ----------------------------------
#HW solution 

def sum_to_n(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    else:
        return n + sum_to_n(n-1)

#print(sum_to_n(10)) # = 55 works fine

# -------------------------------------
#HW solution
def sum_func(n):
    
    if len(str(n)) == 1:
        return n

    if n//10 == 0:
        return n%10
    else:
        return n%10 + sum_func(n//10)

#print(sum_func(345)) # returns 12 works fine

# -----------------------------------------------

#Reverse a string

def reverse_string_recursively(s):
    #Base Case
    if len(s) <= 1:
        return s
    
    return reverse_string_recursively(s[1:]) +  s[0]

# -------------------------------------------------

#MY SOLUTION
def reverse(s):
    s = list(s)
    if len(s) == 1:
        return s[0]
    else: 
        x = s.pop()
        x = x + reverse(s)
        return x

#=====================================================
#All possible Permutation of a given string 

def permute(s):
    out = []
    
    #Base Case 
    if len(s) == 1:
        out = [s]
    
    else:
        # For every permutation resulting from Step 2 and 3
        for i,letter in enumerate(s):
            for perm in permute( s[:1] + s[i+1:] ):
                print('current letter is: {}'.format(letter))
                print('perm is', perm)
                out += [letter + perm]

        return out


# #----- ENUMERATE ------
# #enumerate assigns indexes(starting from 0...) to items in an iterable object, and tuple-pairs each index with the item
# #example: x = 'ab8xn' --- enumerate(x) --- will create an enumerate object as such (0,a), (1,b), (2,8) ... 
# #doing list(enumerate(x)) will output [ (0,a),(1,b),(2,8), (3,x) , ...] etc


#=====================================================
#Fibonacci sequence in Iterative, Recursive, DynamicProgramming Way

#--ITERATIVE --
def fib_iter(n):
    a,b = 0,1

    for i in range(n):
        a,b = b,a+b

    return a  

#-------------------
#--RECURSIVE--
def fib_rec(n):
    if n==0 or n==1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

#---------------------
#DYNAMIC PROGRAMMING - MEMOIZATION
#Memoization - Using memory to save time during recursion, by storing answer in a variable to be used again in the recursion


#Cache
n = 10
cache = [None]*(n+1)

def fib_dyn(n):

    #Base Case
    if n == 0 or n==1:
        return n
    if cache[n] != None:
        return cache[n]

    #Updating Cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

    
         
