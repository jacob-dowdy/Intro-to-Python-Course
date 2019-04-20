# searches for availability of a type of bird based on user input

# [ ] create function bird_available
def bird_available(bird):
    bird_types = 'crow robin parrot eagle sandpiper hawk piegon'
    return bird.lower() in bird_types
# [ ] user input
user_bird = input("Enter a type of bird you're looking for: ")
# [ ] call bird_available
have_bird = bird_available(user_bird)
# [ ] print availbility status
print(user_bird,"availability is",have_bird)
