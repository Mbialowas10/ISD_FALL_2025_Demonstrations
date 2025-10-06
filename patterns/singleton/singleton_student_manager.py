__author__ = "ACE Faculty"
__version__ = "1.0.0"

class SingletonStudentManager: 
    """
    SingletonStudentManager: Employs the singleton pattern
    to ensure only one instance of the class is in memory at 
    a time.
    """
    __instance = None
    __next_student_number = 20240000

    def __new__(cls):
        """Constructs the ShingletoneStudent instance but only
        if it does note already exist in memory."""

        if not cls.__instance:
            # create the instance
            cls.__instance = super(SingletonStudentManager, cls).__new__(cls)
        
        return cls.__instance
    
    def get_next_student_number(self) -> int:
        """Returns the next student number and increments the
        internal counter."""
        
        student_number = self.__next_student_number
        self.__next_student_number += 1
        return student_number
       
