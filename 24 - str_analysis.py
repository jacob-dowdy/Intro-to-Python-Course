# a program that gathers and qualifies user input.
def str_analysis(arg):
    while arg.lower() == "":
        arg = input("Enter a number or integer: ")
    else:
        if arg.lower().isdigit():
            if int(arg) > 99:
                print("That's a big number!")
            elif int(arg) < 99:
                print("That's a small number!")
        elif arg.lower().isalpha():
            print("This string is alphabetic.")
        # this covers strings that contain " " or "."
        else:
            print("This string contains multiple character types. It is neither all alpha nor all digit.")
            
str_analysis(input("Enter a number or integer: "))
