# 9-7. Admin: An administrator is a special kind of user. Write a class called 
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) 
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list 
# of strings like "can add post", "can delete post", "can ban user", and so on. 
# Write a method called show_privileges() that lists the administrator’s set of 
# privileges. Create an instance of Admin, and call your method.

class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def describe_user(self):
        print(f"{self.first.title()} {self.last.title()}\n")

    def greet_user(self):
        print(f"Good morning {self.first.title()} {self.last.title()}!")

class Admin(User):
    def __init__(self, first, last, privileges = []):
        super().__init__(first, last)
        self.privileges = privileges

    def show_privileges(self):
        print(f"List of priveleges: ")
        for i in self.privileges:
            print(f"\t{i}")

# admin = Admin('kurmanbek', 'bazarov', privileges=["can add post", "can delete post", "can ban user",])

# admin.show_privileges()
