# Example 1
my_var = 1

def my_func():
    print(my_var) # output: 1

my_func()
# my_var on 2 and 5 are the same my_var variable

# Example 2
my_var = 1

def my_func():
    my_var = 2 # Creates a new variable named my_var, that has local scope inside the function

my_func()
print(my_var) # Output: 1

# Example 3
my_var = [1]

def my_func():
    my_var[0] = 2

my_func()
print(my_var) # Output: [2]

#Example 4
my_var = [1]

def my_func(my_var):
    my_var.append(2)

my_func(my_var)
print(my_var) # Output: [1, 2]
