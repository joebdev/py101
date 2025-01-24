# START
# Given a collection of integers called 'numbers'

# SET iterator = 1
# SET savedNumber = value within numbers collection at space 1

# While iterator <= length of numbers
    # SET currentNumber = value within numbers collection at space "iterator"
    # IF currentNumber > savedNumber
        # savedNumber = currentNumber
    # iterator = iterator + 1

# PRINT savedNumber

def find_greatest(numbers):
    iterator = 0
    saved_number = numbers[0]

    while iterator < len(numbers):
        current_number = numbers[iterator]
        if current_number > saved_number:
            saved_number = current_number
        
        iterator += 1
    return saved_number


# START 
# Function that takes in two int params
# Function will need to add both int params together
# Function will need to return that value
# PRINT value

# START
# functionName(params)
    # add params together
    # return the result of those added params

# START
# function will need to accept a list parameter
# function will need a variable set to an empty string
# function will need to loop through the list parameter
# concat each list item to the empty str variable
# return str var

# functionName(list)
    # concat_str = ""
    # for item in list:
        # concat_str += item
    # PRINT concat_str

# def str_maker(list):
#     concat_str = ""
#     for item in list:
#         concat_str += item
#     print(concat_str)

# str_maker(['1', '2', '3', '4'])
# str_maker(['dog', 'cat', 'fish', 'squirrel'])


# START
# Function will need to accept a list param
# function will need a new list variable
# function will need an iterator variable to keep track of loop
# function will loop through the parameter
# function will go up by 2 on each loop, starting at first item
# append each item to new list variable
# PRINT new list variable

# functionName(list)
    # new_list = []
    # iterator = 0
    # while iterator < len(list):
        # new_list.append(list[iterator])
        # iterator += 2
    # PRINT new_list

# def every_other(list):
#     new_list = []
#     iterator = 0
#     while iterator < len(list):
#         new_list.append(list[iterator])
#         iterator += 2
#     print(new_list)

# every_other([1, 5, 7, 2, 5])


# START
# function that takes in two parameters, a str, and a char
# a variable that will act as a counter
# loop through the string if char is found, add 1 to counter
# if counter == 3, then we will just return the current index
# if counter never reaches 3, just return None

# functionName(str, char)
    # counter = 0
    # str_list = list(str)
    # for letter in str:
        # if str[letter] == char:
            # counter += 1
        
        # if counter == 3:
            # PRINT letter
    # PRINT NONE

# def letter_occurence(str, char):
#     count = 0
#     for index, letter in enumerate(str):
#         if letter is char:
#             count += 1
        
#         if count == 3:
#             return index
        
#     return None

# print(letter_occurence("appple", "p"))