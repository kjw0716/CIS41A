#Team Name: Python Enjoyers
#Date: 05/09/25
#Class: CIS41A
#Desc: Menu Driven Program fictional De Anza College Food Court using functions.


#CONSTANTS
#Names of the items on the menu.
MENU_OPTION_NAME_1 = "DeAnza Chicken Wings"
MENU_OPTION_NAME_2 = "DeAnza Beef Burger"
MENU_OPTION_NAME_3 = "DeAnza Chicken Burger"
MENU_OPTION_NAME_4 = "Fries"
MENU_OPTION_NAME_5 = "Sprite"
TAX_RATE = 9
DOLLAR ="$"
#Header of the menu.
SERIAL_NO = "No."
ITEM = "Item"
PRICE="Price"
OPTION_6=6
EXIT="Exit"
#Exit Message
EXIT_MESSAGE="Thank you, hope to see you again!"
#Input Messages.
INPUT_FOOD_ITEM ="Please enter your choice, a number between 1 and 5 to order and 6 to quit: "
INPUT_QUANTITY= "Please enter the quantity: "
INPUT_STUDENT_OR_STAFF = "If you are a student, enter 0. If you are a staff member, enter 1: "
#Error Messages.
ERROR_MESSAGE_IS_VALID_ITEM="Error, Please enter a valid choice, a number between 1 and 6."
ERROR_MESSAGE_IS_VALID_QUANTITY="Error, Please enter a valid choice."


#Global Map containing the Key - item number and value - a list of [itemName,price, quanity].
itemPriceAndQuantityMap = {1:[MENU_OPTION_NAME_1,6.99,0],
2:[MENU_OPTION_NAME_2,7.99,0],
3:[MENU_OPTION_NAME_3,5.00,0],
4:[MENU_OPTION_NAME_4,3.00,0],
5:[MENU_OPTION_NAME_5,1.00,0]}

def display_menu():
    """
    Displays 5 choices of food items that can be ordered.

    Parameters:
    None

    Returns:
    None
    """
    print()
    print("%-3s %-25s %s" % (SERIAL_NO, ITEM, PRICE))
    print("-"*40)
    for key in itemPriceAndQuantityMap:
        name = itemPriceAndQuantityMap[key][0]
        price = itemPriceAndQuantityMap[key][1]
        print("%-3s %-25s %s%.2f" % (key, name, DOLLAR , price))
    print("%-3s %-25s" %(OPTION_6, EXIT))
    print()

def call_exit():
    """
    This program exits when 6 is entered at the very beginning.

    Parameters:
    None

    Returns:
    None
    """
    print(EXIT_MESSAGE)
    exit()

def isItemValid(itemNum):
    """
    Validates the food choice entered. Checks to see if the number
    is a digit between 1 and 6. If the choice is not valid, throws an error message.

    Parameters:
    itemNum (str): The food choice number entered by the user.
    
    Returns:
    bool: True if the choice is valid, False otherwise.
    """
    isValid = False
    if itemNum.isdigit() and int(itemNum) >= 1 and int(itemNum) <= 6:
        isValid = True
    else:
        print(ERROR_MESSAGE_IS_VALID_ITEM)
    return isValid    
    
def isQuantityValid(itemQuantity):
    """
    Validates that the quantity is a positive whole number.
    If the choice is not valid, throws an error message.

    Parameters:
    itemNum (str): The food quantity entered by the user.
    
    Returns:
    bool: True if the choice is valid, False otherwise.
    """
    isValid = False
    if itemQuantity.isdigit() and int(itemQuantity) > 0:
        isValid = True
    else:
        print(ERROR_MESSAGE_IS_VALID_QUANTITY)
    return isValid

def order_food():
    order_count = 0
    #While loop to let the user keep entering the food choice until 6 is entered.
    while True:
        itemNum = input(INPUT_FOOD_ITEM)  
        if not isItemValid(itemNum): #Re-prompts if the choice is invalid.
            continue
        if int(itemNum) == 6:
            if order_count == 0: #Exits immediately if 6 is the first input.
                call_exit()
            else:
                 break #Anytime 6 is entered (not as the first choice), go back to main()

        while True:
            itemQuantity = input(INPUT_QUANTITY)
            if not isQuantityValid(itemQuantity): #Re-prompts if the quantity is invalid.
                continue
 
            itemPriceAndQuantityMap[int(itemNum)][2] += int(itemQuantity)
            order_count = order_count+1
        
            break


def ask_user_type():
    """
    Accepts the user type and validates it.

    Parameters:
    None

    Returns:
    str: returns 0 or 1
    """
    isStudentOrStaff = -1
    isEntryValid = False
    while not isEntryValid:
        isStudentOrStaff = input(INPUT_STUDENT_OR_STAFF)
        if isStudentOrStaff.isdigit() and int(isStudentOrStaff) >=0 and int(isStudentOrStaff) <= 1:
            isEntryValid = True
        
    return isStudentOrStaff

def calculate_total_before_tax():
    """
    Calculates the total by multiplying the item cost with quantity.

    Parameters:
    None

    Returns:
    total(float): total before tax.
    """
    total=0
    for item in itemPriceAndQuantityMap:
        total += itemPriceAndQuantityMap[item][1] * itemPriceAndQuantityMap [item][2]
    return round(total,2)

def calculate_tax(total, isStudentOrStaff):
    """
    Calculates the tax if the user type is Staff.

    Parameters:
    total (float) - total cost before tax.
    isStudentOrStaff (str) - 0 if student and 1 if staff

    Returns:
    tax(float): Tax
    """
    tax = 0
    if isStudentOrStaff == "1":
        tax = total * TAX_RATE/100
    return round(tax,2)

def display_receipt(total, tax):
    """
    Displays the receipt with - total, tax, final tax, items ordered with their quantity and cost per item.

    Parameters:
    total (float) - total cost before tax.
    tax (float) - tax

    Returns:
    None
    """
    print()
    print("Total before tax:",total)
    print("Tax",tax)
    print("Final Total:",round(total+tax,2))
    print("Items ordered are as follows: ")
    
       
    for item in itemPriceAndQuantityMap:
        if itemPriceAndQuantityMap[item][2]>0:
            print(itemPriceAndQuantityMap[item][0],"->",itemPriceAndQuantityMap[item][2], "*", itemPriceAndQuantityMap[item][1])
    print()

def main():
    """
    The execution of the program starts here. 
    """
    display_menu()
    order_food()
    isStudentOrStaff = ask_user_type()
    total = calculate_total_before_tax()
    tax = calculate_tax(total, isStudentOrStaff)
    display_receipt(total, tax)

if __name__ == "__main__":
    main()

"""
Output 1

No. Item                      Price
----------------------------------------
1   DeAnza Chicken Wings      $6.99
2   DeAnza Beef Burger        $7.99
3   DeAnza Chicken Burger     $5.00
4   Fries                     $3.00
5   Sprite                    $1.00
6   Exit                     

Please enter your choice, a number between 1 and 5 to order and 6 to quit: 6
Thank you, hope to see you again!
"""
"""
Output 2

No. Item                      Price
----------------------------------------
1   DeAnza Chicken Wings      $6.99
2   DeAnza Beef Burger        $7.99
3   DeAnza Chicken Burger     $5.00
4   Fries                     $3.00
5   Sprite                    $1.00
6   Exit                     

Please enter your choice, a number between 1 and 5 to order and 6 to quit: 1
Please enter the quantity: a
Error, Please enter a valid choice.
Please enter the quantity: a
Error, Please enter a valid choice.
Please enter the quantity: 2
Please enter your choice, a number between 1 and 5 to order and 6 to quit: aa
Error, Please enter a valid choice, a number between 1 and 6.
Please enter your choice, a number between 1 and 5 to order and 6 to quit: aa
Error, Please enter a valid choice, a number between 1 and 6.
Please enter your choice, a number between 1 and 5 to order and 6 to quit: 2
Please enter the quantity: 1
Please enter your choice, a number between 1 and 5 to order and 6 to quit: 6
If you are a student, enter 0. If you are a staff member, enter 1: 1

Total before tax: 21.97
Tax 1.98
Final Total: 23.95
Items ordered are as follows: 
DeAnza Chicken Wings -> 2 * 6.99
DeAnza Beef Burger -> 1 * 7.99
"""