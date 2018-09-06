# LOOPS
people = ['John', 'Sarah', 'Tim', 'Bob']


# FOR LOOPS
print('For loop')
for person in people:
    print('Current Person:', person)
    
# Iterate by sequence index
print('For loop with index')
for i in range(len(people)):
    print('Current Person:', people[i])
    
for i in range(0, 10):
    print(i)
    
# WHILE LOOP
count = 0
while count < 10:
    print('Count:', count)
    if count == 5:
        break
    count=count+1;