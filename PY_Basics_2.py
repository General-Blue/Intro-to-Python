import random 

def spam(x):
    for i in range(0,x):
        print("spam")

def roll():
    Dice1 = random.randint(1,6)
    Dice2 = random.randint(1,6)
    return Dice1, Dice2

spam(1) 

results = roll()
print(results)

# Python Lists
# make an array

# make a tuple

# make a dictionary

# Python loops

# for-loop index method

# pythonic for-loop

# while loop