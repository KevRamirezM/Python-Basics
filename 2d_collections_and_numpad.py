#  2D Collections

fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

#Uses coordinates by using row and column 
print(groceries[0][0])


# Use a for loop for iterating between all values of the collection
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
    
# Creating a Numeric PAD with a TUPLE

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
    
