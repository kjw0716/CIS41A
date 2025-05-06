#CIS41A C2E1 Jackie Wang junkaiwang0716@gmail.com a program that compute gross pay included overpay check

hours = float(input("Enter Hours: "))# Prompt the user for input hours
rate = float(input("Enter Rate: "))# Prompt the user for input rate

pay = hours * rate #compute pay
if hours > 40:#check if need overpay
    pay = rate * 40 + (hours - 40) * rate * 1.5
    print("Your Pay is", pay)# Print the result
else:
    print("Your Pay is", pay)# Print the result


'''
output1:
Enter Hours: 30
Enter Rate: 10
Your Pay is 300.0

output2:
Enter Hours: 60
Enter Rate: 15
Your Pay is 1050.0
'''
    