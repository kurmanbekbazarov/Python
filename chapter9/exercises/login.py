# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another 
# method called reset_login_attempts() that resets the value of login_attempts
# to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented 
# properly, and then call reset_login_attempts(). Print login_attempts again to 
# make sure it was reset to 0.


class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first.title()} {self.last.title()}\n")

    def greet_user(self):
        print(f"Good morning {self.first.title()} {self.last.title()}!")
    
user = User('kurmanbek', 'bazarov')

user.increment_login_attempts()
print(user.login_attempts)

user.increment_login_attempts()
print(user.login_attempts)

user.increment_login_attempts()
print(user.login_attempts)

user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)