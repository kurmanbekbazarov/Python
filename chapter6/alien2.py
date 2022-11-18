alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

# print(alien_0)

# Modifying the existing dictionary in python. 
# print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")

alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_1['x_position']}")

# Move the alien to the right. 
# Determine how far to move the alien based on its current speed.
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # This must a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_1['x_position'] = alien_1['x_position'] + x_increment

# print(f"New position: {alien_1['x_position']}")

# Removing Key_Value pairs
alien_3 = {'color': 'green', 'points': 5}
print(alien_3)

del alien_3['points']
print(alien_3)