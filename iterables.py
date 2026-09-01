#Iterables its an OBJECT or COLLECTION that can return its elements, ONE AT A TIME, can be iterated over in a LOOP.

numbers = [1, 2, 3, 4, 5]#This is a list because its using []

for number in numbers:
    print(number)

for number in reversed(numbers): #You also can iterate backwards from last to first USING REVERSED FUNCTION
    print(number, end=" ") #Ends the element with a space character

fruits = {"apple", "orange", "banana", "coconut"}#This is a set because its using {}
for fruit in fruits:
    print(fruit)
    
    
name = "Kevin Ramirez"#This is a string its defined with " "
for character in name:
    print(character, end=" ")
    
my_dictionary = {"A":1, "B":2, "C":3} #Its defined like a SET but EACH ELEMENT is a key-value pair, in this case it returns the key assigned to it (A, B, C)

for key in my_dictionary:
    print(key)
    
for value in my_dictionary.values(): #In this case it returns the VALUE assigned to it (1, 2, 3)
    print(value)
    
for key, value in my_dictionary.items(): #In this case it returns BOTH the KEY and the VALUE
    print(f"{key} = {value}")