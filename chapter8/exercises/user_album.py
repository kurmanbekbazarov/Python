# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that 
# information, call make_album() with the user’s input and print the dictionary 
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, quantity_songs=None):
    dictionary = {
        'name': artist_name,
        'album title': album_title,
    }
    if quantity_songs:
        dictionary['songs'] = quantity_songs
    return dictionary

Flag = True
prompt = "\nEnter an ablum's artist"
prompt += "\nOr type 'quit' to exit. "

while Flag:
    artist = input(prompt)
    title = input("\nEnter album's title ")
    
    proceed = input("\nWould you like to continue? (yes/no) ")
    if proceed == 'no':
        Flag = False

output = make_album(artist, title)
print(output)