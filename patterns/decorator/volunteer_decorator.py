__author__ = "Ace Faulty"
__version__ = "1.0.0"

from patterns.decorator.student_decorator import StudentDecorator

class VolunteerDecorator(StudentDecorator):
    @property
    def grade_point_average(self) -> float:

        return super().grade_point_average + .25
    