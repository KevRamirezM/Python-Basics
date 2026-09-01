# Default Arguments is a default value, its used when the argument is ommited. Can be replaced manually.
#Makes functions more flexible, easier to use and reduces the number of arguments needed.

def net_price(list_price, discount=0, tax=0.05): # This makes the function ALWAYS USE the part defined by = in the function.
    return list_price  * (1 - discount) * (1 + tax)

print(net_price(500)) # Here it uses default arguments for discount and tax arguments.
print(net_price(500, 0.1)) # Here the discount is NEWLY set to 0.1 and tax remains the same.

# Count up TIMER

import time

def count(start=0, end=10):
    for x in range (start, end+1): #Adds 1 to the end of the time
        print(x)
        time.sleep(1)
    print("DONE!")
    
    
count(0, 10) # This function is called and starts printing the COUNT from START TO END parameters

#IMPORTANT
# The order matters in arguments, also the function has to be called with the SAME NUMBER of arguments as defined
# If for example i define start to 0 and end to 0 there is no problem
# Since both parameters have default values, you can omit one or both.
# If you only pass one argument (count(10)), Python will treat it as the first parameter (start=10) — not as end. BECAUSE OF THE ORDER

