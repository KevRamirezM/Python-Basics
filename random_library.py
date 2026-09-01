import random

#Random number between 2 numbers
low = 1
high = 100
number = random.randint(low, high)
print(number)

#Random float between 0 and 1
number2 = random.random()
print(number2)

#Select a random element
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

#Random shuffling a LIST
cards = ["2","3","4","5","6","7","8",'9','10','J','Q','K','A']
random.shuffle(cards)
