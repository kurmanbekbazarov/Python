filename = 'learning_python.txt'

# 1st method of printing a file
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

# 2nd method
with open(filename) as f:
    for line in f:
        print(line.strip())

# 3rd method
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())