# program that asks the user for the first letter of their favorite rainbow color.
# the program returns the letter and the full color

def rainbow_color(char):
    if char.upper() == "R":
        print("R = Red")
    elif char.upper() == "O":
        print("O = Orange")
    elif char.upper() == "Y":
        print("Y = Yellow")
    elif char.upper() == "G":
        print("G = Green")
    elif char.upper() == "B":
        print("B = Biv")
    elif char.upper() == "I":
        print("I = Indigo")
    elif char.upper() == "V":
        print("V = Violet")
    else:
        print("no match")
        
color_letter = input("What's the first letter of your favorite rainbow color (ROYGBIV)?: ").upper()
rainbow_color(color_letter)
