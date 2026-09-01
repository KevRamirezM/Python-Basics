# Nested loop is a loop within another loop (outer and inner)


# This code PRINTS numbers 1-9
for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()

#This code prints a symbol in a number of rows and columns

rows = int(input("Enter the number of rows"))
columns = int(input("Enter the number of columns"))
symbol = input("Enter a symbol to use")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()