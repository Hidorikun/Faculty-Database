'''
Created on Nov 2, 2016

@author: George Vele
'''


class DatabaseException(Exception):
    '''
    main exception, parent of all exceptions that is caught in main
    '''
    pass

class StudentValidatorException(DatabaseException):
    '''
    exception raised by StudentValidator class if errors are found
    '''
    pass

class DisciplineValidatorException(DatabaseException):
    '''
    exception raised by DisciplineValidator class if errors are found
    '''
    pass

class GradeValidatorException(DatabaseException):
    '''
    exception raised by GradeValidator class if errors are found
    '''
    pass

class StudentValidator(object):
    '''
    class that implements validation method for student object
    '''
    @staticmethod
    def validate(student):
        '''
        method that validates Student Object input
        arguments:
            student - Student object 
        raises:
            StudentValidatorException - if student id or name are incorrect
        '''
        if type(student.entity_id) is not int:
            raise StudentValidatorException("Student ID must be integer")
        
        name = student.name.strip()
        for h in name.split(' '):
            for e in h.split('-'):
                e = e.strip()
                if not e.isalpha():
                    raise StudentValidatorException("Student name must contain only letters, and eventually one '-' between names")
            
    
class DisciplineValidator(object):
    '''
    class that implements validation method for discipline object
    '''
    @staticmethod
    def validate(discipline):
        '''
        method that validates Discipline object input
        arguments:
            discipline - Discipline object
        raises:
            DisciplineValidatorException - if discipline id is not valid
        '''
        if type(discipline.entity_id) is not int:
            raise DisciplineValidatorException("Discipline ID must be integer")
        

class GradeValidator(object):
    '''
    class that implements validation method for Grade object
    '''
    @staticmethod
    def validate(grade):
        '''
        method that validates Grade object input
        :arguments
            grade - Grade object 
        :raises:
            GradeValidatorException - if grade value is not in interval [1..10] 
        '''
        if grade.value < 1 or grade.value > 10:
            raise GradeValidatorException("Grade value muse be between [1..10]")

class EnrollValidator(object):
    '''
    This object type cannot be validated here, but we need the validator anyhow because of the general repository format
    '''

    @staticmethod
    def validate(grade):
        pass