# program that adds user input until they enter a non-digit
sum = 0

while True:
    user_input = input("Give me some numbers to add together or enter a letter to quit: ").lower()
    if user_input.isalpha():
        print("Your sum is", sum)
        break
    if user_input.isdigit():
        sum += int(user_input)
    else:
        break
