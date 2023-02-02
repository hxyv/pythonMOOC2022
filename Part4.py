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














