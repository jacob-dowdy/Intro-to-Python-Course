# program that uses nested if statements to decide on a level of greeting.

hello = input("Say 'Hello' (y/n)?")

if hello.lower() == 'n':
    print("(friendly nod)")
elif hello.lower() == 'y':
    hello2 = input("Full 'Hello'?")
    if hello2.lower() == 'y':
        print("Hello")
    elif hello2.lower() == 'n':
        print("Hi")
else:
    print("Greeting does not compute.")
