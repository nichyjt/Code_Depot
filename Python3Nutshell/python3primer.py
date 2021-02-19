# import modules to access libraries
# Cmd Line: 'pip install modulename'
# Cmd Line: 'pip list' //get list of all installed modules
import pandas as pd
# import specific libarary functons with module.fnname
import matplotlib.pyplot as plt
import itertools

"""VARIABLES"""
# 1. Strongly Typed: no implicit type conversions 
# 2. Dynamicaly Typed: free typeless declarations
var1 = 'string'
var2 = 200
var3 = True
# var2 + var1 throws an error due to strongly typed nature
var1 += str(var2) # explicit type 'casting'

""" ****A NOTE on Variables, Names & Python****
    In other languages, assigning variables is like putting a value in a box.
    Re-assigning a value will change what is IN the box.
    Assigning a new variable to another variable will create a copy of the value
    eg. foo = 1 // foo is the box, the value is 1
        foo = 2 // 1 is replaced with 2
        bar = foo // bar is a new box
    
    In Python, we have names. Objects are created and a label is attached to it.
    eg. foo = 1 // 1 has alias foo, and 1 is created
        foo = 2 // 2 is created, and has alias foo. 1 has no alias.
        bar = foo // 2 has aliases foo and bar
        bar += 1 // 3 is created, and has alias bar.
"""


"""COMMONLY USED DATA STRUCTURES"""
# 1. Lists (Arrays on steroids; ordered, mutable and can hold different data types)
myList = ['string1', True, [1,[2,3],4], (5,6,7), var3]
myList[0] #'string1'
myList.insert(2,'newValue')

# 2. Tuples (Immutable, _usually_ hold heterogenous data)
aTuple = (8,9,'ten!',(11,12),13)
aTuple[2] #'ten!' Note that you cannot delete or add any new elems w/o re-declaring

# 3. Dicts (Key-Value pairs)
myDict = {
    "key1":"value1",
    "key2":800
}
myDict['key1'] # 'value1'
myDict['newKey'] = 'newValue' # appends new k-v pair to myDict
myDict.items() # Get a list of k-v tuples
myDict.keys() # Get a list of keys. Similar to .values()

"""CONTROL FLOW AND LOOPS"""
print("\nCONTROL FLOW SECTION\n")
# &&, ||, ! are represented by 'and' 'or' 'not' keywords
if var3 and var2<100:
    # Do something
    print("Block 1 executed")
elif type(var1) == 'String':
    # Do something
    print("Block 2 executed")
else:
    print("Block 3 executed")
# TERNARY STATEMENT SYNTAX
# returnThisValue if condition else returnThisInstead

print("\nLOOPS SECTION\n")
loopList = list(range(2,11,2))
# ^ range outputs [2,4,6,8,10]. range(start=0, stopindex, step)

# Classic C-style FOR loop equivalent
for myIndex in range(len(loopList)):
    print("Looping in index "+ str(myIndex))

# FOR-EACH equivalent
for loopVar in loopList:
    print(loopVar) # 2,4,6,8,10

# STRING looping demonstration
food = 'apple'
numLetters = 0
while(numLetters<len(food)):
    print(food[numLetters])
    numLetters +=1 # IMPORTANT: ++ and -- do not exist in python.

# ZIP utility demonstration
listA = [1,2,3]
listB = [4,5,6]
for elemListA, elemListB in zip(listA, listB):
    print(elemListA+elemListB) # 5,7,9

"""FUNCTIONS & SCOPE"""
print("\nFUNCTIONS SECTION\n")

# General Syntax (Annotations not included)
def myFunction(param1,param2='Default Value'):
    mySum = param1+param2
    return mySum # Function need not return anything.
""" **** A NOTE on default arguments ***    
    Best practice: DO NOT HAVE MUTABLE SEQUENCES AS A DEFAULT ARG
    Functions are first class objects in Python.
    Default parameters are kind of like 'member data'
    This means that their state can change. This may cause unexpeced behaviour
"""
def oddFn(b, a=[]):
    a.append(b)
    return a
"""
>>> oddFn(1)
[1]
>>> oddFn(2)
[1,2]
"""

# GLOBAL keyword demonstration
someVar = 5
def scopeTester():
    global someVar # references the variable named 'someVar' in the global scope.
    someVar *= 2
    print("Local someVar in the fn is "+str(someVar))
print("Global someVar before fn call is "+str(someVar))
scopeTester()
print("Global someVar after fn call is "+str(someVar)+"\n")

# NONLOCAL keyword demonstration
def parentFunction():
    parVar = 3
    def childFunction():
        nonlocal parVar #references parentFn's parVar
        parVar-=1
    print("Parent var before childFn call is "+str(parVar))
    childFunction()
    print("parent var after childFn call is "+str(parVar))
parentFunction()

"""CLASSES"""
print("\nCLASSES\n")

class Line():
    # Class variable/attr/fields shared by all Line objects
    dimension = 1
    straight = True
    # Vars with _ before its name are by convention treated as private. (PEP8 Convention)
    # Not actually private.
    _myPrivateVariable = "hello world!" 

    # As mentioned ealier, avoid passing default mutable args in the constructor
    # as all instances of 'Line' will share the same sequence

    def __init__(self, length=1): # Constuctor
        # Constructors set the params for an instance of this object.
        self.length = length

    # Common fields (s/a 'straight' in this context)
    # can be set without affecting other instances of it
    def setIsCurved(self, isCurved):
        self.straight = False

    def getLengthTimesTwo(self): # Used to demonstrate super()
        return self.length*2
    
arc = Line(100)
print(arc.straight)
arc.setIsCurved(True)
print(arc.straight)
randomLine = Line(200)
print(randomLine.straight) # Unaffected by arc's common field change as each Line object is unique.

class Shape(Line):
    # Shape inherits everything from line
    # Shape can also inherit specific things from line with the following syntax
    # Shape(Line.straight)
    
    def __init__(self, shapeColor, numSides, length): # Constructor.
        super().__init__(length) # Calls parent constructor to set whatever fields
        self.side = numSides
        self.color = shapeColor

    def getSpecialNumber(self): # Demonstrating using super() for parent class methods
        lengthDoubled = super().getLengthTimesTwo()
        return self.side * lengthDoubled - self.length
        

square = Shape("Brown", 4, 8)
print(square.color)
square.setIsCurved(True)
print(square.dimension)
print(square.getSpecialNumber())

"""USEFUL FUNCTIONS"""
# TODO map, split, join, combi, premu, starmap, filter
print("\nOTHER USEFUL FUNCTIONS")
# Lambda function demonstration (anon fns)
x = lambda a,b : 10*(a+b)
print(x(1,2))
# >>> 3

# map() demonstration
def addOne(arg1:int):
    arg1+=1
    return arg1
oneToTen = map(addOne, [x for x in range(10)])
print(list(oneToTen)) # 1,2,3...,9,10

# itertools has many useful functions. Read: https://docs.python.org/3/library/itertools.html

# If this .py is being run directly, the namespace (__name__) will be __main__
# Is used as a driver function to do stuff.
if __name__ == "__main__":
    print("This script is being run directly!")
