# 8-6. City Names: Write a function called city_country() that takes in the name 
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the 
# values that are returned.

def city_country(city_name, country):
    full_name = f"\n{city_name.title()}, {country.title()}"
    return full_name

output = city_country('moscow', 'russia')
print(output)
output = city_country('washington', 'usa')
print(output)
output = city_country('madrid', 'spain')
print(output)