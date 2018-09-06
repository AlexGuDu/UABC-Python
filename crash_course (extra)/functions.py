# FUNCTIONS

# Create a function
def sayHi(name):
    'This is not getting parsed'
    print('Hi', name)
    
sayHi("it's me, ya boi.")

# Return a Value
def getSum(num1, num2):
    total = num1 + num2
    return total
numSum = getSum(5, 10)
print(numSum)


def addOneToNum(num):
    num = num + 1
    print('Value inside function:', num)
    return

num = 5
addOneToNum(num)
print('Value outside function:', num)
# The result of the addOneToNum function does change the global value of num, since integers are inmutable.

def addOneToList(myList):
    myList.append(4)
    print('Value inside function:', myList)
    return

myList = [1,2,3]
addOneToList(myList)
print('Value outside function:', myList)
# The result of the addOneToList function does change the global value of myList, since lists are mutable.