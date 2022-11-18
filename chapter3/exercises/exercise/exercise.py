# #3-1. Names: Store the names of a few of your friends in a list called names. Print 
# each person’s name by accessing each element in the list, one at a time.

names = ['Beks', 'Baiel', 'Hanbo']
# print(names[0])
# print(names[1])
# print(names[2])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
# printing each person’s name, print a message to them. The text of each message should be the same,
# but each message should be personalized with the 
# person’s name.

message1 = f"This is {names[0]} he plays soccer."
message2 = f"This is {names[1]} he plays soccer."
message3 = f"This is {names[2]} he plays soccer."

# print(message1)
# print(message2)
# print(message3)


# 3-3. Your Own List: Think of your favorite mode of transportation, such as a 
# motorcycle or a car, and make a list that stores several examples. Use your list 
# to print a series of statements about these items, such as “I would like to own a 
# Honda motorcycle.”

types_of_car = ["Toyota", "Honda", "Lexus"]
my_favorite_transportation = ['car', 'bicycle', 'bus']
statement = f"I would like to own a {types_of_car[0]} {my_favorite_transportation[0]}."
print(statement)