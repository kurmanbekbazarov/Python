# 4-10. Slices: Using one of the programs you wrote in this chapter, add several 
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to 
# print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Use a slice to 
# print three items from the middle of the list.
# • Print the message The last three items in the list are:. Use a slice to print the 
# last three items in the list.
favorite_pizzas = ['Brooklyn', 'Italian', 'NYC', "Houston", "French", "Mexican", "Spanish"]

# print("The first three items in the list are:")
# print(favorite_pizzas[0:3])

# print("\nThree items from the middle of the list are:")
# print(favorite_pizzas[2:5])

# print("\nThe last three items in the list are:")
# print(favorite_pizzas[4:])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. 
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite 
# pizzas are:, and then use a for loop to print the first list. Print the message 
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.
favorite_pizzas_1 = ['Brooklyn', 'Italian', 'NYC']
friend_pizzas = favorite_pizzas_1[:]

favorite_pizzas_1.append("Mexican")
friend_pizzas.append("Spanish")

# print("My favorite pizzas are:")
# for pizza in favorite_pizzas_1:
#     print(pizza)

# print("\nMy friend's favorite pizzas are:")
# for pizza_2 in friend_pizzas:
#     print(pizza_2)

# 4-12. More Loops: All versions of foods.py in this section have avoided using 
# for loops when printing to save space. Choose a version of foods.py, and 
# write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for pizza in my_foods:
    print(pizza)

print("\nMy friend's favorite foods are:")
for friend_pizza in friend_foods:
    print(friend_pizza)