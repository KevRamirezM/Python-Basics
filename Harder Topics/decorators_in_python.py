# Decorator is a function that extends the behavior of another function
# without modifying the base function

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Add Sprinkles 🎊")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge 🍫")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Ice Cream for you {flavor} flavor 🍦")

get_ice_cream("vanilla")
