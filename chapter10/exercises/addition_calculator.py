# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop 
# so the user can continue entering numbers even if they make a mistake and 
# enter text instead of a number

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