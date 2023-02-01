# 3.1.1 Print the numbers
# Please write a program which prints out all the even numbers between two and
# thirty, using a loop. Print each number on a separate line.
number = 2
while number <= 30:
    if number % 2 == 0:
        print(number)
    number += 1

# 3.1.2 Fix the code: Countdown
print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number -= 1
print("Now!")

# 3.1.3 Numbers
# Please write a program which asks the user for a number. The program then prints
# out all integer numbers greater than zero but smaller than the input.
max = int(input("Upper limit: "))
numb = 1
while numb < max:
    print(numb)
    numb += 1

# 3.1.4 Power of two
# Please write a program which asks the user to type in an upper limit. The program
# then prints out numbers so that each subsequent number is the previous one doubled,
# starting from the number 1. That is, program prints out powers of two in order.
max = int(input("Upper limit: "))
num = 0
while 2 ** num <= max:
    print(2 ** num)
    num += 1

# 3.1.5 Powers of base n
# Please change the program from the previous exercise so that the user gets to
# input also the base which is multiplied (in the previous program the base was
# always 2).
max = int(input("Upper limit: "))
base = int(input("Base: "))
num = 0
while base ** num <= max:
    print(base ** num)
    num += 1

# 3.1.6 The sum of consecutive numbers, version 1
# Please write a program which asks the user to type in a limit. The program then
# calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is
# at least equal to the limit set by the user.
limit = int(input("Limit: "))

# Calculate the sum
num = 1
sum = 0
while sum < limit:
    sum += num
    num += 1
print(sum)

# 3.1.7 The sum of consecutive numbers, version 2
# Please write a new version of the program in the previous exercise.
limit = int(input("Limit: "))
num = 1
sum = 0
strings = ""
# Calculate the sum and create string
while sum + num < limit:
    strings += repr(num)
    strings += " + "
    sum += num
    num += 1

print(f"The consecutive sum: {strings}{num} = {sum + num}")

# 3.2.1 String multiplied
# Please write a program which asks the user for a string and an amount. The
# program then prints out the string as many times as specified by the amount.
# The printout should all be on one line, with no extra spaces or symbols added.
strings = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))
print(strings * amount)

# 3.2.2 The longer string
# Please write a program which asks the user for two strings and then prints out
# whichever is the longer of the two - that is, whichever has the more characters.
# If the strings are of equal length, the program should print out "The strings
# are equally long".
str1 = input("Please type in string 1: ")
len1 = len(str1)
str2 = input("Please type in string 2: ")
len2 = len(str2)

if len1 == len2:
    print("The strings are equally long")
elif len1 > len2:
    print(str1, "is longer")
else:
    print(str2, "is longer")

# 3.2.3 End to beginning
# Please write a program which asks the user for a string. The program then prints
# out the input string in reversed order, from end to beginning. Each character
# should be on a separate line.
input_string = input("Please type in a string: ")
index = len(input_string) - 1
while index >= 0:
    print(input_string[index])
    index -= 1

# 3.2.4 Second and second to last characters
# Please write a program which asks the user for a string. The program then prints
# out a message based on whether the second character and the second to last
# character are the same or not.
input_string = input("Please type in a string: ")
index = len(input_string) - 1
if input_string[1] == input_string[-2]:
    print("The second and the second to last characters are", input_string[1])
else:
    print("The second and the second to last characters are different")

# 3.2.5 A line of hashes
# Please write a program which prints out a line of hash characters, the width
# of which is chosen by the user.
width = int(input("Width: "))
print("#" * width)

# 3.2.5 A rectangle of hashes
# Please modify the previous program so that it also asks for the height, and
# prints out a rectangle of hash characters accordingly.
width = int(input("Width: "))
height = int(input("Height: "))
count = 1
while count <= height:
    print("#" * width)
    count += 1

# 3.2.6 Underlining
# Please write a program which asks the user for strings using a loop. The program
# prints out each string underlined as shown in the examples below. The execution
# ends when the user inputs an empty string - that is, just presses Enter at the
# prompt.
while True:
    input_string = input("Please type in a string: ")
    if input_string == "":
        break

    len_str = len(input_string)
    print(input_string + "\n" + "-" * len_str)

# 3.2.7 Right-aligned
# Please write a program which asks the user for a string and then prints it out
# so that exactly 20 characters are displayed. If the input is shorter than 20
# characters, the beginning of the line is filled in with `*` characters.
input_string = input("Please type in a string: ")
length = 20 - len(input_string)
if length == 0:
    print(input_string)
else:
    print("*" * length + input_string)

# 3.2.8 A framed word
# Please write a program which asks the user for a string and then prints out a
# frame of `*` characters with the word in the centre. The width of the frame
# should be 30 characters. You may assume the input string will always fit
# inside the frame. If the length of the input string is an odd number, you may
# print out the word in either of the two possible centre locations.
input_string = input("Word: ")
length = len(input_string)

print("*" * 30)
if length % 2 == 0:
    space = int((28 - length) / 2)
    print("*" + " " * space + input_string + " " * space + "*")
else:
    space = int((27 - length) / 2)
    print("*" + " " * space + input_string + " " * (space + 1) + "*")
print("*" * 30)

# 3.2.9 Substrings, Part 1
# Please write a program which asks the user to type in a string. The program
# then prints out all the substrings which begin with the first character, from
# the shortest to the longest.
input_string = input("Please type in a string: ")
length = 1

while length <= len(input_string):
    print(input_string[0:length])
    length += 1

# 3.2.10 Substrings, part 2
# Please write a program which asks the user to type in a string. The program
# then prints out all the substrings which end with the last character, from the
# shortest to the longest.
input_string = input("Please type in a string: ")
length = len(input_string) - 1

while length >= 0:
    print(input_string[length:len(input_string)])
    length -= 1

# 3.2.11 Does it contain vowels
# Please write a program which asks the user to input a string. The program then
# prints out different messages if the string contains any of the vowels a, e or o.
input_string = input("Please type in a string: ")

if "a" in input_string:
    print("a found")
else:
    print("a not found")

if "e" in input_string:
    print("e found")
else:
    print("e not found")

if "o" in input_string:
    print("o found")
else:
    print("o not found")

# Suggested solution
string = input("Please type in a string: ")
vowels = "aeo"
index = 0

while index < len(vowels):
    vowel = vowels[index]
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1

# 3.2.12 Find the first substring
# Please write a program which asks the user to type in a string and a single
# character. The program then prints the first three character slice which begins
# with the character specified by the user. You may assume the input string is
# at least three characters long. The program must print out three characters,
# or else nothing. Pay special attention to when there are less than two characters
# left in the string after the first occurrence of the character looked for. In
# that case nothing should be printed out, and there should not be any indexing
# errors when executing the program.
input_word = input("Please type ina word: ")
length = len(input_word)
input_char = input("Please type in a character: ")

if input_word.find(input_char) > -1:
    index = input_word.find(input_char)
    if index <= length - 3:
        print(input_word[index:(index + 3)])

# 3.2.13 Find all the substrings
# Please make an extended version of the previous program, which prints out all
# the substrings which are at least three characters long, and which begin with
# the character specified by the user. You may assume the input string is at
# least three characters long.
input_word = input("Please type in a word: ")
input_char = input("Please type in a character: ")

while len(input_word) > 2:
    index = input_word.find(input_char)
    if index != -1 and index <= len(input_word) - 3:
        print(input_word[index:(index + 3)])
    else:
        break

    input_word = input_word[(index+1):]

# Suggested solution
word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = 0

while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index + 3])
    index += 1

# 3.2.14 The second occurrence
# Please write a program which finds the second occurrence of a substring. If
# there is no second (or first) occurrence, the program should print out a
# message accordingly. In this exercise the occurrences cannot overlap. For
# example, in the string aaaa the second occurrence of the substring aa is at
# index 2.
input_string = input("Please type in a string: ")
sub_str = input("Please type in a substring: ")
len_sub = len(sub_str)

index1 = input_string.find(sub_str)
index2 = input_string[(index1 + len_sub):].find(sub_str)
if index2 == -1:
    print("The substring does not occur twice in the string.")
else:
    index = index1 + index2 + len_sub
    print(f"The second occurrence of the substring is at index {index}.")

# 3.3.1 Multiplication
# Please write a program which asks the user for a positive integer number. The
# program then prints out a list of multiplication operations until both operands
# reach the number given by the user.
m = int(input("Please type in a number: "))
i = 1
while i <= m:
    j = 1
    while j <= m:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1

#  3.3.2 First letters of words
# Please write a program which asks the user to type in a sentence. The program
# then prints out the first letter of each word in the sentence, each letter on
# a separate line.
input_string = input("Please type in a sentence: ")
index = 0
while index != -1:
    print(input_string[0])
    print("index1 =", index)
    index = input_string.find(" ")
    print("index2 =", index)
    input_string = input_string[(index + 1):]

# Suggested solution
sentence = input("Please type in a sentence: ")

# Add a space at the start, to make handling sentence easier
sentence = " " + sentence

# Searching for indexes which are preceded by spaces
index = 1
while index < len(sentence):
    if sentence[index - 1] == " " and sentence[index] != " ":
        print(sentence[index])
    index += 1

# 3.3.3 Factorial
# Please write a program which asks the user to type in an integer number. If
# the user types in a number equal to or below 0, the execution ends. Otherwise
# the program prints out the factorial of the number. The factorial of a number
# involves multiplying the number by all the positive integers smaller than
# itself. In other words, it is the product of all positive integers less than
# or equal to the number. For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 =
# 120.
while True:
    factor = 1
    factorial = 1
    num = int(input("Please type in a number: "))
    if num <= 0:
        print("Thanks and bye!")
        break
    while factor <= num:
        factorial *= factor
        factor += 1
    print(f"The factorial of the number {num} is {factorial}")

# 3.3.4 Flip the pairs
# Please write a program which asks the user to type in a number. The program
# then prints out all the positive integer values from 1 up to the number.
# However, the order of the numbers is changed so that each pair or numbers is
# flipped. That is, 2 comes before 1, 4 before 3 and so forth. See the examples
# below for details.
num = int(input("Please type in a number: "))
i = 1
if num % 2 == 0:
    while i + 1 <= num:
        print(i + 1)
        print(i)
        i += 2
else:
    while i + 1 <= num:
        print(i + 1)
        print(i)
        i += 2
    print(num)

# 3.3.5 Taking turns
# Please write a program which asks the user to type in a number. The program
# then prints out the positive integers between 1 and the number itself,
# alternating between the two ends of the range as in the examples below.
num = int(input("Please type in a number: "))
index = 1

if num % 2 == 0:
    while index < num:
        print(index)
        index += 1
        print(num)
        num -= 1
else:
    while index < num:
        print(index)
        index += 1
        print(num)
        num -= 1
    print(num)

# 3.4.1 Seven Brothers
# Please write a function named `seven_brothers`. When the function is called, it
# should print out the names of the seven brothers in alphabetical order, as in
# the example below. See the similarly named exercise in part 1 for more details
# about the brothers.
def seven_brothers():
    print("Aapo\nEero\nJuhani\nLauri\nSimeoni\nTimo\nTuomas")

if __name__ == "__main__":
    seven_brothers()

# 3.4.2 The first character
# The exercise contains the outline of the function `first_character`. Please
# complete it so that it prints out the first character of the string it takes
# as its argument.
def first_character(text):
    print(text[0])

# 3.4.3 Mean
# Please write a function named `mean`, which takes three integer arguments. The
# function should print out the arithmetic mean of the three arguments.
def mean(a, b, c):
    print((a + b + c) / 3)

# 3.4.4 Print many times
# Please write a function named `print_many_times(text, times)`, which takes a
# string and an integer as arguments. The integer argument specifies how many
# times the string argument should be printed out:
def print_many_times(text, times):
    i = 1
    while i <= times:
        print(text)
        i += 1

# 3.4.5 A square of hashes
# Please write a function named `hash_square(length)`, which takes an integer
# argument. The function prints out a square of hash characters, and the
# argument specifies the length of the side of the square.
def hash_square(length):
    i = 1
    while i <= length:
        print("#" * length)
        i += 1

# 3.4.6 Chessboard
# Please write a function named `chessboard`, which prints out a chessboard made
# out of ones and zeroes. The function takes an integer argument, which specifies
# the length of the side of the board. See the examples below for details:
def chessboard(num):
    i = 1
    while i <= num:
        j = i
        while j < num + i:
            print(j % 2, end = "")
            j += 1
        i += 1
        print("")

# 3.4.7 A word squard
# Please write a function named `squared`, which takes a string argument and an
# integer argument, and prints out a square of characters as specified by the
# examples below.
def squared(text, range):
    length = len(text)
    i = 1
    j = 0
    count = 1

    while i <= range:
        k = 1

        while k <= range:
            if j == length:
                j = 0
            print(text[j], end="")
            j += 1
            count += 1
            k += 1

        j = (count - 1) % length
        i += 1
        print("")

# Suggested solution
def squared(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)