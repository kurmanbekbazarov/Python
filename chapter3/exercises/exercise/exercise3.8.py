# 3-8. Seeing the World: Think of at least five places in the world you’d like to 
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly, 
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the 
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its 
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show 
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the 
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse alphabetical order. 
# Print the list to show that its order has changed.

placesToVisit = ['Japan', 'France', 'Russia', 'Switzerland', 'Sweden']

# print(placesToVisit)
# print(sorted(placesToVisit))
# print(placesToVisit)
# print(sorted(placesToVisit, reverse=True))
# print(placesToVisit)

# placesToVisit.reverse()
# print(placesToVisit)
# placesToVisit.reverse()
# print(placesToVisit)

# placesToVisit.sort()
# print(placesToVisit)
# placesToVisit.sort(reverse=True)
# print(placesToVisit)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
# through 3-7 (page 42), use len() to print a message indicating the number 
# of people you are inviting to dinner.
invitation = ['kate', 'hailey', 'lili']
# print(len(invitation))

# 3-10. Every Function: Think of something you could store in a list. For example, 
# you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items 
# and then uses each function introduced in this chapter at least once.
countries = ['Sweden', 'France', 'Japan', 'Albania']

countries.sort()
print(countries)

sorted(countries)
print(countries)

countries.reverse()
print(countries)

countries.sort(reverse=True)
print(countries)
