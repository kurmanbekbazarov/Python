# 9-13. Dice: Make a class Die with one attribute called sides, which has a default 
# value of 6. Write a method called roll_die() that prints a random number 
# between 1 and the number of sides the die has. Make a 6-sided die and roll it 
# 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        rand_numb = randint(1, self.sides)
        print(rand_numb)


# Roll it 10 times
die = Die()
for i in range(10):
    die.roll_die()
print("\n")

# 10 sided Die
die2 = Die(sides=10)
for j in range(10):
    die2.roll_die()
print("\n")

# 20 sided Die
die3 = Die(sides=20)
for k in range(10):
    die3.roll_die()
