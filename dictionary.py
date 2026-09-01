# Dictionary = its a collection of key:value pairs, ordered and cheangeable, NO DUPLICATES

capitals = {"USA": "Washington D.C.",
            "India":"New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"}) #Used for creating new parts of the dictionary or reassigning values

capitals.pop("China") #Used for removing a value

capitals.popitem() #Used for removing the last used pair

capitals.clear() #Deletes ALL

keys = capitals.keys() #Gets only the keys on the dictionary

for key in capitals.keys():
    print(key)
    

values = capitals.values(): #Gets only the values on the dictionary
    
for value in capitals.values():
    print(value)

items = capitals.items() #Gives a dictionary that is a 2D LIST of tuples	items = [(),(),()]
print(items)



print(capitals)