# Keyword arguments are preceded by an identifier, this helps with readability, THE ORDER DOESN'T MATTER.
# They help by referencing the argument in the function call, this makes it easier to identify which is which and for what

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}\n")
    
hello("Hello", title="MR", first="Spongebob", last="Squarepants") #THIS KEYWORD ARGUMENTS REFERENCE THE FUNCTION (now the order doesn't matter).
#Make sure any positional arguments are in correct order if not using keyword arguments (the order matters in these).


for x in range (1, 11):
    print(x, end=" ") #End is an argument for the PRINT statement or function

print("1", "2", "3", "4", "5", sep="-") #Separates the strings with a dash this is also a keyword argument

#Generate a phone number
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)
