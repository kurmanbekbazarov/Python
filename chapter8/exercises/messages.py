# 8-9. Messages: Make a list containing a series of short text messages. Pass the 
# list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    for message in messages:
        print(f"This is the message {message}.")

messages = ['SOS', '911', 'HELP']
show_messages(messages)
