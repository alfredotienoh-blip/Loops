# Loops
# Looping through a string
# Print each fruit in a fruit list
fruits = ["Apple", "Banana", "Cherry"]
for x in fruits:
    print(x)

     for x in "banana":
        print(x)

  # Continue statement
## With the continue statement we can stop the current iteration, and continue with the next
## Exit the current iteration when x is "banana", and continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() function
## To loop through a set of code a specified number of times, we can use the range() function
for x in range(6):
    print(x)
    
