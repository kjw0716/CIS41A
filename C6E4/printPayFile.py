def printPay(theDict):
    print("\n====== PAY STUB ======")
    print("Company:      ", theDict["company_name"])
    print(f"Rate:           ${theDict['rate']:.2f}")
    print(f"Hours:          {theDict['hour']:.2f}")
    print(f"Regular pay:    ${theDict['total_pay']:.2f}")