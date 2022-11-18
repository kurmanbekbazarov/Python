alien_0 = {'color': 'green', 'speed': 'slow'}

# get() method requires a key as a first argument and
# as a second argument optional you can print a message
# if the key doesn't exist in the dictionary.

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)