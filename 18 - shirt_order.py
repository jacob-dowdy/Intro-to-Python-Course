#program that places a shirt order for a customer. Shirt has to be blue or white and a certain size to actually place.

available = False
color_list = "white blue"
color = input("What color shirt would you like (white or blue)?: ").lower()
size = input("Which size shirt would you like?: ").lower()

while not available:
        if color not in color_list:
            print("color unavailable")
            break
        elif color == "white":
            if size == "m" or size == "l":
                print("available")
                print("One",size,color,"shirt coming up")
                available = True
            else:
                print("unavailable")
                break
        elif color == "blue":
            if size == "m" or size == "s":
                print("available")
                print("One",size,color,"shirt coming up")
                available = True
            else:
                print("unavailable")
                break
        else:
            print("Please choose a different color or size.")
