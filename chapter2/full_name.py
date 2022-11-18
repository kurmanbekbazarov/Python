first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
# print(full_name)
# print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
# print(message)

# adding tab
# print("\tPython")

# adding new line
# print("Languages:\nPython\nC\nJavascript")

# Using rstrip() method to remove whitespace at the end of a string
favorite_language = 'python '
cpp = 'cpp'
cpp_and_python = f"{favorite_language} {cpp}"
# print(cpp_and_python)

cpp_and_python.rstrip()
# print(cpp_and_python)

# using lstrip() to remove white space from the left side of the string
random = '     random'
# print(random)
random = random.lstrip()
# print(random)

# using strip() to remove white space from both sides of a string
kate = "          kate               "
kate = kate.strip()
print(kate)