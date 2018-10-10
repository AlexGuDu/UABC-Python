# User functions: return string
def greeting():
	return "Hey there "

print(greeting())
greeting_message = (greeting())
greetee = "Bob Cernovsky"
print(greeting_message + greetee)

# User functions: sum
x = int(input("Give me the first number "))
y = int(input("Give me the SECOND number "))

def add(num1, num2):
    num_total = num1 + num2
    return num_total

print(add(x, y))

# functions by Python
import random, math
from math import pi
for i in range(10):
    print(random.randint(x, y) * math.cos(i))
    print(pi)
