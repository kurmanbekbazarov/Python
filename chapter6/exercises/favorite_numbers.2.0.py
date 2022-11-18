# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) 
# so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

favorite_number = {
    'Beks': [1, 11, 111],
    'Baiel': [2, 123, 90], 
    'Hanbo': [44, 22, 33],
    'Natalie': [12, 32, 43],
    'Sarah': [23, 43, 54],
}

for person, numbers in favorite_number.items():
    print(f"\n{person.title()}'s, favorite numbers are:")
    for number in numbers:
        print(f"{number}")