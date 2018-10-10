#While
i = 1

while i<10:
	print(i)
	i += 1

#For
k = 1

for k in range(10):
	print(k)

for j,k in enumerate(range(10)):
	print(j)
	print("K",k)

for item in [1,2,3,4,5]:
	print(item*2)

for item in "[1,2,3,4,5]":
	print(item*2)

for line open("Nombre de archivo"):
	print(line)

for l, line in enumerate(open("Nombre del archivo")):
	for p in line.split():
	print(p)

for l, line in enumerate(open("Nombre del archivo")):
	for p in line.split():
		for f in p:
			print(f)

for l, line in enumerate(open("Nombre del archivo")):
	for p in line.split():
		for f in p:
			if f == "r":
				pass
			else:
				print(f)

lista = []
for i in range(10):
	lista.append(i)
print(lista)


import random
r = 1
while r ! = 99:
	r = random.randint(1, 100)
	print(r)
