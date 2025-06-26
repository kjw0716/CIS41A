'''
prompts the user to input their company name, hourly rate, and worked hours. It validates inputs, calculates total pay including overtime if hours exceed 40, and displays a formatted pay stub
'''
from getInputsFile import getInputs
from computePayFile import computePay
from printPayFile import printPay

def payProcess():
    '''
    This function is to process all other functions to get inputs,
    calculate and print the pay stub
    '''
    theDict = getInputs()
    theDict = computePay(theDict)
    printPay(theDict)

if __name__ == '__main__':
    payProcess()

'''
test1
Enter your company name: Instagram
Instagram is not in database, please try a new one.
Enter your company name: Twitter
Twitter is not in database, please try a new one.
Here's company list:
Amazon
Apple
Facebook
Google
Uber
Enter your company name: Amazon
Enter your rate: forty
Rate must be numeric.
Enter your rate: 40
Enter your hour: thirty
hour must be numeric.
Enter your hour: 30

====== PAY STUB ======
Company:       Amazon
Rate:           $40.00
Hours:          30.00
Regular pay:    $1200.00


test2
Enter your company name: Facebook
Enter your rate: -30
Rate must be a positive number.
Enter your rate: 30
Enter your hour: -45
hour must be a positive number.
Enter your hour: 45

====== PAY STUB ======
Company:       Facebook
Rate:           $30.00
Hours:          45.00
Regular pay:    $1425.00
'''