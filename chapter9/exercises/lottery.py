# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 
# five letters. Randomly select four numbers or letters from the list and print a 
# message saying that any ticket matching these four numbers or letters wins a 
# prize.
from random import choice

lottery_values = [1, 12, 32, 43, 54, 34, 89, 95, 88, 7, 'a', 'x', 'y', 'z', 'b']
winning_ticket = []

print("Any ticket matching these four numbers or letters wins a prize!")
for i in range(4):
    rand_select = choice(lottery_values)
    winning_ticket.append(rand_select)
print(f"\tThe final winning ticket is: {winning_ticket}")