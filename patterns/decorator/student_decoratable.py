__author__ = "Ace Faculty"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class StudentDecoratable(ABC):

    """"
    Interface to be applied to the student class.

    Note: Add more abstract method to support future 
    decorators as needed
    """

    @abstractmethod
    def grade_point_average(self)->float:
        pass