# 1. 
numbers = [1, 2, 3, 4, 5]
# numbers.clear()
del numbers[:]
print(numbers)

# 2. 
print([1, 2, 3] + [4, 5]) # output [1, 2, 3, 4, 5]

# 3. 
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1) # hello there

# 4. 
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1) # output: 42

# 5. 
def is_color_valid(color):
    return color == 'blue' or color == 'green'

def is_color_valid(color):
    return color in ['blue', 'green']