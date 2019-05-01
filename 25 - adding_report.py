# report that adds user-entered numbers together
def adding_report(report="T"):
    total = 0
    items = "\nItems:\n"
    while True:
        user_input = input("Please enter an integer or \"Q\" to quit: ")
        if user_input.isdigit():
          total += int(user_input)
          items += str(user_input) + "\n"
        elif user_input.isdigit() and report.upper() == "A":
            items += str(user_input) + "\n"
        elif user_input.isdigit() == False:
            # checking for the 'quit' entry
            if user_input.upper() == "Q" or user_input.lower().startswith("q"):
                if report.upper() == "A":
                    print(items) 
                    print("Total:\n", total) 
                    break
                elif report.upper() == "T":
                    print("Total:\n",total)
                    break
            else:
                print("Input is invalid")
# calling the function with 'All' selected. Will show a list of the items added.
adding_report("A")
