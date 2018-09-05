# STRING FUNCTIONS

myStr = 'Hey There Everybody'

# Capitalize
print(myStr.capitalize())

# Swap case
print(myStr.swapcase())

# Get length
print(len(myStr))

# Replace
print(myStr.replace('Everybody', 'Nobody'))

# Count
sub = "e"
print(myStr.count(sub))

# Startswith
print(myStr.startswith('Hey'))
print(myStr.startswith('Somethingelseentirely'))

# Endswith
print(myStr.endswith('body'))
print(myStr.endswith('Body'))

# Split to list
print(myStr.split())

# Find
print(myStr.find('Everybody'))
print(myStr.find('o'))

# Index
print(myStr.index('y'))

# Is all alphanumeric
print(myStr.isalnum())

# Is all alphabetic
print(myStr.isalpha())

# Is all numeric
print(myStr.isnumeric())
