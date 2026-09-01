# For loops = Executes a block of code a FIXED NUMBER of times.

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# Continue keyword skips the number on the function

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

# Break STOPS the for LOOP in this case by getting to a number