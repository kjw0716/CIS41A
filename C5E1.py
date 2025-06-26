#CIS41A C5E1 Jackie Wang junkaiwang0716@gmail.com 
#A program that compute  your pay and use three funciton
def get_input():# ask user to input his hours and rate
    company_name = input("Enter your company name")
    try:
        the_hours = float(input("Entyer Hours:"))
    except ValueError:
        print("Error, please enter numeric input")
    try:
        the_rate = float(input("Entyer rate:"))
    except ValueError:
        print("Error, please enter numeric input")
    return the_hours, the_rate

def compute_pay(the_hours,the_rate):# compute your pay
    if the_hours > 40:# check if need overpay
        return 40 * the_rate + (the_hours-40) * the_rate * 1.5
    else:
        return the_hours * the_rate
    
def print_output(pay):# output your pay
    print("pay is %.2f" %pay)

def main():# main function structure
    the_hours, the_rate = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    print_output(the_pay)

main()# run main
'''
Entyer Hours:45
Entyer Rates:10
pay is 475.00

Entyer Hours:30
Entyer Rates:15
pay is 450.00
'''