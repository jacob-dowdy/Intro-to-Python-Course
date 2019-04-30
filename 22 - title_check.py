# program that checks if a user entry is title cased. Asks for rentry until titlecased.
while True:
    user_title = input("Can you give me a title?: ")
    if user_title.istitle():
        print("Cool title.")
        break
    else:
        print("Try again")
