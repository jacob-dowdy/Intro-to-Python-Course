# created while practicing elif statements

# shirt sale program that asks user for their shirt size and responds with the price for that shirt
size = input("Which size shirt would you like?: ")

if size.lower() == "s":
    print("Small = $6")
elif size.lower() == "m":
    print("Medium = $7")
elif size.lower() == "l":
    print("Large = $8")
elif size.lower() == "xl":
    print("X-Large = $9")
# if requested shirt size isn't found
else:
    print("Sorry. We don't have that size.")
