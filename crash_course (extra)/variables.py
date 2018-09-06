# VARIABLES & DATA TYPES

greeting = 'Welcome to Python'
greeting = 'Python to welcome'

print(greeting)

# DATA TYPE
myStr = 'Hey'
myInt = 22
myFloat = 7.5

myList = [1, 2, 3, 'Hey']
myDict = {
    'a': 1,
    'b': 2,
    'c': 3
    }

print(type(myStr), myStr)
print(type(myInt), myInt)
print(type(myFloat), myFloat)
print(type(myList), myList)
print(type(myDict), myDict)

print(myList[3])
print(myDict['b'])

print(myStr, "it's me.")
greeting = myStr + " it's not me."
print(greeting)