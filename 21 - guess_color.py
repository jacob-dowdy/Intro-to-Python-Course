# program that gives a user 4 chances to name a rainbow color

num_guess = 4
rainbow = "red orange yellow green blue indigo violet"

while True:
    color_guess = input("Can you guess one of the colors in a rainbow?: ")
    if color_guess.lower() in rainbow:
        print("You got it right!")
        break
    else:
        print("Nope")
        num_guess -= 1
        if num_guess == 0:
            print("You're out of guesses. Better luck next time.")
            break
