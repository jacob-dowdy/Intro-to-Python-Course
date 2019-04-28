# a program that takes user input to make a long number
# enter a non-digit to see the final number
long_num = ""
int_num = input("Please enter a number: ")

while int_num.isdigit():
    long_num += int_num
    int_num = input("Please make the number longer. Enter a letter to stop the program: ")
    
print(long_num)
