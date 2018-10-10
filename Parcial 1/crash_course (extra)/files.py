# Open a file
fo = open('test.txt', 'w')

# Get some info 
print('Name:', fo.name)
print('Is closed:', fo.closed)
print('Opening mode:', fo.mode)

# Write to file
fo.write('I am wrrrrrrrriting')
fo.write('\nIn another line too')
fo.close()

# Open to append
fo = open('test.txt', 'a')
fo.write('\n\nHey yo wadup it is I')
fo.close()

# Read from file 
fo = open('test.txt', 'r+')
text = fo.read()
print(text)

# Create file
fo = open('test2.txt', 'w+')
fo.write('This is my new file')
fo.close
