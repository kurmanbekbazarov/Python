# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the 
# function send_messages() with a copy of the list of messages. After calling the 
# function, print both of your lists to show that the original list has retained its 
# messages.

def show_messages(messages):
    for message in messages:
        print(f"This is the message {message}.")

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ['SOS', '911', 'HELP']
sent_messages = []
show_messages(messages)

send_messages(messages[:], sent_messages)
print(f"\n{messages}")
print(f"\n{sent_messages}")