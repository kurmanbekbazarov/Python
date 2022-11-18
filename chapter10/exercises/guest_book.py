# 10-4. Guest Book: Write a while loop that prompts users for their name. When 
# they enter their name, print a greeting to the screen and add a line recording 
# their visit in a file called guest_book.txt. Make sure each entry appears on a 
# new line in the file.
prompt = "Please enter your name: "
prompt += "\nor type 'q' to exit! "
flag = True
filename ='guest_book.txt'

while flag:
    name = input(prompt)
    if name == 'q':
        flag = False
        break

    print(f"Welcome back {name}.\n")
    with open(filename, 'a') as file_object:
        file_object.write(f"{name}\n")
