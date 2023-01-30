# 1.1.1 Emoticon
# Please write a program which prints out an emoticon: :-)
print(":-)")

# 1.1.2 Fix the code: Seven Brothers
# This program is supposed to print out the names of the brothers in alphabetical
# order, but it's not working quite right yet. Please fix the program so that the
# names are printed in the correct order.
print("Aapo")
print("Eero")
print("Juhani")
print("Lauri")
print("Simeoni")
print("Timo")
print("Tuomas")

# 1.1.3 Row, Row, Row Your Boat
# Please write a program which prints out the following lines exactly as they
# are written here, punctuation and all:
print("Row, row, row your boat,")
print("Gently down the stream.")
print("Merrily, merrily, merrily, merrily,")
print("Life is but a dream.")

# 1.1.4 Minutes in a year
# Please write a program which prints out the number of minutes in a year. Use
# Python code to perform the calculation, as in the previous code example.
print("Minutes in a year:")
print(365 * 24 * 60) # 365 days, 24 hours in each day, 60 minutes in each hour

# 1.1.5 Print some code
# Please write a program which points out the following:
# print("Hello there!")
print('print("Hello there!")')

# 1.2.1 Name twice
# Please write a program which asks for the user's name and then prints it twice,
# on two consecutive lines.
name = input("What is your name?")
print(name)
print(name)

# 1.2.2 Name and exclamation marks
# Please write a program which asks for the user's name and then prints it out
# twice on a single line so that there is an exclamation mark at the beginning
# of the line, another between the two names and a third one at the end of the line.
name = input("What is your name?")
print("!" + name + "!" + name + "!")

# 1.2.3 Name and address
# Please write a program which asks for the user's name and address. The program
# should also print out the given information, as followers:
givenName = input("Given name: ")
familyName = input("Family name: ")
streetAddress = input("Street address: ")
cityCode = input("City and postal code: ")
print(givenName + " " + familyName + "\n" + streetAddress + "\n" + cityCode)

# 1.2.4 Fix the code: Utterances
# Here is a program which should ask for three htterances and print them out,
# like so:
part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1 + "-" + part2 + "-" + part3 + "!")

# 1.2.5 Story
# Please write a program which prints out the following story. The user gives a
# name and a year, which should be inserted into the printout.
name = input("Please type in a name: ")
year = input("Please type in a year: ")
print(name + " is a valiant knight, born in the year " + year + ". One morning " +
      name + " woke up to an awful racket: a dragon was approaching the village. Only " +
      name + " could save the village's residents.")

# 1.3.1 Extra space
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old\n\n"
      f"my skills are\n"
      f" - {skill1} ({level1})\n"
      f" - {skill2} ({level2})\n"
      f" - {skill3} ({level3})\n\n"
      f"I am looking for a job with a salary of {lower}-{upper} euros per month")

# 1.3.2 Arithmetics
x = 27
y = 15
print(f"{x} + {y} = {x + y}\n"
      f"{x} - {y} = {x - y}\n"
      f"{x} * {y} = {x * y}\n"
      f"{x} / {y} = {x / y}")

# 1.3.3 Fix the code: Print a single line
print(5, end = "")
print(" + ", end = "")
print(8, end = "")
print(" - ", end = "")
print(4, end = "")
print(" = ", end = "")
print(5 + 8 - 4, end = "")

# 1.4.1 Times five
# Write a program which asks the user for a number. The program then prints out
# the number multiplied by five.
number = int(input("Please type in a number: "))
print(f"{number} times 5 is {number * 5}")

# 1.4.2 Name and age
# Please write a program which asks the user for their name and year of birth.
name = input("What is your name? ")
year = int(input("Which year were you born? "))
print(f"Hi {name}, you will be {2021 - year} years old at the end of the year 2021")

# 1.4.3 Seconds in a day
# Please write a program which asks the user for a number of days. The program
# then prints out the number of seconds in the amount of days given.
day = int(input("How many days? "))
print(f"Seconds in that many days: {24 * 60 * 60 * day}")

# 1.4.4 Fix the code: Product
# This program asks the user for three numbers. The program then prints out their
# product, that is, the numbers multiplied by each other. There is, however,
# something wrong with the program - it doesn't work quite right, as you can see
# if you run it. Please fix it.
number = int(input("Please type in the first number: "))
number *= int(input("Please type in the second number: "))
number *= int(input("Please type in the third number: "))

print("The product is", number)

# 1.4.5 Sum and product
# Please write a program which asks the user for two numbers. The program will
# then print out the sum and the product of the two numbers.
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
print(f"The sum of the numbers: {num1 + num2}")
print(f"The product of the numbers: {num1 * num2}")

# 1.4.6 Sum and mean
# Please write a program which asks the user for four numbers. The program then
# prints out the sum and the mean of the numbers.
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
num4 = int(input("Number 4: "))
print(f"The sum of the numbers is {num1 + num2 + num3 + num4}"
      f" and the mean is {(num1 + num2 + num3 + num4) / 4}")

# 1.4.7 Food expenditure
#  Please write a program which estimates a user's typical food expenditure. The
# program asks the user how many times a week they eat at the student cafeteria.
# Then it asks for the price of a typical student lunch, and for money spent on
# groceries during the week. Based on this information the program calculates the
# user's typical food expenditure both weekly and daily.
cafeteria = int(input("How many times a week do you eat at the student cafeterai? "))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

print(f"Average food expenditure:\n"
      f"Daily: {(cafeteria * price + groceries) / 7} euros\n"
      f"Weekly: {cafeteria * price + groceries} euros")

# 1.4.8 Students in groups
# Please write a program which asks for the number of students on a course and
# the desired group size. The program will then print out the number of groups
# formed from the students on the course. If the division is not even, one of
# the groups may have fewer members than specified.
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

groups = (students + group_size - 1) // group_size

print("Number of groups formed:", groups)

# 1.5.1 Orwell
# Please write a program which asks the user for an integer number. The program
# should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.
number = input("Please type in a number: ")
if number == "1984":
      print("Orwell")

# 1.5.2 Absolute value
# Please write a program which asks the user for an integer number. If the number
# is less than zero, the program should print out the number multiplied by -1.
# Otherwise the program prints out the the number as is. Please have a look at
# the examples of expected behaviour below.
number = int(input("Please type in a number: "))
if number < 0:
      number = -number
print(f"The absolute value of this number is {number}")

# 1.5.3 Soup or no soup
# Please write a program which asks for the user's name. If the name is anything
# but "Jerry", the program then asks for the number of portions and prints out
# the total cost. The price of a single portion is 5.90.
name = input("Please tell me your name: ")
if name != "Jerry":
      portion = int(input("How many portions of soup? "))
      print(f"The total cost is {portion * 5.9}")
print("Next please!")

# 1.5.4 Order of magnitude
# Please write a program which asks the user for an integer number. The program
# should then print out the magnitude of the number according to the following
# examples.
number = float(input("Please type in a number: "))
if number < 1000:
      print("This number is smaller than 1000")
if number < 100:
      print("This number is smaller than 100")
if number < 10:
      print("This number is smaller than 10")
print("Thank you!")

# 1.5.5 Calculator
# Please write a program which asks the user for two numbers and an operation.
# If the operation is add, multiply or subtract, the program should calculate
# and print out the result of the operation with the given numbers. If the user
# types in anything else, the program should print out nothing.
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operator = input("Operation: ")

if operator == "add":
      print(f"{num1} + {num2} = {num1 + num2}")
if operator == "multiply":
      print(f"{num1} * {num2} = {num1 * num2}")
if operator == "subtract":
      print(f"{num1} - {num2} = {num1 - num2}")

# 1.5.6 Temperatures
# Please write a program which asks the user for a temperature in degrees
# Fahrenheit, and then prints out the same in degrees Celsius. If the converted
# temperature falls below zero degrees Celsius, the program should also print out
# "Brr! It's cold in here!". The formula for converting degrees Fahrenheit to
# degrees Celsius can be found easily by any search engine of your choice.
tempF = int(input("Please type in temperature (F): "))
tempC = (tempF - 32) * 5 / 9
print(f"{tempF} degrees Fahrenheit equals {tempC} degrees Celsius")
if tempC < 0:
      print("Brr! It's cold in here!")

# 1.5.7 Daily wages
# Please write a program which asks for the hourly wage, hours worked, and the
# day of the week. The program should then print out the daily wages, which equal
# hourly wage multiplied by hours worked, except on Sundays when the hourly wage
# is doubled.
wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")
daily_wages = wage * hours
if day == "Sunday":
      daily_wages *= 2
print(f"Daily wages: {daily_wages} euros")

# 1.5.8 Loyalty bonus
# This program calculates the end of year bonus a customer receives on their
# loyalty card. The bonus is calculated with the following formula:
# - If there are less than a hundred points on the card, the bonus is 10 %
# - In any other case the bonus is 15 %
points = int(input("How many points are on your card? "))
if points < 100:
      factor = 1.1
      print("Your bonus is 10 %")

if points >= 100:
      factor = 1.15
      print("Your bonus is 15 %")

# a *= b is the same thing as a = a * b
points *= factor
print("You now have", points, "points")

# 1.5.9 What to wear tomorrow
# Please write a program which asks for tommorrow's weather forecast and then
# suggests weather-appropriate clothing. The suggestion should change if the
# temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also
# if there is rain on the radar.
print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")
if temp <= 20:
      print("I recommend a jumper as well")
if temp <= 10:
      print("Take a jacket with you")
if temp <= 5:
      print("Make it a warm coat, actually\nI think gloves are in order")
if rain == "yes":
      print("Don't forget your umbrella!")

# 1.5.10 Solving a quadratic equation
# In the Python `math` module there is the function `sqrt`, which calculates the
# square root of a number. We will return to the concept of a module and the
# `import` statement latter. For now, it is sufficient to understand that the line
# `from math import sqrt` allows us to use the`sqrt` function in our program.
#
# Please write a program for solving a quadratic equation of the form ax^2+bx+c.
# The program asks for values a, b and c. It should then use the quadratic formula
# to solve the equation. The quadratic formula expressed with the Python `sqrt`
# function is as follows:
# x = (-b ± sqrt(b^2-4ac))/(2a).
# You can assume the equation will always have two real roots, so the above formula
# will always work.
# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

x1 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
x2 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)

print(f"The roots are {x1} and {x2}")