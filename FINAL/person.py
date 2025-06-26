# CIS 41A Final part1 Jackie Wang Team Name: Python Enjoyers Person class hierarchy for De Anza Food Court system

class Person:

    def __init__(self, person_type):
        #Initialize a Person object.
        self._person_type = person_type
        self._tax_rate = 0.0
    
    def calculate_tax(self, total_before_tax):
        #Calculate tax on the total amount.
        return round(total_before_tax * self._tax_rate / 100, 2)
    
    def get_person_type(self):
        #Get the type of person.
        return self._person_type


class Student(Person):
    #Student subclass - students don't pay tax.
    
    def __init__(self):
        #Initialize a Student object.
        super().__init__("Student")
        self._tax_rate = 0.0
    
    def calculate_tax(self, total_before_tax):
        #Override tax calculation for students (no tax).
        return 0.0


class Staff(Person):
    #Staff subclass - staff members pay 9% tax.
    
    def __init__(self):
        #Initialize a Staff object.
        super().__init__("Staff")
        self._tax_rate = 9.0
    
    def calculate_tax(self, total_before_tax):
        #Override tax calculation for staff (9% tax).
        return round(total_before_tax * self._tax_rate / 100, 2)