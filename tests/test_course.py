"""
Description: Unit tests for the Course class.
Author: ACE Faculty
Modified by: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command (replace test_file_name.py with 
the appropriate file name.):
    python -m unittest tests/test_file_name.py
"""
import unittest
from course.course import Course
from department.department import Department

class TestClient(unittest.TestCase):

    # setup course object 
    def setUp(self):
        self.course = Course("ISD", Department.COMPUTER_SCIENCE, 6)

    def test_init_valid(self):
        # Arrange and Act
        course = Course("ISD", Department.COMPUTER_SCIENCE, 6)

        # Assert
        self.assertEqual("ISD",course._Course__name) # name mangling

        self.assertEqual(Department.COMPUTER_SCIENCE, course._Course__department)

        self.assertEqual(6, course._Course__credit_hours)
    
    def test_init_invalid_name_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            course = Course(" ", Department.COMPUTER_SCIENCE, 6)

    def test_init_invalid_deparment_raises_exception(self):
        #Arrange & Act
        with self.assertRaises(ValueError):
            course = Course("ISD", "Invalid", 6)
    
    def test_init_invalid_credit_hours_raises_exception(self):
        with self.assertRaises(ValueError):
            course = Course("ISD", Department.COMPUTER_SCIENCE, "six")
    
    def test_name_accessor(self):
        self.assertEqual("ISD", self.course.name)
    
    def test_department_accessor(self):
        self.assertEqual(Department.COMPUTER_SCIENCE, self.course.department)

    def test_credit_hours_accessor(self):
        self.assertEqual(6, self.course.credit_hours)

    def test_str(self):
        # Arrange done by the setup above 
        expected = ("Course: ISD\n"
                    +"Department: Computer Science\n"+
                    "Credit Hours: 6")
        
        # Act and Assert
        self.assertEqual(expected, str(self.course))
