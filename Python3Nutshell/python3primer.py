# import modules to access libraries
# Cmd Line: 'pip install modulename'
# Cmd Line: 'pip list' //get list of all installed modules
import pandas as pd
# import specific libarary functons with module.fnname
import matplotlib.pyplot as plt

# VARIABLES
# 1. Strongly Typed: no implicit type conversions 
# 2. Dynamicaly Typed: free typeless declarations
var1 = 'string'
var2 = 200
var3 = True
# var2 + var1 throws an error due to strongly typed nature
var1 += str(var2) # explicit type 'casting'

# DATA STRUCTURES (some of the various)
# 1. Lists (Arrays on steroids; ordered, mutable (and dynamic?))
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

# CONTROL FLOW
print("\nCONTROL FLOW SECTION\n")
# &&, ||, ! are represented by 'and' 'or' 'not' (syntatic sugar...)
if var3 and var2<100:
    # Do something
    print("Block 1 executed")
elif type(var1) == 'String':
    # Do something
    print("Block 2 executed")
else:
    print("Block 3 executed")
# TERNARY OPERATION //shortcut!
# returnThisValue if condition else returnThisInstead

# LOOPS
print("\nLOOPS SECTION\n")

loopList = list(range(2,11,2)) # Often used sequence generator to help with looping
# ^ range outputs [2,4,6,8,10]. range(start=0, stopindex, step)
# FOR loop that allows index manipulation
for myIndex in range(len(loopList)):
    print("Looping in index "+ str(myIndex))
# FOR-EACH equivalent
for loopVar in loopList:
    print(loopVar) # 2,4,6,8,10
food = 'apple'
numLetters = 0
while(numLetters<len(food)):
    print(food[numLetters])
    numLetters +=1 # IMPORTANT: ++ and -- do not exist in python.
listA = [1,2,3]
listB = [4,5,6]
for elemListA, elemListB in zip(listA, listB):
    print(elemListA+elemListB) # 5,7,9

# FUNCTIONS (and scope)
print("\nFUNCTIONS SECTION\n")

def myFunction(param1,param2='Default Value'):
    mySum = param1+param2
    return mySum # Function need not return anything.

# GLOBAL keyword
someVar = 5
def scopeTester():
    global someVar # allows fn to read/write the global definition of someVar
    someVar *= 2
    print("Local someVar in the fn is "+str(someVar))
print("Global someVar before fn call is "+str(someVar))
scopeTester()
print("Global someVar after fn call is "+str(someVar)+"\n")

# NONLOCAL keyword
def parentFunction():
    parVar = 3
    def childFunction():
        nonlocal parVar #references parentFn's parVar
        parVar-=1
    print("Parent var before childFn call is "+str(parVar))
    childFunction()
    print("parent var after childFn call is "+str(parVar))
parentFunction()

# CLASSES
print("\nCLASSES\n")

class Line():
    # Class variable shared by all variables
    dimension = 1
    straight = True
    # Vars with _ before its name are by convention treated as private.
    # It's not **actually** private.
    _myPrivateVariable = "hello world!" 
    # AVOID PASSING MUTABLE SEQUENCES (lists, dics) //Refer to documentation
    # ...all instances of 'Line' will share the same sequence

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
print(randomLine.straight) # Unaffected by arc's common field change

class Shape(Line):
    # Shape inherits everything from line
    # Shape can also inherit specific things from line...
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

# If this .py is being run directly, the namespace (__name__) will be __main__
# Is used as a driver function to do stuff.
if __name__ == "__main__":
    print("This script is being run directly!")
