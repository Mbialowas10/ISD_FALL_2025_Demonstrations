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

    def test_init_valid(self):
        # Arrange and Act
        course = Course("ISD", Department.COMPUTER_SCIENCE, 6)

        # Assert
        self.assertEqual("ISD",course._Course__name) # name mangling
