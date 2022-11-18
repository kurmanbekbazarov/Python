# 10-6. Addition: One common problem when prompting for numerical input 
# occurs when people provide text instead of numbers. When you try to convert 
# the input to an int, you’ll get a ValueError. Write a program that prompts for 
# two numbers. Add them together and print the result. Catch the ValueError if 
# either input value is not a number, and print a friendly error message. Test your 
# program by entering two numbers and then by entering some text instead of a 
# number. 

prompt = "Please enter two numbers\n"
prompt += "or type 'q' to exit. "

while True:
    value1 = input("Enter value 1: ")
    if value1 == 'q':
        break
    value2 = input("Enter value 2: ")
    if value2 == 'q':
        break

    try:
        answer = int(value1) + int(value2)
    except ValueError:
        print("\nSorry, can not add strings to integers.")
    else:
        print(answer)