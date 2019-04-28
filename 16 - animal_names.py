# program that asks a user to enter 4 animal names
animal_name = ""
num_animals = 0
all_animals = str("")

while num_animals < 4:
    animal_name = input("Can you name an animal? You can exit early by typing 'exit': ").lower()
    num_animals += 1
    if animal_name == 'exit':
        print("Exiting program...")
        break
    else:
        all_animals = all_animals + animal_name + "\n"
print(all_animals)
