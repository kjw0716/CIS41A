def computePay(theDict):
    rate = theDict["rate"]
    hour = theDict["hour"]
    if hour > 40:
        total_pay = 40 * rate + (hour-40) * rate * 1.5
    else :
        total_pay = hour * rate

    theDict.update({
        "total_pay": total_pay
    })

    return theDict