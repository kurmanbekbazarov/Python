# Exercise
# 2-3. Personal Message: Use a variable to represent a person’s name, and print 
# a message to that person. Your message should be simple, such as, “Hello Eric, 
# would you like to learn some Python today?”

import this


name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
# print(message)

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print 
# that person’s name in lowercase, uppercase, and title case.

name = "kurmanbek bazarov"
# print(name.lower())
# print(name.upper())
# print(name.title())


# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the 
# quote and the name of its author. Your output should look something like the 
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a 
# mistake never tried anything new.”

quote = "\"A person who never made a mistake never tried anything new.\""
author = "Albert Einstein"

# print(f"{author} once said, {quote}")

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the 
# famous person’s name using a variable called famous_person. Then compose 
# your message and represent it with a new variable called message. Print your 
# message.
famous_person = "Cristiano Ronaldo"
siuuuuu = "siuuuuuuu"
# print(f"{famous_person}, says {siuuuuu}")





# 2-7. Stripping Names: Use a variable to represent a person’s name, and include 
# some whitespace characters at the beginning and end of the name. Make sure 
# you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, lstrip(), 
# rstrip(), and strip().

name = "     Lionel Messi   "
# print(name)

name2 = name.lstrip()
# print(name2)

name3 = name2.rstrip()
# print(name3)

name4 = name3.strip()
# print(name4)

# In order to print division w/o it being a float we use double backslash // 
# example below 

value = 10
value_2 = 5
division = value / value_2
division2 = value // value_2

# print(division)
# print(division2)

# using underscore in python 
year = 2_0_2_2
# print(year)

# using constant in python 
# in order to set the variable as a constant in python 
# you have to set it your variable to be all capital letters 
# example below

MAX = 100
# print(MAX)



# 2-8. Number Eight: Write addition, subtraction, multiplication, and division 
# operations that each result in the number 8. Be sure to enclose your operations 
# in print() calls to see the results. You should create four lines that look like this:
# print(5+3)
# Your output should simply be four lines with the number 8 appearing once 
# on each line.

# print(5 + 3)
# print(10 - 2)
# print(4 * 2)
# print(16 // 2)

# 2-9. Favorite Number: Use a variable to represent your favorite number. Then, 
# using that variable, create a message that reveals your favorite number. Print 
# that message

favorite_number = 7
message = f"My favorite number is {favorite_number}"
# print(message)

# Python Easter egg 
import this
print(this)