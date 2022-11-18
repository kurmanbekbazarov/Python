# Using two askerisks (**) (exponents) to print 10 square numbers into a list.
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# Using min(), max(), and sum() function
# print(min(squares))
# print(max(squares))
# print(sum(squares))

# Using list comprehension to generate the same code from line 2 to 6
squares_2 = [value ** 2 for value in range(1, 11)]
print(squares_2)