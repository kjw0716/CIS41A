#CIS41A C4E2 Jackie Wang junkaiwang0716@gmail.com 
#A program that compute gross pay included overpay check and check whether it's numeric input or not,
#Print the company's name, the hours, the rate, and the gross pay, and also a random number between 1000 to 2000 for their document numbers
import random

company = input("Enter your company name: ")
doc = random.randint(1000, 2000)#create a random number for document
while True:
    try:
        hours = float(input("Enter Hours: "))
        break#when get all input information right, break the loop
    except ValueError:#handle error
        print("Error, please enter numeric input")

while True:
    try:
        rate = float(input("Enter Rate: "))
        break#when get all input information right, break the loop
    except ValueError:#handle error
        print("Error, please enter numeric input")

if hours > 40:#check if need overpay
    pay = rate * 40 + (hours - 40) * rate * 1.5
else:
    pay = hours * rate #compute pay

print("\nCompany: %s" % company)
print("Hours: %.2f" % round(hours,2))
print("Rate: %.2f" % round(rate, 2))
print("**********************************************")
print("Your document number is:", doc)
print(f"Your %s gross pay is %.2f dollars." %(company, (round(pay,2))))
'''
output1:
Enter your company name: Apple
Enter Hours: 40
Enter Rate: 30

Company:Apple
Hours:40.00
Rate:30.00
**********************************************
Your document number is: 1593
Your Apple gross pay is 1200.00 dollars.

output2:
Enter your company name: Google
Enter Hours: forty
Error, please enter numeric input
Enter Hours: 40
Enter Rate: twenty
Error, please enter numeric input
Enter Rate: 20

Company:Google
Hours:40.00
Rate:20.00
**********************************************
Your document number is: 1350
Your Google gross pay is 800.00 dollars.

output3:
Enter your company name: Tesla
Enter Hours: 55
Enter Rate: twenty five
Error, please enter numeric input
Enter Rate: 25

Company:Tesla
Hours:55.00
Rate:25.00
**********************************************
Your document number is: 1989
Your Tesla gross pay is 1562.50 dollars.
'''