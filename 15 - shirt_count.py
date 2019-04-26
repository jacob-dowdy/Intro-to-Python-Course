# program that takes the shirt order for a user
# program can be exited by typing 'exit'
small_shirts = 0
medium_shirts = 0
large_shirts = 0

while True:
    size_entry = input("Please enter a size (S,M,L): ").capitalize()
    
    if size_entry.lower() == "exit":
        print("You've got",small_shirts,"smalls,",medium_shirts,"mediums, and",large_shirts,"larges.")
        break
    elif size_entry == "S":
        small_shirts += 1
    elif size_entry == "M":
        medium_shirts += 1
    elif size_entry == "L":
        large_shirts +=1
    else:
        print("Please enter a valid shirt type")
        
# test output
'''Please enter a size (S,M,L): S
Please enter a size (S,M,L): M
Please enter a size (S,M,L): S
Please enter a size (S,M,L): L
Please enter a size (S,M,L): exit
You've got 2 smalls, 1 mediums, and 1 larges. '''      
       
