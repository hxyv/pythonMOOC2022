# 1.1.1 Emoticon
# Please write a program which prints out an emoticon: :-)
print(":-)")

# 1.1.2 Fix the code: Seven Brothers
# This program is supposed to print out the names of the brothers in alphabetical order, but it's not working quite
# right yet. Please fix the program so that the names are printed in the correct order.
print("Aapo")
print("Eero")
print("Juhani")
print("Lauri")
print("Simeoni")
print("Timo")
print("Tuomas")

# 1.1.3 Row, Row, Row Your Boat
# Please write a program which prints out the following lines exactly as they are written here, punctuation and all:
print("Row, row, row your boat,")
print("Gently down the stream.")
print("Merrily, merrily, merrily, merrily,")
print("Life is but a dream.")

# 1.1.4 Minutes in a year
# Please write a program which prints out the number of minutes in a year. Use Python code to perform the calculation,
# as in the previous code example.
print("Minutes in a year:")
print(365 * 24 * 60) # 365 days, 24 hours in each day, 60 minutes in each hour

# 1.1.5 Print some code
# Please write a program which points out the following:
# print("Hello there!")
print('print("Hello there!")')

# 1.2.1 Name twice
# Please write a program which asks for the user's name and then prints it twice, on two consecutive lines.
name = input("What is your name?")
print(name)
print(name)

# 1.2.2 Name and exclamation marks
# Please write a program which asks for the user's name and then prints it out twice on a single line so that there is
# an exclamation mark at the beginning of the line, another between the two names and a third one at the end of the line.
name = input("What is your name?")
print("!" + name + "!" + name + "!")

# 1.2.3 Name and address
# Please write a program which asks for the user's name and address. The program should also print out the given
# information, as followers:
givenName = input("Given name: ")
familyName = input("Family name: ")
streetAddress = input("Street address: ")
cityCode = input("City and postal code: ")
print(givenName + " " + familyName + "\n" + streetAddress + "\n" + cityCode)

# 1.2.4 Fix the code: Utterances
# Here is a program which should ask for three htterances and print them out, like so:
part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1 + "-" + part2 + "-" + part3 + "!")

# 1.2.5 Story
# Please write a program which prints out the following story. The user gives a name and a year, which should be
# inserted into the printout.
name = input("Please type in a name: ")
year = input("Please type in a year: ")
print(name + " is a valiant knight, born in the year " + year + ". One morning " + name +
      " woke up to an awful racket: a dragon was approaching the village. Only " + name +
      " could save the village's residents.")
