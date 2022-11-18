# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162). 
# Add an attribute called number_served with a default value of 0. Create an 
# instance called restaurant from this class. Print the number of customers the 
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number 
# of customers that have been served. Call this method with a new number and 
# print the value again.
# Add a method called increment_number_served() that lets you increment 
# the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a 
# day of business


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 10

    def set_number_served(self, served):
        self.number_served = served
    
    def increment_number_served(self, serving):
        self.number_served += serving

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
        print(f"The restaurant has served {self.number_served} customers.")
    
    def open_restaurant(self):
        print(f"\nThe restaurant is open!")

restaurant = Restaurant('agas', 'indian')

print(f"{restaurant.restaurant_name.title()}")
print(f"{restaurant.cuisine_type.title()}")

restaurant.set_number_served(100)
restaurant.describe_restaurant()

restaurant.increment_number_served(200)
restaurant.describe_restaurant()

restaurant.open_restaurant()