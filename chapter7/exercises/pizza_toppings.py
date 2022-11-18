#  Pizza Toppings: Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value. As they enter each topping, 
# print a message saying you’ll add that topping to their pizza.

prompt = "\nPlease enter a series of pizza toppings or type 'quit' to exit. "
flag = True
while(flag):
    message = input(prompt)
    if message != 'quit':
        print(f"\tI'll add {message} topping to your pizza.")
    else:
        flag = False