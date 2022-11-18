# Using lists in python
# in order to use list we use square brackets 
# and add all the items inside followed by comma []

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

# to access an element in a list write the name of the list 
# followed by the index.
# print(bicycles[0].title())

# speacial syntax in python to return the last element 
# print(bicycles[-1])

# Using f_strings with lists in python 
message = f"My first bicycle was a {bicycles[0].title()}."
# print(message)

# Changing the values in a list
# print(bicycles)
bicycles[0] = 'suzuki'
# print(bicycles)

# Using append in a list in order to add an element to the end of a list
bicycles.append('ducati')
# print(bicycles)

# Using insert in a list in order to add new elements in any position in list
bicycles.insert(0, 'Hello')
# print(bicycles)

# removing an item using `del` in a list
del bicycles[0]
# print(bicycles)

# using pop() to remove a last item from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)


# Popping items any position in a list
# by including index of the item we can remove any item we want 
first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an item by value
# when we don't know the position of an item we can just specify the value to be removed
e_motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(e_motorcycles)

e_motorcycles.remove('honda')
print(e_motorcycles)