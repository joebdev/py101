print(True) # True
print(False) # False

def make_longer(string, longer):
    if longer:
        return string + string
    else:
        return string
    
print(make_longer("abc", True)) # 'abcabc'
print(make_longer("xyz", False)) # 'xyz'

def is_digit(char):
    if '0' <= char <= '9':
        return True
    else:
        return False
    
print(is_digit('5')) # True
print(is_digit('a')) # False

value = True # or False
if value is True:
    print("It's true!")
elif value is False:
    print("It's false!")
else:
    print("It's not true or false!")

# Expressions and Conditionals
num = 5
if num < 10:
    print("Small number")
else:
    print("large number")

def is_small(number):
    return num < 10

num = 15
if is_small(num):
    print("small number")
else:
    print("large number")

# and Operator <-- both sides must evaluate to True or it returns false
print(True and True) # True
print(True and False) # False
print(False and False) # False

num = 5
print((num < 10) and (num > 3)) # True

# or Operator <-- one side must evaluate to True or it returns false
print(True or False) # True
print(True or True) # True
print(False or False) # False

# The not Operator <-- does the opposite of the value given
print(not True) # False
print(not False) # True

# Short-circuiting
name = 'Joe'

if name != None and name.isupper():
    print(f'Hi, {name}.')
else:
    print("Hello, whoever you are.")

