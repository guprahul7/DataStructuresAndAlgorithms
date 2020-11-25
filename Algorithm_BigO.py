
#------- BIG-O to compare algorithms------------ 

def sum1(n):
    ''' take input n and return sum of numbers from 0 to n'''
    final_sum = 0
    for x in range(n+1):
        final_sum += x
    return final_sum

def sum2(n):
    return (n*(n+1))/2

print(sum1(10))
print(sum2(10),'\n')

#how quickly runtime will grow based on input

#---------- BIG-O Examples --------------

#Constant O(1)

def func_constant(values):
    print(values[0],'\n')
lst = [1,2,3,4,5]
func_constant(lst)

#Constant O(n)

def func_lin(lst):
    for x in lst:
        print(x)
    print('\n')
func_lin(lst)

#Constant O(n^2)

def func_quad(lst):
    for x in lst:
        for y in lst:
            print(x)
            print(y)

    print('\n')
func_lin(lst)

#Best cases and worst cases
    #O(1) and O(n) 

#SPACE COMPLEXITY (how much space does the algorithm take)
def printer(n):
    for x in range(10):       #TIME COMPLEXTIY O(n)
        print ('Hello World') #SPACE COMPLEXTIY O(1)


#BIG O for python data structures

#LISTS - dynamic array 
# most common ops -> indexing, and assigning index position -> O(1)
#Built-in functions are faster and efficient


def method1():
    l = []
    for n in range:
        l.append(n)
        print(l)

def method2():
    l = [x for x in range(10)]
    print(l)
method2()

l = list(range(10))
print(l)