__author__ = "Ace Faculty"
__version__ = "1.0.0"

from patterns.decorator.student_decoratable import StudentDecoratable

class StudentDecorator(StudentDecoratable):
    """
    Student Decorator
    Implements the abstract superclass methods...
    """
    def __init__(self, student: StudentDecoratable):
        """
        Identy the student to which decorators 
        may apply
        """
        self.__student = student
    
    @property
    def grade_point_average(self) -> float:
        """
        Purpose: Grade point average

        Returns: float: the grade point value
        assigned to a student
        """
        return self.__student.grade_point_average

