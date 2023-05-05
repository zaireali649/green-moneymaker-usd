import random

# Create a list of numbers from 0 to 9 and print each number along with its double
numbers = list(range(10))
for number in numbers:
    print(number, number*2)

# Create a dictionary and print each key-value pair
var2 = {"a":1, "b":2, "c":3}
for k, v in var2.items():
    print(k, v)

# Print the same message 5 times
for i in range(5):
    print("Green is the goat")

# Generate a random number between 0 and 100 until it equals 57 and count how many iterations it takes
number = random.randint(0, 100)
counter = 0
while (number != 57):
    number = random.randint(0, 100)
    counter = counter + 1 # counter += 1
print(counter, number)

# Generate a random number between 0 and 100 until it equals 57, but break out of the loop if it takes more than 100 iterations
number = random.randint(0, 100)
counter = 0
while (number != 57):
    number = random.randint(0, 100)
    counter = counter + 1 # counter += 1
    if(counter >= 100):
        break
print(counter, number)

# Generate a random number between 0 and 100 until it equals 57, but break out of the loop after 1000 iterations
number = random.randint(0, 100)
for i in range(1000):
    if number == 57:
        break
    number = random.randint(0, 100)
print(i, number)
