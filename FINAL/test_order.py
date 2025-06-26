# Team Name: Python Enjoyers
# Date: 05/09/25
# Class: CIS41A
# Desc: Unit testing file for De Anza Food Court system

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from food_item import Burger, DeAnzaBurger, BaconCheese, MushroomSwiss, WesternBurger, DonCaliBurger
from person import Person, Student, Staff
from order import Order


class TestBurgerClasses(unittest.TestCase):
    #Test cases for Burger classes.
    
    def setUp(self):
        #Set up test fixtures before each test method.
        self.basic_burger = Burger()
        self.deanza_burger = DeAnzaBurger()
        self.bacon_cheese = BaconCheese()
        self.mushroom_swiss = MushroomSwiss()
        self.western_burger = WesternBurger()
        self.don_cali_burger = DonCaliBurger()
    
    def test_burger_initialization(self):
        #Test that burgers are initialized correctly.
        self.assertEqual(self.basic_burger.get_name(), "Basic Burger")
        self.assertEqual(self.basic_burger.get_price(), 5.00)
        
    def test_specific_burger_names(self):
        #Test that specific burger subclasses have correct names.
        self.assertEqual(self.deanza_burger.get_name(), "De Anza Burger")
        self.assertEqual(self.bacon_cheese.get_name(), "Bacon Cheese")
        self.assertEqual(self.mushroom_swiss.get_name(), "Mushroom Swiss")
        self.assertEqual(self.western_burger.get_name(), "Western Burger")
        self.assertEqual(self.don_cali_burger.get_name(), "Don Cali Burger")
    
    def test_specific_burger_prices(self):
        #Test that specific burger subclasses have correct prices.
        self.assertEqual(self.deanza_burger.get_price(), 5.25)
        self.assertEqual(self.bacon_cheese.get_price(), 5.75)
        self.assertEqual(self.mushroom_swiss.get_price(), 5.95)
        self.assertEqual(self.western_burger.get_price(), 5.95)
        self.assertEqual(self.don_cali_burger.get_price(), 5.95)
    
    def test_calculate_total(self):
        #Test total calculation for different quantities.
        self.assertEqual(self.deanza_burger.calculate_total(2), 10.50)
        self.assertEqual(self.bacon_cheese.calculate_total(3), 17.25)
        self.assertEqual(self.mushroom_swiss.calculate_total(1), 5.95)
    
    def test_set_price(self):
        #Test price setting functionality.
        original_price = self.basic_burger.get_price()
        self.basic_burger.set_price(6.00)
        self.assertEqual(self.basic_burger.get_price(), 6.00)
        
        # Test invalid price (should not change)
        self.basic_burger.set_price(-1.00)
        self.assertEqual(self.basic_burger.get_price(), 6.00)
    
    def test_str_representation(self):
        #Test string representation of burgers.
        expected = "De Anza Burger - $5.25"
        self.assertEqual(str(self.deanza_burger), expected)


class TestPersonClasses(unittest.TestCase):
    #Test cases for Person superclass and subclasses.
    
    def setUp(self):
        #Set up test fixtures before each test method.
        self.student = Student()
        self.staff = Staff()
    
    def test_student_initialization(self):
        #Test that student is initialized correctly.
        self.assertEqual(self.student.get_person_type(), "Student")
        self.assertEqual(self.student._tax_rate, 0.0)
    
    def test_staff_initialization(self):
        #Test that staff is initialized correctly.
        self.assertEqual(self.staff.get_person_type(), "Staff")
        self.assertEqual(self.staff._tax_rate, 9.0)
    
    def test_student_tax_calculation(self):
        #Test that students pay no tax.
        self.assertEqual(self.student.calculate_tax(100.00), 0.00)
        self.assertEqual(self.student.calculate_tax(50.25), 0.00)
    
    def test_staff_tax_calculation(self):
        #Test that staff pay 9% tax.
        self.assertEqual(self.staff.calculate_tax(100.00), 9.00)
        self.assertEqual(self.staff.calculate_tax(50.00), 4.50)
        self.assertAlmostEqual(self.staff.calculate_tax(33.33), 3.00, places=2)


class TestOrderClass(unittest.TestCase):
    #Test cases for Order class and CRUD operations.
    
    def setUp(self):
        #Set up test fixtures before each test method.
        self.order = Order()
    
    def test_order_initialization(self):
        #Test that order is initialized correctly.
        self.assertIsNotNone(self.order._price_dict)
        self.assertIsNotNone(self.order._order_dict)
        self.assertEqual(len(self.order._price_dict), 5)
        self.assertEqual(len(self.order._order_dict), 5)
        self.assertEqual(self.order._price_before_tax, 0.0)
        self.assertEqual(self.order._price_after_tax, 0.0)
        self.assertEqual(self.order._tax, 0.0)
    
    def test_menu_items(self):
        #Test that menu items are correctly set up.
        menu_items = self.order.get_menu_items()
        expected_items = ["De Anza Burger", "Bacon Cheese", "Mushroom Swiss", 
                         "Western Burger", "Don Cali Burger"]
        for item in expected_items:
            self.assertIn(item, menu_items)
    
    def test_crud_create_operation(self):
        #Test CRUD Create operation.
        result = self.order.create_order_item("De Anza Burger", 2)
        self.assertTrue(result)
        self.assertEqual(self.order._order_dict["De Anza Burger"], 2)
        
        # Test invalid item
        result = self.order.create_order_item("Invalid Item", 1)
        self.assertFalse(result)
    
    def test_crud_update_operation(self):
        #Test CRUD Update operation.
        # First add an item
        self.order.create_order_item("Bacon Cheese", 1)
        
        # Then update it
        result = self.order.update_order_item("Bacon Cheese", 3)
        self.assertTrue(result)
        self.assertEqual(self.order._order_dict["Bacon Cheese"], 3)
        
        # Test invalid item
        result = self.order.update_order_item("Invalid Item", 1)
        self.assertFalse(result)
    
    def test_crud_delete_operation(self):
        #Test CRUD Delete operation.
        # First add an item
        self.order.create_order_item("Mushroom Swiss", 2)
        
        # Then delete it
        result = self.order.delete_order_item("Mushroom Swiss")
        self.assertTrue(result)
        self.assertEqual(self.order._order_dict["Mushroom Swiss"], 0)
        
        # Test deleting non-existent item
        result = self.order.delete_order_item("Mushroom Swiss")
        self.assertFalse(result)
    
    def test_price_calculation(self):
        #Test price calculation functionality.
        # Add some items
        self.order._order_dict["De Anza Burger"] = 2  # 2 * 5.25 = 10.50
        self.order._order_dict["Bacon Cheese"] = 1    # 1 * 5.75 = 5.75
        # Total should be 16.25
        
        # Set customer type
        self.order._person = Student()
        self.order.calculate()
        
        self.assertEqual(self.order._price_before_tax, 16.25)
        self.assertEqual(self.order._tax, 0.0)  # Student pays no tax
        self.assertEqual(self.order._price_after_tax, 16.25)
        
        # Test with staff (with tax)
        self.order._person = Staff()
        self.order.calculate()
        
        self.assertEqual(self.order._price_before_tax, 16.25)
        self.assertAlmostEqual(self.order._tax, 1.46, places=2)  # 16.25 * 0.09
        self.assertAlmostEqual(self.order._price_after_tax, 17.71, places=2)
    
    def test_get_order_total(self):
        #Test getting order total.
        self.order._price_after_tax = 25.50
        self.assertEqual(self.order._price_after_tax, 25.50)
    
    def test_item_validation(self):
        #Test item number validation.
        self.assertTrue(self.order.is_item_valid("1"))
        self.assertTrue(self.order.is_item_valid("5"))
        self.assertTrue(self.order.is_item_valid("6"))
        self.assertFalse(self.order.is_item_valid("0"))
        self.assertFalse(self.order.is_item_valid("7"))
        self.assertFalse(self.order.is_item_valid("abc"))
    
    def test_quantity_validation(self):
        #Test quantity validation.
        self.assertTrue(self.order.is_quantity_valid("1"))
        self.assertTrue(self.order.is_quantity_valid("10"))
        self.assertFalse(self.order.is_quantity_valid("0"))
        self.assertFalse(self.order.is_quantity_valid("-1"))
        self.assertFalse(self.order.is_quantity_valid("abc"))


class IntegrationTests(unittest.TestCase):
    #Integration tests for the complete system.
    
    def setUp(self):
        #Set up test fixtures before each test method.
        self.order = Order()
    
    def test_complete_order_flow(self):
        #Test complete order flow integration.
        # Add items to order
        self.order.create_order_item("De Anza Burger", 1)
        self.order.create_order_item("Western Burger", 2)
        
        # Set customer
        self.order._person = Staff()
        
        # Calculate totals
        self.order.calculate()
        
        # Verify calculations
        expected_subtotal = 5.25 + (2 * 5.95)  # 17.15
        expected_tax = round(expected_subtotal * 0.09, 2)  # 1.54
        expected_total = expected_subtotal + expected_tax  # 18.69
        
        self.assertAlmostEqual(self.order._price_before_tax, expected_subtotal, places=2)
        self.assertAlmostEqual(self.order._tax, expected_tax, places=2)
        self.assertAlmostEqual(self.order._price_after_tax, expected_total, places=2)
    
    def test_burger_inheritance(self):
        #Test burger inheritance and polymorphism.
        burgers = [
            DeAnzaBurger(),
            BaconCheese(),
            MushroomSwiss(),
            WesternBurger(),
            DonCaliBurger()
        ]
        
        for burger in burgers:
            # Test that all burgers have required methods
            self.assertTrue(hasattr(burger, 'get_name'))
            self.assertTrue(hasattr(burger, 'get_price'))
            self.assertTrue(hasattr(burger, 'calculate_total'))
            self.assertTrue(hasattr(burger, '__str__'))
            
            # Test that methods return expected types
            self.assertIsInstance(burger.get_name(), str)
            self.assertIsInstance(burger.get_price(), float)
            self.assertIsInstance(burger.calculate_total(1), float)
            self.assertIsInstance(str(burger), str)
    
    def test_person_inheritance(self):
        #Test person inheritance and tax calculation.
        student = Student()
        staff = Staff()
        
        # Test inheritance
        self.assertIsInstance(student, Person)
        self.assertIsInstance(staff, Person)
        
        # Test tax calculation differences
        test_amount = 100.0
        self.assertEqual(student.calculate_tax(test_amount), 0.0)
        self.assertEqual(staff.calculate_tax(test_amount), 9.0)


def run_tests():
    #Run all tests and display results.
    print("Running De Anza Food Court System Unit Tests")
    print("="*50)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestBurgerClasses))
    suite.addTests(loader.loadTestsFromTestCase(TestPersonClasses))
    suite.addTests(loader.loadTestsFromTestCase(TestOrderClass))
    suite.addTests(loader.loadTestsFromTestCase(IntegrationTests))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1) 