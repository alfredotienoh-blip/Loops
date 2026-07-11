# Looping through a string
# Print each fruit in a fruit list
fruits = ["Apple", "Banana", "Cherry"]
for x in fruits:
    print(x)
    
    for x in "banana":
        print(x)
        
# The Break statement
# With break statement you can stop the loop before it has looped through all the items
#Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break