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

## The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
    print(x)
    
 ## The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3): 
for x in range(2, 30, 3):
        print(x)

 # Else in for loop
## The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
    print(x)
else:
    print("Finally finished!")
    
