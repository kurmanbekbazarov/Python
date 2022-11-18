# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"\nThe restaurant is open!\n")

restaurant = Restaurant('agas', 'indian')
restaurant_2 = Restaurant('china king', 'chinese')
restaurant_3 = Restaurant('tequila', 'mexican')

print(f"{restaurant.restaurant_name.title()}")
print(f"{restaurant.cuisine_type.title()}")

restaurant.describe_restaurant()      
restaurant.open_restaurant()

print(f"{restaurant_2.restaurant_name.title()}")
print(f"{restaurant_2.cuisine_type.title()}")

restaurant_2.describe_restaurant()      
restaurant_2.open_restaurant()

print(f"{restaurant_3.restaurant_name.title()}")
print(f"{restaurant_3.cuisine_type.title()}")

restaurant_3.describe_restaurant()      
restaurant_3.open_restaurant()
