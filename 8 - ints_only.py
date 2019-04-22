# a program that asks a user to enter a number.

number = input("Give me a number: ")

if number.isdigit():
    number = int(number)
    # checks if number is greater than 100
    print("greater than 100 is",number > 100)
else:
    # message if not a digit
    print("only int is accepted")
