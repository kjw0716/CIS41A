#CIS41A C3E2 Jackie Wang junkaiwang0716@gmail.com a program that compute gross pay included overpay check and check if the input is right

'''
#Method isdigit
hours1 = input("Enter Hours(integer): ")# Prompt the user for input hours
rate1 = input("Enter Rate(integer): ")# Prompt the user for input rate

if hours1.isdigit() and rate1.isdigit():
    hours = int (hours1)
    rate = int (rate1)

    if hours > 40:#check if need overpay
        pay = rate * 40 + (hours - 40) * rate * 1.5
        print("Your Pay is", pay)# Print the result
    else:
        pay = hours * rate #compute pay
        print("Your Pay is", pay)# Print the result
else:
    print("not interger, pls try input again")
'''
#Method VALUEERROR
try:
    hours = float(input("Enter Hours: "))# Prompt the user for input hours
    rate = float(input("Enter Rate: "))# Prompt the user for input rate

    if hours > 40:#check if need overpay
        pay = rate * 40 + (hours - 40) * rate * 1.5
        print("Your Pay is", pay)# Print the result
    else:
        pay = hours * rate #compute pay
        print("Your Pay is", pay)# Print the result
except ValueError:#handle error
    print("ValueError")

'''
output1:
Enter Hours(integer): 45
Enter Rate(integer): 10
Your Pay is 475.0

output2:
Enter Hours(integer): 45
Enter Rate(integer): ten
ValueError

'''