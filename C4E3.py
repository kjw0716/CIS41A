#CIS41A Jackie Wang junkaiwang0716@gmail.com this is a programm that can calculate the sum of digits of an input number.
num = input("Enter an integer number: ")# Ask the user to enter an integer number

if num.isdigit(): # Check if the input is numeric
    total=0
    for i in num:
        total += int(i)
    print("Sum :", total)
else:
    print("Please enter a positive integer number.")
'''
Enter an integer number: 1729
Sum : 19

Enter an integer number: 6829
Sum : 25
'''
