#program that asks a user about their pet.

about_pet = input("What kind of pet do you have?").lower()

if about_pet == "dog":
    print("Nice! I love doggos!")
elif about_pet == "cat":
    print("Meooww!")
elif about_pet == "fish":
    print("Swimmies!")
else:
    print("Cool pet!")
    
print("Thanks for sharing!")
