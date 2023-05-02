import random

# Create an empty list called var
var = []

# Print the data type of var
print(type(var))

# Add different data types to a new list called var2
var2 = [151, 251, 386, 493, "009"]

# Print var2
print(var2)

# Add 649 to var2
var2.append(649)

# Print var2
print(var2)

# Concatenate var2 with [721]
var2 = var2 + [721]

# Print var2
print(var2)

# Reverse the order of var2
var2.reverse()

# Print var2
print(var2)

# Print the available methods and attributes for var2
print(dir(var2))

# Create a list of numbers from 0 to 9 called var3
var3 = [0,1,2,3,4,5,6,7,8,9]

# Print var3
print(var3)

# Create a list of numbers from 0 to 14 called numbers
numbers = list(range(15))

# Print the 6th element of numbers
print(numbers[5])

# Print the length of numbers
print(len(numbers))

# Print each number in numbers and its double
for number in numbers:
    print(number, number*2)
    
# Create a 5x5 matrix of random integers between 0 and 100 called var4
var4 = [[random.randint(0,100) for i in range(5)] for j in range(5)]

# Print var4
print(var4)
