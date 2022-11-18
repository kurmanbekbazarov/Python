# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
# text of a message that should be printed on the shirt. The function should print 
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the 
# function a second time using keyword arguments

def make_shirt(size, message):
    print(f"The size of the shirt is {size.title()}.")
    print(f"Message that will be displayed is {message.title()}.")

# Postional function call
make_shirt('m', 'hello world!')

# Function call using keyword arguments
make_shirt(size = 'm', message = 'hello world!')