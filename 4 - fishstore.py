# program that takes a fish type and price and returns the info

def fishstore(fish,price):
    return "Fish Type: " + fish + " costs $" + price
    
fish_entry = input("Which kind of fish would you like to buy?: ")
price_entry = input("How much does it cost?: ")

print(fishstore(fish_entry,price_entry))
