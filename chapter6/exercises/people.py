# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). 
# Make two new dictionaries representing different people, and store all three 
# dictionaries in a list called people. Loop through your list of people. As you 
# loop through the list, print everything you know about each person.

person = {
    'first name': 'Baiel',
    'last name': 'Sadatbek uulu',
    'age': 21,
    'city': 'Houston', 
}

person2 = {
    'first name': 'Cristiano',
    'last name': 'Ronaldo',
    'age': 38,
    'city': 'England',
}

person3 = {
    'first name': 'Gareth',
    'last name': 'Bale',
    'age': 34,
    'city': 'Wales',
}

people = [person, person2, person3]

for person in people:
    name = f"{person['first name'].title()} {person['last name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")
