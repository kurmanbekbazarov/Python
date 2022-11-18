# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean 
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When 
# you’re sure that your loop works, add five more Python terms to your glossary. 
# When you run your program again, these new words and meanings should 
# automatically be included in the output.


glossary = {
    'if': 'if condition',
    'lists': 'used to store elements',
    'tuples': 'used to store constant elements',
    'elif': 'else if condition',
    'else': 'else condition',
    'dictionary': 'used to store key and value',
    'key': 'unique item that is used to access the value',
    'value': 'element associated with the key',
    'in': 'checks whether a value exist in lists, tuples, dictionary',
    'set': 'built in python function that stores only the unique values',
}

for key, value in glossary.items():
    print(f"\n{key} and value {value}")