# function that takes an argument and determines if alpha, small or big number
def str_analysis(arg):
    if str(arg).isdigit():
        if int(arg) > 99:
            print("That's a big number")
        else:
            print("That's a small number")
    elif arg.isalpha():
        print("Entry is alpha")
    else:
        print("Entry is neither all alpha nor all digit")

str_analysis(80)
