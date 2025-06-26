# CIS 41A Final part1 Jackie Wang Team Name: Python Enjoyers Main execution file for De Anza Food Court system with CRUD operations demonstration

from order import Order

def demonstrate_crud_operations(order):
    #Demonstrate CRUD operations on the order.
    print("\n" + "="*50)
    print("DEMONSTRATING CRUD OPERATIONS")
    print("="*50)
    
    # Read current order
    order.read_order()
    
    # Create - Add items programmatically
    print("\nCRUD - CREATE: Adding items to order...")
    menu_items = order.get_menu_items()
    if len(menu_items) > 0:
        order.create_order_item(menu_items[0], 1)
        order.create_order_item(menu_items[1], 2)
    
    # Read updated order
    print("\nCRUD - READ: Current order after adding items:")
    order.read_order()
    
    # Update - Modify quantities
    print("\nCRUD - UPDATE: Updating item quantities...")
    if len(menu_items) > 0:
        order.update_order_item(menu_items[0], 3)
    
    # Read after update
    print("\nCRUD - READ: Order after update:")
    order.read_order()
    
    # Delete - Remove items
    print("\nCRUD - DELETE: Removing items from order...")
    if len(menu_items) > 1:
        order.delete_order_item(menu_items[1])
    
    # Final read
    print("\nCRUD - READ: Final order state:")
    order.read_order()
    
    print("\nCRUD Operations demonstration complete!")

def main():
    #Main function to run the De Anza Food Court ordering system.
    print("Welcome to De Anza Food Court Ordering System!")
    print("This system demonstrates OOP with inheritance and CRUD operations.")
    
    flag = True
    order_count = 0
    
    while flag:
        order_count += 1
        print(f"\n{'='*60}")
        print(f"ORDER #{order_count}")
        print(f"{'='*60}")
        
        # Create new order object
        order = Order()
        
        # Display menu
        order.display_menu()
        
        # Get user inputs
        order.get_inputs()
        
        # Calculate totals
        order.calculate()
        
        # Print bill
        order.print_bill()
        
        # Save to file
        order.save_to_file()
        
        # Ask if user wants to continue
        user_input = input("\nContinue for another order? ('y' = Yes, 'n' = No): ").strip()
        
        if user_input == 'n':
            print("Thank you for using De Anza Food Court!")
            flag = False

if __name__ == "__main__":
    main()

"""
Sample Output 1

Welcome to De Anza Food Court Ordering System!
This system demonstrates OOP with inheritance and CRUD operations.

============================================================
ORDER #1
============================================================

----------- De Anza Food Court -----------
No. Item                      Price
----------------------------------------
1   De Anza Burger            $5.25
2   Bacon Cheese              $5.75
3   Mushroom Swiss            $5.95
4   Western Burger            $5.95
5   Don Cali Burger           $5.95
6   Exit

Please enter your choice, a number between 1 and 5 to order and 6 to quit: 3
Please enter the quantity: 2
Please enter your choice, a number between 1 and 5 to order and 6 to quit: 5
Please enter the quantity: 3
Please enter your choice, a number between 1 and 5 to order and 6 to quit: 6 
If you are a student, enter 0. If you are a staff member, enter 1: 0

Your bill:
Item                      Qty        Price      Total
------------------------------------------------------------
Mushroom Swiss            2          $5.95      $11.90
Don Cali Burger           3          $5.95      $17.85
------------------------------------------------------------
Price before tax: $29.75
Tax: $0.00
Price after tax: $29.75
Customer type: Student

Bill saved to file: 2025-06-22 23-57-13.txt

Continue for another order? ('y' = Yes, 'n' = No): y

============================================================
ORDER #2
============================================================

----------- De Anza Food Court -----------
No. Item                      Price
----------------------------------------
1   De Anza Burger            $5.25
2   Bacon Cheese              $5.75
3   Mushroom Swiss            $5.95
4   Western Burger            $5.95
5   Don Cali Burger           $5.95
6   Exit

Please enter your choice, a number between 1 and 5 to order and 6 to quit: 3
Please enter the quantity: 1
Please enter your choice, a number between 1 and 5 to order and 6 to quit: 6
If you are a student, enter 0. If you are a staff member, enter 1: 0

Your bill:
Item                      Qty        Price      Total
------------------------------------------------------------
Mushroom Swiss            1          $5.95      $5.95
------------------------------------------------------------
Price before tax: $5.95
Tax: $0.00
Price after tax: $5.95
Customer type: Student

Bill saved to file: 2025-06-22 23-57-41.txt

Continue for another order? ('y' = Yes, 'n' = No): n
Thank you for using De Anza Food Court!

Sample Output 2

Welcome to De Anza Food Court Ordering System!
This system demonstrates OOP with inheritance and CRUD operations.

============================================================
ORDER #1
============================================================

----------- De Anza Food Court -----------
No. Item                      Price
----------------------------------------
1   De Anza Burger            $5.25
2   Bacon Cheese              $5.75
3   Mushroom Swiss            $5.95
4   Western Burger            $5.95
5   Don Cali Burger           $5.95
6   Exit

Please enter your choice, a number between 1 and 5 to order and 6 to quit: 4
Please enter the quantity: 1
Please enter your choice, a number between 1 and 5 to order and 6 to quit: 6
If you are a student, enter 0. If you are a staff member, enter 1: 1

Your bill:
Item                      Qty        Price      Total
------------------------------------------------------------
Western Burger            1          $5.95      $5.95
------------------------------------------------------------
Price before tax: $5.95
Tax: $0.54
Price after tax: $6.49
Customer type: Staff

Bill saved to file: 2025-06-22 23-58-50.txt

Continue for another order? ('y' = Yes, 'n' = No): n
Thank you for using De Anza Food Court!
"""