import random

# Create an empty dictionary called var
var = {}

# Print the data type of var
print(type(var))

# Create a dictionary called var2 with some key-value pairs
var2 = {"color":"blue", "juice":"cranberry", "fruit":"mango"}

# Print var2
print(var2)

# Add a new key-value pair to var2
var2["drank"] = "jose"

# Print var2
print(var2)

# Change the value of the "fruit" key in var2
var2["fruit"] = "apple"

# Print var2
print(var2)

# Remove the "fruit" key and its value from var2
del var2["fruit"]

# Print var2
print(var2)

# Print the value associated with the "drank" key in var2
print(var2["drank"])

# Change the value associated with the "fruit" key in var2 back to "mango"
var2['fruit'] = "mango"

# Print var2
print(var2)

# Print the available methods and attributes for var2
print(dir(var2))

# Print the keys of var2
print(var2.keys())

# Print the values of var2
print(var2.values())

# Print the items (key-value pairs) of var2
print(var2.items())

# Print each key and value in var2
for k, v in var2.items():
    print(k, v)
    
# Create a dictionary called var3 with random integer values for each key
var3 = {j:[random.randint(0,100) for i in range(5)] for j in range(5)}

# Print var3
print(var3)
