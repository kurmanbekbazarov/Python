# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"\nThe restaurant is open!")

# restaurant = Restaurant('agas', 'indian')

# print(f"{restaurant.restaurant_name.title()}")
# print(f"{restaurant.cuisine_type.title()}")

# restaurant.describe_restaurant()      
# restaurant.open_restaurant()
