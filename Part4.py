# 4.1.1 Hello Visual Studio Code
# Please write a program which asks the user which editor they are using. The
# program should keep on asking until the user types in Visual Studio Code. If
# the user types in Word or Notepad, the program counters with awful. Other
# unacceptable editor choices receive the reply not good. The program should be
# case-insensitive in its reactions. That is, the same user input in lowercase,
# uppercase or mixed case should trigger the same reaction:
while True:
    editor = input("editor: ").lower()
    if editor == "visual studio code":
        print("an excellent choice!")
        break
    elif editor == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")

# 4.2.1 Line
# Please write a function named `line`, which takes two arguments: an integer
# and a string. The function prints out a line of text, the length of which is
# specified by the first argument. The character used to draw the line should be
# the first character in the second argument. If the second argument is an empty
# string, the line should consist of stars.
def line(length, text):
    if text == "":
        print("*" * length)
    else:
        print(text[0] * length)

# 4.2.2 A box of hashes
# Please write a function named box_of_hashes, which prints out a rectangle of
# hash characters. The function takes one argument, which specifies the height
# of the rectangle. The rectangle should be ten characters wide.
#
# The function should call the function line from the exercise above for the
# actual printing out. Copy your solution to that exercise above the code for
# this exercise. Please don't change anything in your line function.
def box_of_hashes(height):
    # You should call function line here with proper parameters
    count = 1
    while count <= height:
        line(10, "#")
        count += 1
        
        
def line(length, text):
    if text == "":
        print("*" * length)
    else:
        print(text[0] * length)

# 4.2.3 Square of hashes
# Please write a function named square_of_hashes, which draws a square of hash 
# characters. The function takes one argument, which determines the length of 
# the side of the square.
#
# The function should call the function line from the exercise above for the 
# actual printing out. Copy your solution to that exercise above the code for 
# this exercise. Please don't change anything in the line function.
def line(length, text):
    if text == "":
        print("*" * length)
    else:
        print(text[0] * length)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    count = 1
    while count <= size:
        line(size, "#")
        count += 1

# 4.2.4 A square
# Please write a function named square, which prints out a square of characters,
#  and takes two arguments. The first parameter specifies the length of the side 
# of the square. The second parameter specifies the character used to draw the
#  square.
#
# The function should call the function line from the exercise above for the 
# actual printing out. Copy your solution to that exercise above the code for 
# this exercise. Please don't change anything in the line function.
def line(length, text):
    if text == "":
        print("*" * length)
    else:
        print(text[0] * length)

def square(size, character):
    # You should call function line here with proper parameters
    count = 1
    while count <= size:
        line(size, character)
        count += 1

# 4.2.5 A triangle
# Please write a function named triangle, which draws a triangle of hashes, and 
# takes one argument. The triangle should be as tall and as wide as the value of 
# the argument.

# The function should call the function line from the exercise above for the 
# actual printing out. Copy your solution to that exercise above the code for
#  this exercise. Please don't change anything in the line function.
def line(length, text):
    if text == "":
        print("*" * length)
    else:
        print(text[0] * length)

def triangle(size):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
        line(i, "#")
        i += 1

# 4.2.6 A shape
# Please write a function named shape, which takes four arguments. The first two 
# parameters specify a triangle, as above, and the character used to draw it. 
# The first parameter also specifies the width of a rectangle, while the third
#  parameter specifies its height. The fourth parameter specifies the filler
#  character of the rectangle. The function prints first the triangle, and then 
# the rectangle below it.

# The function should call the function line from the exercise above for the 
# actual printing out. Copy your solution to that exercise above the code for 
# this exercise. Please don't change anything in the line function.
def line(length, text):
    if text == "":
        print("*" * length)
    else:
        print(text[0] * length)

def shape(size1, char1, size2, char2):
    count = 1
    # Triangle
    while count <= size1:
        line(count, char1)
        count += 1
    
    # Rectangle
    count = 1
    while count <= size2:
        line(size1, char2)
        count += 1

# 4.2.7 A spruce
# Please write a function named spruce, which takes one argument. The function 
# prints out the text a spruce!, and the a spruce tree, the size of which is 
# specified by the argument.
def spruce(size):
    print("a spruce!")
    i = 1
    j = size
    while i <= size:
        print(" " * (j - 1) + "*" * (2 * i - 1))
        j -= 1
        i += 1
    print(" " * (size - 1) + "*")

# 4.2.8 Greatest number
# Please write a function named greatest_number, which takes three arguments.
# The function returns the greatest in value of the three.
def greatest_number(a, b, c):
    if a == b and a == c:
        return a
    elif a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
    
# 4.2.9 Same characters
# Please write a function named same_chars, which takes one string and two 
# integers as arguments. The integers refer to indexes within the string. The 
# function should return True if the two characters at the indexes specified are 
# the same. Otherwise, and especially if either of the indexes falls outside the 
# scope of the string, the function returns False.
def same_chars(text, index1, index2):
    length = len(text)
    if index1 > length -1 or index2 > length - 1:
        return False
    
    if text[index1] == text[index2]:
        return True
    else:
        return False

# 4.2.10 First, second, and last words
# Please write three functions: first_word, second_word and last_word. Each 
# function takes a string argument.
# 
# As their names imply, the functions return either the first, the second or the 
# last word in the sentence they receive as their string argument.
#
# In each case you may assume the argument string contains at least two separate
#  words, and all words are separated by exactly one space character. There will 
# be no spaces in the beginning or at the end of the argument strings.
def first_word(text):
    index = text.find(" ")
    return text[0:index]

def second_word(text):
    text = text + " "
    index = text.find(" ")
    text = text[(index + 1):]

    index = text.find(" ")
    return text[0:index]

def last_word(text):
    while True:
        index = text.find(" ")
        if index == -1:
            return text

        text = text[(index + 1):]

# 4.3.1 Change the value of an item
# Please write a program which initializes a list with the values 
# [1, 2, 3, 4, 5]. Then the program should ask the user for an index and a new 
# value, replace the value at the given index, and print the list again. This 
# should be looped over until the user gives -1 for the index. You can assume 
# all given index values will fall within your list.
my_list = [1, 2, 3, 4, 5]
index = 0
while True:
    index = int(input("Index: "))
    
    if index == -1:
        break

    value = int(input("New value: "))
    my_list[index] = value
    print(my_list)

# 4.3.2 Add items to a list
# Please write a program which first asks the user for the number of items to 
# be added. Then the program should ask for the given number of values, one by 
# one, and add them to a list in the order they were typed in. Finally, the list
# is printed out.
item = int(input("How many items: "))
index = 0
my_list = []
while index < item:
    my_list.append(int(input(f"Item {index + 1}: ")))
    index += 1
print(my_list)

# 4.3.3 Addition and removal
# Please write a program which asks the user to choose between addition and 
# removal. Depending on the choice, the program adds an item to or removes an
#  item from the end of a list. The item that is added must always be one 
# greater than the last item in the list. The first item to be added must be 1.
#
# The list is printed out in the beginning and after each operation.
my_list = []
while True:
    length = len(my_list)
    print("The list is now", my_list)
    choice = input("a(d)d, (r)emove or e(x)it: ")

    if choice == "x":
        print("Bye!")
        break
    
    if choice == "d":
        value = length + 1
        my_list.append(value)
    
    if choice == "r":
        my_list.pop(length - 1)
    
# 4.3.4 Same word twice
# Please write a program which asks the user for words. If the user types in a 
# word for the second time, the program should print out the number of different
#  words typed in, and exit.
my_list = []
while True:
    word = input("Word: ")
    if word in my_list:
        print(f"You typed in {len(my_list)} different words")
        break
    else:
        my_list.append(word)

# 4.3.5 List twice
# Please write a program which asks the user to type in values and adds them to 
# a list. After each addition, the list is printed out in two different ways:
# - in the order the items were added
# - ordered from smallest to greatest
# The program exits when the user types in 0.
my_list = []
while True:
    item = input("New item: ")

    if item == "0":
        print("Bye!")
        break

    my_list.append(int(item))
    print("The list now:", my_list)
    print("The list in order:", sorted(my_list))

# 4.3.6 The length of a list
# Please write a function named length which takes a list as its argument and
# returns the length of the list.
def length(my_list: list):
    return len(my_list)

# 4.3.7 Arithmetic mean
# Please write a function named mean, which takes a list of integers as an
# argument. The function returns the arithmetic mean of the values in the list.
def mean(my_list: list):
    return sum(my_list) / len(my_list)

# 4.3.8 The range of a list
# Please write a function named range_of_list, which takes a list of integers as 
# an argument. The function returns the difference between the smallest and the 
# largest value in the list.
def range_of_list(my_list: list):
    return max(my_list) - min(my_list)

# 4.4.1 Star-studded
# Please write a program which asks the user to type in a string. The program 
# then prints each input character on a separate line. After each character 
# there should be a star (*) printed on its own line.
input_string = input("Please type in a string: ")
for character in input_string:
    print(character)
    print("*")

# 4.4.2 From negative to positive
# Please write a program which asks the user for a positive integer N. The 
# program then prints out all numbers between -N and N inclusive, but leaves out 
# the number 0. Each number should be printed on a separate line.
value = int(input("Please type in a positive integer： "))
for i in range(-value, 0):
    print(i)
for i in range(1, value + 1):
    print(i)

# 4.4.3 List of stars
# Please write a function named list_of_stars, which takes a list of integers as 
# its argument. The function should print out lines of star characters. The 
# numbers in the list specify how many stars each line should contain.
def list_of_stars(my_list: list):
    for item in my_list:
        print("*" * item)

# 4.4.4 Anagrams
# Please write a function named anagrams, which takes two strings as arguments. 
# The function returns True if the strings are anagrams of each other. Two words
# are anagrams if they contain exactly the same characters.
def anagrams(str1: str, str2: str):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# 4.4.5 Palindromes
# Please write a function named palindromes, which takes a string argument and
# returns True if the string is a palindrome. Palindromes are words which are 
# spelled exactly the same backwards and forwards.
def palindromes(word: str):
    return word == word[::-1]

while True:
            word = input("Please type in a palindrome: ")
            if palindromes(word):
                print(f"{word} is a palindrome!")
                break
            else:
                print("that wasn't a palindrome")
                
# 4.4.6 The sum of positive numbers
# Please write a function named `sum_of_positives`, which takes a list of 
# integers as its argument. The function returns the sum of the positive values
# in the list.
def sum_of_positives(my_list : list):
    positives = []
    for item in my_list:
        if item > 0:
            positives.append(item)
    
    return(sum(positives))

# 4.4.7 Even numbers
# Please write a function named even_numbers, which takes a list of integers as
#  an argument. The function returns a new list containing the even numbers from 
# the original list.
def even_numbers(my_list : list):
    even = []

    for item in my_list:
        if item % 2 == 0:
            even.append(item)
    
    return(even)

# 4.4.8 The sum of lists
# Please write a function named list_sum which takes two lists of integers as 
# arguments. The function returns a new list which contains the sums of the 
# items at each index in the two original lists. You may assume both lists have
# the same number of items.
def list_sum(list1 : list, list2 : list):
    sum_list = []
    
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return(sum_list)

# 4.4.9 Distinct numbers
# Please write a function named distinct_numbers, which takes a list of integers 
# as its argument. The function returns a new list containing the numbers from 
# the original list in order of magnitude, and so that each distinct number is 
# present only once.
def distinct_numbers(my_list : list):
    new = []
    
    for item in my_list:
        if item not in new:
            new.append(item)

    return(sorted(new))

# 4.4.10 The length of the longest in the list
# Please write a function named `length_of_longest`, which takes a list of
# strings as its argument. The function returns the length of the longest string.
def length_of_longest(my_list : list):
    length = 0
    for item in my_list:
        if len(item) > length:
            length = len(item)
    
    return(length)

# 4.4.11 The shortest in the list
# Please write a function named shortest, which takes a list of strings as its
# argument. The function returns whichever of the strings is the shortest. If 
# more than one are equally short, the function can return any of the shortest 
# strings (there will be no such situation in the tests). You may assume there 
# will be no empty strings in the list.
def shortest(my_list : list):
    length = len(my_list[0])
    shorter = ""
    for item in my_list:
        if length > len(item):
            length = len(item)
            shorter = item
    return(shorter)

# 4.4.12 All the longest in the list
# Please write a function named all_the_longest, which takes a list of strings 
# as its argument. The function should return a new list containing the longest 
# string in the original list. If more than one are equally long, the function 
# should return all of the longest strings.The order of the strings in the 
# returned list should be the same as in the original.
def all_the_longest(my_list : list):
    length = 0
    longer = []
    for item in my_list:
        if length == len(item):
            longer.append(item)
        elif length < len(item):
            length = len(item)
            longer = []
            longer.append(item)
    return(longer)

# 4.5.1 Integer to strings
# Please write a function named formatted, which takes a list of floating point 
# numbers as its argument. The function returns a new list, which contains each 
# element of the original list in string format, rounded to two decimal points. 
# The order of the items in the list should remain unchanged.
#
# Hint: use f-strings to format the floating point numbers into suitable strings.
def formatted(my_list : list):
    new = []
    for item in my_list:
        newItem = f"{item:.2f}"
        new.append(newItem)
    return(new)












