import random

# Generate a random integer between 0 and 10 (inclusive)
number = random.randint(0, 10)

# Set a threshold value to compare against the random number
thresh = 6

# Compare the random number to the threshold value and print an appropriate message
if number > thresh:
    print("big number")
elif number < 4:
    print("really small number")
elif number < thresh:
    print("small number")
else: # elif number == 7:  # Comment: This condition is unnecessary since it is covered by the previous elif statement.
    print("number is {}".format(thresh))

# Check if the random number is really big and print a message if it is
if number > thresh + 1:
    print("really big number")

# Print the random number
print(number)
