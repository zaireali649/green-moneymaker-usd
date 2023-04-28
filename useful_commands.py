# This line imports the "random" module, which provides functions for generating random numbers
import random

# This line creates a variable "var" and assigns it the value 2
var = 2

# This line prints the data type of the variable "var" to the console
print(type(var))

# This line creates a variable "var2" and assigns it the value "str"
var2 = "str"

# This line prints the data type of the variable "var2" to the console
print(type(var2))

# This line prints a list of all the available methods and attributes of the variable "var2"
print(dir(var2))

# This line calls the "capitalize()" method on the variable "var2" and prints the result to the console
print(var2.capitalize())

# This line creates a variable "var3" and assigns it the value "9"
var3 = "9"

# This line pads the variable "var3" with leading zeros until it has a length of 3, and prints the result to the console
print(var3.zfill(3))

# This line generates a random integer between 0 and 100 (inclusive) and prints it to the console
number = random.randint(0,100)
print(number)
