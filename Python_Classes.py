#print('hello ')

#print(1+2)

# Python Scope - Follows LEGB Rule
# --Local (eg. def, lambda)
# --Enclosing Function locals
# --Global
# --Built-In

# def my_func():
# 	global x
	
	
#-- OOP --
#How are we able to create our own object in python (list, set, etc) and be able to run method/attributes on it
#Class is like a blueprint that defines the nature of an object
#From classes, we can construct instances - an instance is just a specific object created on a particular class
#everything in python is an object and we can create our own objects using the class keywords

#Attributes are characteristics of an object
#Methods are operations we can perform on an object
#Methods look like functions inside of a class
#Methods are functions defined inside the body of a class -- they are used to perform operations with the attributes of an object
#Syntax for creating an attribute = self.attributeName = sth


class Sample(): #class names start with Uppercaase
	print('hi')

x = Sample()
print(type(x))

class Dog():               #Class Object Attribute
	species = "mammal"
	
	def __init__(self, breed, name): #this method is the initalize method and it refers to itself -- to the actual class object
		self.breed = breed
		self.name = name
	
		
mydog = Dog("Lab","Sammy")
#otherdog = Dog(breed="Huskie")
print(mydog.breed)
print(mydog.name)
print(mydog.species)
#CLass obejct Attributes - these are always the same for any instance of the class


class Circle():
	pi = 3.14
	def __init__(self,radius):
		self.radius = radius

	def area(self): # passing in self is to know that this function is a method of that class, and not just some random function
		return self.radius*self.radius*Circle.pi
	
	def set_radius(self, new_r):
		self.radius = new_r #changing the radius inside of itself
		
		
myc = Circle(3)
print(myc.radius)
print(myc.area())
	
myc.radius = 100 #to redefine something in the function
	



#------- INHERITANCE & SPECIAL METHODS ------------------------------------
 
#Inheritance is a way to form new classes using older classes that have already been defined,
#--these newly formed classes are called derived classes, older ones are called base classes 

#creating base class
class Animal():
	
	def __init__(self):
		print ("Animal Created")

	def whoAmI(self):
		print("I am an ANIMAL")
		
	def eat(self):
		print("eating")

mya = Animal()
mya.whoAmI()
mya.eat()
		
class Dog(Animal):
	
	def __init__(self):
		#Animal.__init__(self) #don't need to have this line, it's for understanding
		print("DOG CREATED")
	
	def bark(self):
		print("woof")
		
	def eat(self):
		print("Dog Eating")
	
mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()

#Special Methods-- using certain python syntax to call them
mylist = [1,2,3]

class Book():
	
	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages
		
	def __str__ (self):
		return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)
	
	def __len__(self):
		return self.pages
	
	def __del__(self):
		print("book deleted")
		
	
b = Book("python","jose",200)
print(b) #for print, python looks for an object's string representation
#We provided the string representation __str__ 

print(len(b)) #for len function, python looks for __len__ representation, so we provided that 

del b 



#---------------------------------------------------------------------------#

print('\n -------------- REGEX -------------------')

import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but not the other'

for pattern in patterns:
	print('Im searching for: ' + pattern)

	if re.search(pattern, text): #if pattern is found in text, returns true
		print('match')
	else:
		print('no match')


print(re.search('term1', text))
print(re.search('term1', text).start()) #to get index where 'term1' starts

split_term = '@'
email = 'user@gmail.com'
match = re.split(split_term, email)
print(match) #returns list of texts split at the '@'
# match = email.split('@')
# print(match)

print(re.findall('match','test phrase match in match middle')) 
#returns list wherever match is found. Do len to find the length of that list

def multi_re_find(patterns, phrase):
	for x in patterns:
		print('searching for pattern {}'.format(x))
		print(re.findall(x, phrase))
		print('\n')

#META CHARACTERS 
#any character followed by * is repeated 0 or more times 

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'
test_patterns = ['sd*'] 
#looks for 's' followed by ZERO OR MORE 'd' i.e. s,s,sd,sdd,s,sdd
multi_re_find(test_patterns, test_phrase)
#returns a list of every instance where there is s or s followed by d's

#looks for 's' followed by ONE OR MORE 'd' i.e. sd, sdd, sddd
test_patterns = ['sd+'] 
multi_re_find(test_patterns, test_phrase)

#looks for 's' followed by ZERO OR ONE 'd' i.e. s or sd
test_patterns = ['sd?'] 
multi_re_find(test_patterns, test_phrase)

#looks for 's' followed by SPECIFIC COUNT of 'd' 
test_patterns = ['sd{3}']
#here looks for s followed by 3 d's. i.e. sddd
multi_re_find(test_patterns, test_phrase)
#RETURNS LIST wherever it finds a match

#looks for 's' followed by VARYING COUNT of 'd' 
test_patterns = ['sd{1,3}']
#here looks for s followed by 2 or 3 d's. i.e. sddd, sd, 
multi_re_find(test_patterns, test_phrase)
#RETURNS LIST wherever it finds a match


#looks for 's' followed by different letters 
test_patterns = ['s[sd]+']
#here looks for terms s followed by 1-or-more s's or 1-or-more d's, so, ss,sss,sddd
multi_re_find(test_patterns, test_phrase)
#RETURNS LIST of items wherever it finds a match

#exclusion
test_phrase = 'This is a string! but it has punctuation. How can we remove it?'
 
test_patterns = ['[^!.?]+'] #Looks for all those punctuations, + is to specify one or more instances
multi_re_find(test_patterns, test_phrase)
#returns list of items split at the punctuations specified.

test_patterns = ['[a-z]+'] 
multi_re_find(test_patterns, test_phrase)
#returns list of lowercase characters

test_patterns = ['[A-Z]+'] 
multi_re_find(test_patterns, test_phrase)
#returns list of UPPERCASE characters

test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'
test_patterns = [r'\d+'] #looks for all numbers
multi_re_find(test_patterns, test_phrase)

#IMPORTANT QUICK EXAMPLE
# import re

# x = '12345go 343 34'
# y = re.findall(r'\d+', x)
# print(y) #prints [12345, 343, 34]

# x = '12345go'
# y = re.findall(r'\d+', x)
# print(y) #prints [12345]


# '\D' - non numbers
# '\s' - white space
# '\S' - non white space
# '\w' - alphanumeric
# '\W' - non alpha numeric


#------------------------------------------------------------------------------#

#MODULES and PACKAGES

#Let's say, in the same folder you have a file called mymodule.py and in that file there is a func as such:
#  def func_in_mymodule():
#       print("I am func in mymodel.py file")

#import mymodule
#mymodule.func_in_module()

#import mymodule as mm
#from mymodule import func_in_module
#from mymodule import *  #(imports everything)

#------------------------------------------------------------------------------#

print('\n -------------- DECORATORS -------------------')

#Decorators - can be thought of as functions that modify the functionality of an inner function.
 
# s = 'GLOBAL VARIABLE!'

# def func():
#     print(locals())

# func()

# locals() - returns dictionary, with local variables and their values
# globals() - returns dictionary, with global variables and their values 
#ex: locals()['x']   --- or --- globals()['key']

def hello(name='jose'):
    return 'hello' + name

# print(hello())

#ASSIGN LABELS TO THE FUNCTION ITSELF
mynewgreet = hello
print(mynewgreet())


#FUNCTIONS within FUNCTIONS

def hello(name='jose'):
    print('\nthe hello() function has been run')

    def greet():
        return 'This string is inside greet()'
    def welcome():
        return 'This string is inside welcome'

    # print(greet())
    # print(welcome())
    # print('end of hello()')


#RETURNING FUNCTIONS ** --------------------------------

def hello(name='jose'):
    print('\nthe hello() function has been run')

    def greet():
        return 'This string is inside greet()'
    def welcome():
        return 'This string is inside welcome'

    # print(greet())
    # print(welcome())
    # print('end of hello()')

    if name == 'jose':
        return greet
    else:
        return welcome

#returning a function - assigning it to a variable - and calling that variable's function and printing it out

x = hello()  #hello() function has greet() and welcome() functions inside it. if true x=greet, 
#so x=greet, and x() = greet(). so now we can call greet() by using x(). 
print(x())


# FUNCTIONS as ARGUMENTS
def hello():
    return 'Hi Jose'

def other(func):
    print('hello')
    print(func)
    print(func())

#PASSING THE FUNCTION ITSELF - not what the function returns
#we can pass in functions as arguments, just as we can pass strings/numbers
other(hello)

#------------------------------------------------------------------------------#

#NAME AND IMPORT
def func():
	print('func() in one.py')

print('top level one.py')

if __name__ == '__main__':
	print('one.py is being run directly')
else:
	print('one.py has been imported')

# import one
# print('top level two.py')
# one.func()

if __name__ == '__main__':
	print('two.py being run direcrly')
else:
	print('two is being imported')


#---------------------------------------------------------------------------#

# DECORATORS 

# These were the basic steps needed to know to create a decorator

def new_decorator(func):

    def wrap_func():
        print('code here before execting func')
        func()
        print('func() has been called')

    return wrap_func

# def func_needs_decorator():
#     print('this function is in need of a decorator')

# func_needs_decorator = new_decorator(func_needs_decorator)


#THIS CAN BE DONE WITH THE '@' symbol

@new_decorator
def func_needs_decorator():
    print('this function is in need of a decorator')

func_needs_decorator()
