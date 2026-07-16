# Looping through a string
# Print each fruit in a fruit list
fruits = ["Apple", "Banana", "Cherry"]
for x in fruits:
    print(x)
    
    for x in "banana":
        print(x)
        
# The Break statement
# With break statement you can stop the loop before it has looped through all the items
# Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    
# Exiting the loop when x = "banana", but this time the break comes before the print(print()
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
    
    # Continue statement
# With the continue statement we can stop the current iteration, and continue with the next
# Exit the current iteration when x is "banana", and continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)