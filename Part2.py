# 2.1.1 Fix the syntax
# The following program contains several syntactic errors. Please fix the program
# so that the syntax is in order and the program works as specified by the
# examples below.
number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print("Its value is now", number)
print(number, " must be my lucky number!")
print("Have a nice day!")

# 2.1.2 Number of characters
# The function `len` can be used to find out the length of a string, among other
# things. The function returns the number of characters in a string. Please write
# a program which asks the user for a word and then prints out the number of
# characters, if there was more than one typed in.
word = input("Please type in a word: ")
if len(word) > 1:
    print(f"There are {len(word)} letters in the word {word}")
print("Thank you!")

# 2.1.3 Typecasting
# Please write a program which asks the user for a floating point number and then
# prints out the integer part and the decimal part separately. Use the Python int
# function. You can assume the number given by the user is always greater than zero.
numb = float(input("Please type in a number: "))
print("Integer part:", int(numb))
print("Decimal part:", numb - int(numb))

# 2.2.1 Age of maturity
# Please write a program which asks the user for their age. The program should
# then print out a message based on whether the user is of age or not, using 18
# as the age of maturity.
age = int(input("How old are you? "))
if age < 18:
    print("You are not of age!")
else:
    print("You are of age!")

# 2.2.2 Greater than or equal to
# Please write a program which asks for two integer numbers. The program should
# then print out whichever is greater. If the numbers are equal, the program
# should print a different message.
num1 = int(input("Please type in the first number: "))
num2 = int(input("Please type in the second number: "))

if num1 == num2:
    print("The numbers are equal!")
else:
    print("The greater number was:", max(num1, num2))

# 2.2.3 The elder
# Please write a program which asks for the names and ages of two persons. The
# program should then print out the name of the elder.
print("Person 1:\n")
name1 = input("Name: ")
age1 = int(input("Age: "))
print("Person 2:\n")
name2 = input("Name: ")
age2 = int(input("Age: "))

if age1 > age2:
    print("The elder is " + name1)
elif age1 == age2:
    print(name1 + " and " + name2 + " are the same age")
else:
    print("The elder is " + name2)

# 2.2.4 Alphbetically last
# Please write a program which asks the user for two words. The program should
# then print out whichever of the two comes alphabetically last. You can assume
# all words will be typed in lowercase entirely.
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

if word1 == word2:
    print("You gave the same word twice.")
elif word1 > word2:
    print(word1, "comes alphabetically last.")
else:
    print(word2, "comes alphabetically last.")

# 2.3.1 Age check
# Please write a program which asks for the user's age. If the age is not plausible,
# that is, it is under 5 or something that can't be an actual human age, the program
# should print out a comment.
age = int(input("What is your age? "))
if age < 0 or age > 150:
    print("That must be a mistake")
elif age >= 0 and age < 5:
    print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {age} years old")

# 2.3.2 Nephews
# Please write a program which asks for the user's name. If the name is Huey,
# Dewey or Louie, the program should recognise the user as one of Donald Duck's
# nephews. In a similar fashion, if the name is Morty or Ferdie, the program
# should recognise the user as one of Mickey Mouse's nephews.
name = input("Please type in your name: ")
if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

# 2.3.3 Grades and points
# The table below outlines the grade boundaries on a certain university course.
# Please write a program which asks for the amount of points received and then
# prints out the grade attained according to the table.
point = int(input("How many points [0-100]: "))
if point < 0 or point > 100:
    print("Grade: impossible!")
elif point >= 0 and point < 50:
    print("Grade: fail")
elif point >= 50 and point < 60:
    print("Grade: 1")
elif point >= 60 and point < 70:
    print("Grade: 2")
elif point >= 70 and point < 80:
    print("Grade: 3")
elif point >= 80 and point < 90:
    print("Grade: 4")
else:
    print("Grade: 5")

# 2.3.4 FizzBuzz
# Please write a program which asks the user for an integer number. If the number
# is divisible by three, the program should print out Fizz. If the number is
# divisible by five, the program should print out Buzz. If the number is divisible
# by both three and five, the program should print out FizzBuzz.
num = float(input("Number: "))
if num % 3 == 0 and num % 5 != 0:
    print("Fizz")
elif num % 5 == 0 and num % 3 != 0:
    print("Buzz")
elif num % 15 == 0:
    print("FizzBuzz")

# 2.3.5 Leap year
# Generally, any year that is divisible by four is a leap year. However, if the
# year is additionally divisible by 100, it is a leap year only if it also
# divisible by 400. Please write a program which asks the user for a year, and
# then prints out whether that year is a leap year or not.
year = float(input("Please type in a year: "))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print("That year is not a leap year.")
    else:
        print("That year is a leap year.")
else:
    print("That year is not a leap year.")

# 2.3.6 Alphabetically in the middle
# Please write a program which asks the user for three letters. The program
# should then print out whichever of the three letters would be in the middle if
# the letters were in alphabetical order. You may assume the letters will be either
# all uppercase, or all lowercase.
a = input("1st letter: ")
b = input("2nd letter: ")
c = input("3rd letter: ")

if a < b:
    if c > b:
        print("The letter in the middle is", b)
    elif c < a:
        print("The letter in the middle is", a)
    else:
        print("The letter in the middle is", c)
else:
    if c > a:
        print("The letter in the middle is", a)
    elif c < b:
        print("The letter in the middle is", b)
    else:
        print("The letter in the middle is", c)

# 2.3.7 Gift tax calculator
gift = int(input("Value of gift: "))
if gift >= 5000:
    if gift < 25000:
        tax = 100 + (gift - 5000) * 0.08
    elif gift < 55000:
        tax = 1700 + (gift - 25000) * 0.1
    elif gift < 200000:
        tax = 4700 + (gift - 55000) * 0.12
    elif gift < 1000000:
        tax = 22100 + (gift - 200000) * 0.15
    else:
        tax = 142100 + (gift - 1000000) * 0.17
    print(f"Amount of tax: {tax} euros")
else:
    print("No tax!")

# 2.4.1 Shall we continue?
# Let's create a program along the lines of the example above. This program should
# print out the message "hi" and then ask "Shall we continue?" until the user inputs
# "no". Then the program should print out "okay then" and finish. Please have a
# look at the example below.
while True:
    print("hi")
    message = input("Shall we continue? ")
    if message == "no":
        print("okay then")
        break

# 2.4.2 Input validation
# Please write a program which asks the user for integer numbers. If the number
# is below zero, the program should print out the message "Invalid number". If
# the number is above zero, the program should print out the square root of the
# number using the Python `sqrt` function. In either case, the program should then
# ask for another number. If the user inputs the number zero, the program should
# stop asking for numbers and exit the loop.
from math import sqrt
while True:
    num = float(input("Please type in a number: "))
    if num < 0:
        print("Invalid number")
    elif num > 0:
        print(sqrt(num))
    else:
        print("Exiting...")
        break

# 2.4.3 Fix the code: Countdown
# This program should print out a countdown. The code is as follows:
number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number < 1:
    break

print("Now!")

# 2.4.4 Repeat password
# Please write a program which asks the user for a password. The program should
# then ask the user to type in the password again. If the user types in something
# else than the first password, the program should keep on asking until the user
# types the first password again correctly.
password = input("Password: ")
while True:
    repeat = input("Repear password: ")
    if repeat == password:
        print("User account created!")
        break
    else:
        print("They do not match!")

# 2.4.5 PIN and number of attempts
# Please write a program which keeps asking the user for a PIN code until they
# type in the correct one, which is 4321. The program should then print out the
# number of times the user tried different codes.
pin = "4321"
attempt = 0

while True:
    user = input("PIN: ")
    attempt += 1
    if user == pin:
        if attempt == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempt} attempts")
        break
    else:
        print("Wrong")

# 2.4.6 The next leap year
year = int(input("Year: "))
leap = year + 1

while True:
    if leap % 4 == 0:
        if leap % 100 != 0 or (leap % 100 == 0 and leap % 400 == 0):
            break
        else:
            leap += 1
    else:
        leap += 1

print(f"The next leap year after {year} is {leap}")

# 2.4.7 Story
# Part 1: Please write a program which keeps asking the user for words. If the
# user types in end, the program should print out the story the words formed,
# and finish.
# Part 2: Change the program so that the loop ends also if the user types in the
# same word twice.
story = ""
temp = " "
while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    elif temp == word:
        break
    else:
        story = story + " " + word
    temp = word
print(story)

# 2.4.8 Working with numbers
# Pre-task: Please write a program which asks the user for integer numbers. The
# program should keep asking for numbers until the user types in zero.
# Task 1: Count. After reading in the numbers the program should print out how
# many numbers were typed in. The zero at the end should not be included in the
# count. You will need a new variable here to keep track of the numbers typed in.
# Part 2: Sum. The program should also print out the sum of all the numbers typed
# in. The zero at the end should not be included in the calculation.
# Part 3: Mean. The program should also print out the mean of the numbers. The zero
# at the end should not be included in the calculation. You may assume the user
# will always type in at least one valid non-zero number.
# Part 4: Positives and negatives. The program should also print out statistics
# on how many of the numbers were positive and how many were negative. The zero
# at the end should not be included in the calculation.
print("Please type in integer numbers. Type in 0 to finish.")
num = 0
attempt = 0
sum = 0
positive = 0
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    sum += num
    if num > 0:
        positive += 1
    attempt += 1

print("...the program asks for numbers")
print("Numbers typed in", attempt)
print("The sum of the numbers is", sum)
print("The mean of the numbers is", sum / attempt)
print("Positive numbers", positive)
print("Negative numbers", attempt - positive)