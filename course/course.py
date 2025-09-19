__author__ = "student name"
__version__ = "1.0.0"

from department.department import Department
from student.student import Student
from abc import ABC, abstractmethod

class Course(ABC):

    """
    Initializes a course object based upon received arguments (if valid)

    args:
        name(str) : The name of the course
        department (Deparment) : the name of the department in which 
        courses exist. 
        credit_hours (int): The number of credit hrs a course has.
    """

    def __init__(self, name:str, department:Department, credit_hours: int,
                 capacity: int, current_enrollment: int):

        if len(name.strip())> 0: # strip removes any space 
                                #before and after the word
            self.__name = name # name mangling _ClassName.__name
        else:
            raise ValueError("Name cannot be blank.")
        
        if isinstance(department, Department):
            self.__department = department
        else:
            raise ValueError("Deparment is invalid")
        if isinstance(credit_hours, int):
            self.__credit_hours = credit_hours
        else:
            raise ValueError("Credit hours must be an int type")
        if isinstance(capacity, int):
            # single understore to represent protected
            self._capacity = capacity
        else:
            raise ValueError("Capacity must be numeric.")
        
        if isinstance(current_enrollment, int):
            self._current_enrollment = current_enrollment
        else:
            raise ValueError("Current enrollmment must be numeric.")
        
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def department(self) -> Department:
        return self.__department
    
    @property
    def credit_hours(self) -> int:
        return self.__credit_hours
    
    @abstractmethod
    def enroll_student(self, student: Student) -> str:
        """
        Enrolls a student in a course if capacity allows
        Args:
            student(Student): The student to enrolled.
        Returns: str: Str message indicating success or failure
        of enrollment.
        """
        pass
    
    def __str__(self) ->str:
        return (f"Course: {self.__name}"
                + f"\nDepartment: "+
                f"{self.__department.name.replace('_',' ').title()}"
                + f"\nCredit Hours: {self.__credit_hours}")
    
    

    

    
        
       