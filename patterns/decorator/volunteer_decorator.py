__author__ = "Ace Faculty"
__version__ = "1.0.0"

from patterns.decorator.student_decorator import StudentDecorator

class VolunteerDecorator(StudentDecorator):

    """
    Decorator applied to student objects for students who particiapate
    in volunteer activities. Student who volunteers receives gpa boost.]
    """
    @property
    def grade_point_average(self) -> float:
        """
        Grade poiint average accessor.
        Returns: 
            float: The value of teh grade point average with aa boost
            applied."""    
        return super().grade_point_average + .25