#company database list
COMPANYLIST = ["Amazon", "Apple", "Facebook", "Google", "Uber"]

def getInputs():
    count = 0
    company_name = None

    while company_name is None:
        name = input("Enter your company name: ")
    
        if name in COMPANYLIST:
            company_name = name
        else:
            count += 1
            print(name, "is not in database, please try a new one.")

            if count >= 2:
                print("Here's company list:")
                for company in COMPANYLIST:
                    print(company)

    while True:
        rate_str = input("Enter your rate: ")
        try:
            rate = float(rate_str)
            if rate > 0:
                break
            print("Rate must be a positive number.")
        except ValueError:
            print("Rate must be numeric.")


    while True:
        hour_str = input("Enter your hour: ")
        try:
            hour = float(hour_str)
            if hour > 0:
                break
            print("hour must be a positive number.")
        except ValueError:
            print("hour must be numeric.")

    return {"company_name": company_name, "rate": rate, "hour": hour}