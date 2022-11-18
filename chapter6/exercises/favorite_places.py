# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three 
# names to use as keys in the dictionary, and store one to three favorite places 
# for each person. To make this exercise a bit more interesting, ask some friends 
# to name a few of their favorite places. Loop through the dictionary, and print 
# each person’s name and their favorite places

favorite_places = {
    'erin': ['eiffel tower', 'usa', 'burger kings'],
    'michael': ['statue of liberty', 'brazil', 'sumo'],
    'felix': ['clubs', 'smoking', 'weed'],
}

for key, values in favorite_places.items():
    name = key.title()
    print(f"\n{name} likes these places:")
    for value in values:
        print(f"{value.title()}")

