# Exceptions are events that interrupt a program
# basically they are errors (try, except, finally)

try:
    number = int(input("Enter a  Number"))
    print(1 / number)
except ZeroDivisionError:
    print("Cannot divide by 0")
except ValueError:
    print("Enter only numbers")

finally:
    print("Executes always")

