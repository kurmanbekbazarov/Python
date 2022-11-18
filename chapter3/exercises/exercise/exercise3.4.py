# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
# would you invite? Make a list that includes at least three people you’d like to 
# invite to dinner. Then use your list to print a message to each person, inviting 
# them to dinner.

invitation_to_dinner = ['Albert Einstein', 'Isaac Newton', 'Muhammad Ali']
# print(f"Why did you invented theory of relativity {invitation_to_dinner[0]}?")
# print(f"Did you discover the gravity {invitation_to_dinner[1]}?")
# print(f"Best thing about boxing {invitation_to_dinner[2]}?")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the 
# dinner, so you need to send out a new set of invitations. You’ll have to think of 
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end 
# of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with 
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still 
# in your list.

# print(f"{invitation_to_dinner[0]} can't make it today.")
# print(invitation_to_dinner[0])
# print(invitation_to_dinner[1])
# print(invitation_to_dinner[2])


# 3-6. More Guests: You just found a bigger dinner table, so now more space is 
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger 
# dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

# print(f"Hey, I just found a new dinner table {invitation_to_dinner}")
invitation_to_dinner.insert(0, 'Mihir Sahu')
invitation_to_dinner.insert(2, 'Cristiano Ronaldo')
invitation_to_dinner.append('Lionel Messi')

# print(f"Welcome {invitation_to_dinner[0]}!")
# print(f"Welcome {invitation_to_dinner[1]}!")
# print(f"Welcome {invitation_to_dinner[2]}!")
# print(f"Welcome {invitation_to_dinner[3]}!")
# print(f"Welcome {invitation_to_dinner[4]}!")
# print(f"Welcome {invitation_to_dinner[5]}!")


# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a 
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two 
# names remain in your list. Each time you pop a name from your list, print 
# a message to that person letting them know you’re sorry you can’t invite 
# them to dinner.
# • Print a message to each of the two people still on your list, letting them 
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty 
# list. Print your list to make sure you actually have an empty list at the end 
# of your program

print(f'\nSorry, but I can only invite two people for dinner.')

print(invitation_to_dinner)
person1 = invitation_to_dinner.pop()
print(f"I'm sorry {person1}, but I can only invite two people for dinner!")

person2 = invitation_to_dinner.pop()
print(f"I'm sorry {person2}, but I can only invite two people for dinner!")

person3 = invitation_to_dinner.pop()
print(f"I'm sorry {person3}, but I can only invite two people for dinner!")

person4 = invitation_to_dinner.pop()
print(f"I'm sorry {person4}, but I can only invite two people for dinner!")

print(f"Good news you are still invited {invitation_to_dinner[0]}.")
print(f"Good news you are still invited {invitation_to_dinner[1]}.")

del invitation_to_dinner[1]
del invitation_to_dinner[0]
print(invitation_to_dinner)
