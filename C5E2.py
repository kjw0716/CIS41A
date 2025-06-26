#CIS41A C5E2 Jackie Wang junkaiwang0716@gmail.com 
#A program that compute gross pay included overpay check and check whether it's numeric input or not,
#Print the company's name, the hours, the rate, and the gross pay, and also a random number between 1000 to 2000 for their document numbers
import random
def get_input():# ask user to input his hours and rate
    company = input("Enter your company name:").strip()
    while True:
        try:
            hours = float(input("Enter Hours: ").strip())
            break
        except ValueError:
            print("Error, please enter numeric input")
    while True:
        try:
            rate = float(input("Enter Rate: ").strip())
            break
        except ValueError:
            print("Error, please enter numeric input")
    return company, hours, rate

def compute_pay(the_hours,the_rate):# compute your pay
    if the_hours > 40:# check if need overpay
        return 40 * the_rate + (the_hours-40) * the_rate * 1.5
    else:
        return the_hours * the_rate
    
def print_output(company, hours, rate,pay, doc):# output your pay
    print("\nCompany: %s" % company)
    print("Hours: %.2f" % round(hours,2))
    print("Rate: %.2f" % round(rate, 2))
    print("**********************************************")
    print("Your document number is:", doc)
    print(f"Your %s gross pay is %.2f dollars." %(company, (round(pay,2))))

def main():# main function structure
    the_compant,the_hours, the_rate = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    the_doc = random.randint(1000, 2000)#create a random number for document
    print_output(the_compant,the_hours, the_rate, the_pay, the_doc)

main()# run main
'''
Enter your company name:Google
Enter Hours: 45
Enter Rate: 10

Company: Google
Hours: 45.00
Rate: 10.00
**********************************************
Your document number is: 1303
Your Google gross pay is 475.00 dollars.

Enter your company name:   Apple
Enter Hours: 35
Enter Rate: 20

Company: Apple
Hours: 35.00
Rate: 20.00
**********************************************
Your document number is: 1614
Your Apple gross pay is 700.00 dollars.
'''