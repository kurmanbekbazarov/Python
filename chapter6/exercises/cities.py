# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as 
# keys in your dictionary. Create a dictionary of information about each city and 
# include the country that the city is in, its approximate population, and one fact 
# about that city. The keys for each city’s dictionary should be something like 
# country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'new york': {
        'country': 'usa',
        'population': '19 million',
        'fact': 'originally was called new amsterdam',
         },
    'los angeles': {
        'country': 'usa',
        'population': '3 million',
        'fact': 'original name El Pueblo de Nuestra Senora Reina de los Angeles sobre el Rio Porciuncula',
         },
    'houston': {
        'country': 'usa',
        'population': '2 million',
        'fact': 'founded by land investors',
         },
}

for city, info in cities.items():
    country = info['country'].title()
    population = info['population'].title()
    fact = info['fact'].title()

    print(f"\nName of the city is {city}.")
    print(f"Located in {country} with the {population}, and fun fact {fact}.")
