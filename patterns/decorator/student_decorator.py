__author__ = "Ace Faulty"
__version__ = "1.0.0"

from patterns.decorator.student_decoratable import StudentDecoratable

class StudentDecorator(StudentDecoratable):

    """
    Student Decorator.
    Implements the abstract superclaaa method

    """

    def __init__(self, student: StudentDecoratable):
        self.__student = student
    
    @property
    def grade_point_average(self) ->float:
        return self.__student.grade_point_average