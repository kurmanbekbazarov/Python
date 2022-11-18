# Introduction to Tuples 
# Tuples work just like a list but when creating a tuple
# the items cannot change when u use tuples and is referred to as immutable list and is called tuple. 
# We use parentheses instead of square brackets to define a tuple.

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)