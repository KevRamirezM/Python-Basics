# A collection is a single variable used to store multiple values

    # A list is ORDERED and CHANGEABLE. You can use DUPLICATES ITS USED WITH []
fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)

# Index operator gets the number you assign of the collection (CAN ALSO BE A RANGE)
print(fruits[0])
print(fruits[0:3])

# In operator checks if a value is inside of the list
print("pineapple" in fruits)

# Append adds a element at the end of the list
fruits.append("pineapple")

# Remove removes an element of the list
fruits.remove("apple")

# Insert inserts an element at whatever position of the list
fruits.insert(0, "pineapple")

# Sort orders the list on alphabetical order
fruits.sort()

# Reverse changes the order of the list and starts at the end and ends on the beginning
fruits.reverse()

# Clear erases all elements of the list
fruits.clear

# Checks the position of a value on the list
fruits.index("apple")

# Counts HOW MANY of a value is on a list
fruits.count("banana")

    # A set is UNORDERED and IMMUTABLE, but you can ADD or REMOVE. NO DUPLICATES ITS USED WITH {}
fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)

#Len function is for the length
len(fruits)

# In operator checks if a value is inside of the set
print("pineapple" in fruits)

# A set cannot be ordered and is NOT SUBSCRIPTABLE
# Add adds a element to the set
fruits.add("pineapple")

# Remove removes an specific element of the set
fruits.remove("pineapple")

# Pop removes WHATEVER ELEMENT IS THE FIRST ONE, but in this case it is random because its A SET (unordered)
fruits.pop()

# Clear erases all elements of the set
fruits.clear

    # A tuple is ORDERED and UNCHEANGEABLE, You can use DUPLICATES. IS FASTER ITS USED WITH ()

# In operator checks if a value is inside of the tuple
print("pineapple" in fruits)

#Index checks on what position is a value
fruits.index("apple")

#Count counts HOW MANY times a value appears in the tuple
fruits.count("coconut")
