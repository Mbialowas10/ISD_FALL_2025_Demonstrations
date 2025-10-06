__author__ = "Ace Faculty"
__version__ = "1.0.0"

from patterns.decorator.student_decorator import StudentDecorator
class CouncilDecorator(StudentDecorator):

    """
    Decorator to be applie to student objects for students who
    participate in the student council. Student who participate
    in student countil receieve a gpa boost. 
    """

    @property
    def grade_point_avaerage(self)-> float:
        """
        Grade Point Average accessor
        Returns :
            float: The value of the grade point average with a boost
            applied.
        """
        grade_point_average = super().grade_point_average

        increases: dict[float, float] = {
            4.13: .35,
            3.66: .19,
            2.4: .03
        }
        increase = 0 

        for average in increases:
            if grade_point_average >= average:
                increase = increases[average]
                break
        return grade_point_average + increase
