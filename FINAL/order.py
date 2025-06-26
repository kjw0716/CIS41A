# CIS 41A Final part1 Jackie Wang Team Name: Python Enjoyers Order class for De Anza Food Court system with CRUD operations

import time
import datetime
from person import Student, Staff
from food_item import Burger, DeAnzaBurger, BaconCheese, MushroomSwiss, WesternBurger, DonCaliBurger


class Order:
    #Order class to manage food court orders with CRUD operations.  
    
    def __init__(self):
        #Initialize an Order object with food items and order tracking.
        self._price_before_tax = 0.0
        self._price_after_tax = 0.0
        self._tax = 0.0
        self._person = None
        
        # Dictionary to store food items with their details
        self._price_dict = {
            "De Anza Burger": 5.25,
            "Bacon Cheese": 5.75,
            "Mushroom Swiss": 5.95,
            "Western Burger": 5.95,
            "Don Cali Burger": 5.95
        }
        
        # Dictionary to store order quantities
        self._order_dict = {
            "De Anza Burger": 0,
            "Bacon Cheese": 0,
            "Mushroom Swiss": 0,
            "Western Burger": 0,
            "Don Cali Burger": 0
        }
    
    def get_menu_items(self):
        #Get list of menu item names for CRUD operations.
        return list(self._price_dict.keys())
    
    def display_menu(self):
        #Display the food court menu with prices.
        print("\n----------- De Anza Food Court -----------")
        print("%-3s %-25s %s" % ("No.", "Item", "Price"))
        print("-" * 40)
        
        number = 1
        for key in self._price_dict:
            print("%-3s %-25s $%.2f" % (number, key, self._price_dict[key]))
            number += 1
        print("%-3s %-25s" % ("6", "Exit"))
        print()
    
    def is_item_valid(self, item_num):
        #Validate the food choice entered by user.
        is_valid = False
        if item_num.strip().isdigit() and 1 <= int(item_num.strip()) <= 6:
            is_valid = True
        else:
            print("Error, Please enter a valid choice, a number between 1 and 6.")
        return is_valid
    
    def is_quantity_valid(self, quantity):
        #Validate that quantity is a positive whole number.
        is_valid = False
        if quantity.strip().isdigit() and int(quantity.strip()) > 0:
            is_valid = True
        else:
            print("Error, Please enter a valid quantity.")
        return is_valid
    
    def get_inputs(self):
        #Get order inputs from user and fill the order dictionary.
        order_count = 0
        menu_items = list(self._price_dict.keys())
        
        while True:
            item_num = input("Please enter your choice, a number between 1 and 5 to order and 6 to quit: ")
            
            if not self.is_item_valid(item_num):
                continue
            
            item_num = int(item_num.strip())
            
            if item_num == 6:
                if order_count == 0:
                    print("Thank you, hope to see you again!")
                    exit()
                else:
                    break
            
            while True:
                quantity = input("Please enter the quantity: ")
                if not self.is_quantity_valid(quantity):
                    continue
                
                quantity = int(quantity.strip())
                item_name = menu_items[item_num - 1]
                self._order_dict[item_name] += quantity
                order_count += 1
                break
        
        # Get person type for tax calculation
        while True:
            person_type = input("If you are a student, enter 0. If you are a staff member, enter 1: ").strip()
            if person_type.isdigit() and int(person_type) in [0, 1]:
                if int(person_type) == 0:
                    self._person = Student()
                else:
                    self._person = Staff()
                break
            else:
                print("Error, Please enter 0 for student or 1 for staff.")
    
    def calculate(self):
        #Calculate the price before and after tax.
        self._price_before_tax = 0.0
        for key in self._price_dict:
            self._price_before_tax += self._order_dict[key] * self._price_dict[key]
        
        self._price_before_tax = round(self._price_before_tax, 2)
        self._tax = self._person.calculate_tax(self._price_before_tax)
        self._price_after_tax = round(self._price_before_tax + self._tax, 2)
    
    def print_bill(self):
        #Print the bill on the console.
        print("\nYour bill:")
        print("%-25s %-10s %-10s %-10s" % ("Item", "Qty", "Price", "Total"))
        print("-" * 60)
        
        for key in self._order_dict:
            if self._order_dict[key] > 0:
                item_total = self._order_dict[key] * self._price_dict[key]
                print("%-25s %-10d $%-9.2f $%-9.2f" % 
                      (key, self._order_dict[key], self._price_dict[key], item_total))
        
        print("-" * 60)
        print("Price before tax: $%.2f" % self._price_before_tax)
        print("Tax: $%.2f" % self._tax)
        print("Price after tax: $%.2f" % self._price_after_tax)
        print("Customer type: %s" % self._person.get_person_type())
        print()
    
    def save_to_file(self):
        #Save the bill to a file with timestamp.
        time_stamp = time.time()
        order_time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H-%M-%S')
        file_name = order_time_stamp + '.txt'
        
        try:
            with open(file_name, 'w') as file_handle:
                file_handle.write("----------- De Anza Food Court Bill -----------\n")
                file_handle.write("%-25s %-10s %-10s %-10s\n" % ("Item", "Qty", "Price", "Total"))
                file_handle.write("-" * 60 + "\n")
                
                for key in self._order_dict:
                    if self._order_dict[key] > 0:
                        item_total = self._order_dict[key] * self._price_dict[key]
                        file_handle.write("%-25s %-10d $%-9.2f $%-9.2f\n" % 
                                        (key, self._order_dict[key], self._price_dict[key], item_total))
                
                file_handle.write("-" * 60 + "\n")
                file_handle.write("Price before tax: $%.2f\n" % self._price_before_tax)
                file_handle.write("Tax: $%.2f\n" % self._tax)
                file_handle.write("Price after tax: $%.2f\n" % self._price_after_tax)
                file_handle.write("Customer type: %s\n" % self._person.get_person_type())
                file_handle.write("Order saved on: %s\n" % datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S'))
            
            print(f"Bill saved to file: {file_name}")
            
        except Exception as e:
            print(f"Error saving bill to file: {e}")
    
    # CRUD Operations
    
    def create_order_item(self, item_name, quantity):
        #Create/Add an order item.
        if item_name in self._order_dict:
            self._order_dict[item_name] += quantity
            print(f"Added {quantity} {item_name}(s) to order.")
            return True
        else:
            print(f"Item {item_name} not found in menu.")
            return False
    
    def read_order(self):
        #Read/Display current order.
        print("\nCurrent Order:")
        print("%-25s %-10s" % ("Item", "Quantity"))
        print("-" * 35)
        
        has_items = False
        for key in self._order_dict:
            if self._order_dict[key] > 0:
                print("%-25s %-10d" % (key, self._order_dict[key]))
                has_items = True
        
        if not has_items:
            print("No items in order.")
        print()
    
    def update_order_item(self, item_name, new_quantity):
        #Update an order item quantity.
        if item_name in self._order_dict:
            old_quantity = self._order_dict[item_name]
            self._order_dict[item_name] = new_quantity
            print(f"Updated {item_name} quantity from {old_quantity} to {new_quantity}.")
            return True
        else:
            print(f"Item {item_name} not found in order.")
            return False
    
    def delete_order_item(self, item_name):
        #Delete an order item by setting quantity to 0.
        if item_name in self._order_dict and self._order_dict[item_name] > 0:
            self._order_dict[item_name] = 0
            print(f"Removed {item_name} from order.")
            return True
        else:
            print(f"Item {item_name} not found in current order.")
            return False
    
    def get_order_dict(self):
        #Get a copy of the current order dictionary.
        return self._order_dict.copy()
    
    def get_price_dict(self):
        #Get a copy of the price dictionary.
        return self._price_dict.copy() 