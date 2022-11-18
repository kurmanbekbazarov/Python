# Dream Vacation: Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where 
# would you go? Include a block of code that prints the results of the poll.

poll = {}
prompt = "If you could visit one place in the world, where would you go? "
flag = True


while flag:
    name = input("\nWhat is your name? ")
    place = input(prompt)
    poll[name] = place

    new = input("\nWould you like to continue? (yes/no) ")
    if new == 'no':
        flag = False

print('\n')
for name, place in poll.items():
    print(f"{name.title()} wants to visit {place.title()}.")
    

