__author__ = "ACE FACULTY"
__version__ = "1.0.0"

from abc import ABC,abstractmethod

class StudentDecoratable(ABC):

    """
    Interface to be applied the Student class.
    Note : Add more abstract methods  to 
    support future decoractors as needed.
    """

    @abstractmethod
    def grade_point_average(self)->float:
        pass