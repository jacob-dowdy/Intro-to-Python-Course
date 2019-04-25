# a program that asks the user to enter a familiar name (with no spaces)
familiar_name = ""

while True:
    familiar_name = input("Enter a familiar name (common name friends/family use): ")
    # test for name without spaces
    if familiar_name.isalpha():
        print("Hi,",familiar_name.title() + "!")
        break
    else:
        print("Try a name with no spaces.")
