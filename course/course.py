__author__ = "student name"
__version__ = "1.0.0"

from department.department import Department

class Course:

    """
    Initializes a course object based upon received arguments (if valid)

    args:
        name(str) : The name of the course
        department (Deparment) : the name of the department in which 
        courses exist. 
        credit_hours (int): The number of credit hrs a course has.
    """

    def __init__(self, name:str, department:Department, credit_hours: int):

        if len(name.strip())> 0:
            self.__name = name # name mangling _ClassName.__name
        else:
            raise ValueError("Name cannot be blank.")
        
        if isinstance(department, Department):
            self.__department = department
        else:
            raise ValueError("Deparment is invalid.")
        
        if isinstance(credit_hours, int):
            self.__credit_hours = credit_hours
        else:
            raise ValueError("Credit hours must be numeric.")
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property 
    def department(self) -> Department:
        return self.__department

    @property
    def credit_hours(self) -> int:
        return self.__credit_hours
    
    def __str__(self) -> str:

        return (f"Course: {self.__name}"
                    f"\nDepartment:"
                     f"{self.__department.name.replace('-',' ').title()}"
                     + f"\nCredit Hours: {self.__credit_hours}"
                )
