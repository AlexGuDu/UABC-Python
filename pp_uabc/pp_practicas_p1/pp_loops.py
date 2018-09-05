# for
list = []
for i in range(10):
    list.append(i)

print(list)

list = [i for i in range(10) if i % 2 != 0]
print(list)


# while
import random
r = 0
c = 0
while r != 57 or c < 50:
    r = random.randint(1, 10000)
    c += 1
    print(r)
