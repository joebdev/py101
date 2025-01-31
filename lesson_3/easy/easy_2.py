# 1. 
numbers = [1, 2, 3, 4, 5]

reversed_numbers = numbers[::-1]
new_list = list(reversed(numbers))
print(reversed_numbers)
print(new_list)
print(numbers)

# 2. 
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)

# 3. 
42 in range(10, 101)
100 in range(10, 101)
101 in range(10, 101)

# 4. 
numbers = [1, 2, 3, 4, 5]
numbers.pop(2)
# or
del numbers[2]

# 5. 
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
print(type(numbers) is list)
print(type(table) is list)
# or
isinstance(numbers, list)
isinstance(table, list)

# 6. 
title = "Flintstone Family Members"
title.center(40)

# 7. 
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

letter_counter = [letter for letter in statement1 if letter == 't']
print(len(letter_counter))
# or 
statement1.count('t')

# 8.
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print('Spot' in ages)

# 9. 
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
# ages['Marilyn'] = 22
# ages['Spot'] = 237
# or
additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.update(additional_ages)
print(ages)