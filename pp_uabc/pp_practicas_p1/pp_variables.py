# Integers

a = 30
b = 20
c = 50

print(a + b + c)
print("Output Vars a, b, c", a, b, c)
print("Output Vars a:{0}, b:{1}, c:{2}".format(a, b, c))
print("La suma de {0}, {1}, {2}, es de: {3}".format(a,b,c,(a+b+c)))

# Float

a = 49.99
b = 33.33
c = 25.55

print(a + b + c)

# Boolean

a = True
b = False

# String
s = "String de comillas dobles"
ss = 'String de comillas simples'
sss = "String con 'comillas simples' dentro el"

# List

list = [1,2,3,4,5,6,7,8,9]
list.append(0)
list.insert(0, 20)
print(list)

lista.append(0)
print(list)

lista.insert(0, 0)
print (list)

lista.pop()
print(list)

lista.pop(0)
print(list)

lista.pop(len(list)-1)
print(list)

list[10] = 10
print(list)


for item in list:
    print(item)

list = ["Message 0", "Message 1", "Message 3"]
list.pop(list.index("Message 0"))

print(list)


# Tuples
t = (1, 2, "abc", true, [4, 5])
lista = [4]
print (t)

print(t(2))

for item in t:
	print(item)

# Dicts
d = {1:2, "abc":34, 2:"item", "d":"ch", "li":[1, 2, 3], "dic": {11:23}}

print(d[2])
print(d["li"][1])
print(d["dic"][11])

print(d.keys())
print(d.values())
print(d.items())

# Sets
s ={,1, 2, 3, 4, 5}

print(s)
print(type(s))

for item in s:
	print(item)

s.add(5)
print(s)
