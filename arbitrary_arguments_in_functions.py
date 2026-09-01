#Arbitrary Arguments
# *args = allows you to pass multiple NON-KEY arguments
# **kwargs = allows you to pass multiple KEY arguments

def add (*args): #This will pack arguments into a tuple ()
    total = 0
    for arg in args:
        total += arg
    return total
        
def add (*nums): #The name can be anything BUT it has to have the unpacking operator *, normally it stays as args
    total = 0
    for num in nums:
        total += num
    return total
        

print(add(1))

def display_name(*args):
    for arg in args:
        print(arg, end="")
    
display_name("Spongebob"," ", "Squarepants\n")

def print_address(**kwargs): #This keyword arguments are packed into a DICTIONARY
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="123 Diamond",
              apt= "100", 
              city="Detroit", 
              state="Michigan", 
              zip="54321")

def shipping_label(*args, **kwargs): #In this instance PUT FIRST positional arguments and THEN keyword arguments
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr", "Spongebob", "Squarepants",
              street="123 Diamond",
              apt= "100", 
              city="Detroit", 
              state="Michigan", 
              zip="54321")