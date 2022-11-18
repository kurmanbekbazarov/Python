# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list and as 
# you do, print everything you know about each pet.

pet_1 = {
    'kind of an animal': 'dog',
    'name': 'speed',
    'owners name': 'Jackie',
}

pet_2 = {
    'kind of an animal': 'cat',
    'name': 'bond',
    'owners name': 'suzy',
}

pets = []

pets.append(pet_1)
pets.append(pet_2)

for pet in pets:
    type = pet['kind of an animal'].title()
    name = pet['name'].title()
    owner = pet['owners name'].title()

    print(f"This is {type} his name is {name}, his owner's name is {owner}.")