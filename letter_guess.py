# letter guessing game

def check_guess(letter, guess):
    # check to ensure alpha
    if guess.isalpha() == False :
        print("invalid")
        return(guess.isalpha())
    elif guess.lower() > letter.lower():
        print("too high")
        #return guess.lower() == letter.lower()
    elif guess < letter:
        print("too low")
        #return guess.lower() == letter.lower()
    else:
        print("correct")
        #return guess.lower() == letter.lower()
        
# test for check_guess
user_guess = input("Guess a letter between A - Z: ").lower()

check_guess("k",user_guess)
