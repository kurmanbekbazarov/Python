# *asterisk in the parameter name *toppings 
# tells Python to make an empty tuple called toppings

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

