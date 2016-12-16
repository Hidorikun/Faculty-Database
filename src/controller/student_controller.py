'''
Created on Nov 2, 2016

@author: Ok!
'''

import re

from domain.entities import Student


class StudentController(object):
    def __init__(self, student_repository):
        self.__student_repository = student_repository 
        
    def add_student(self, student_id, student_name):
        '''
        creates a student with student_id and student_name
        and calls the add method in repository with certain student
        '''
        student = Student(student_id, student_name)
        self.__student_repository.add(student)
        
    def find_by_id(self, student_id):
        '''
        passes student_id argument to the find_by_id method in studdnt_repository 
        '''
        return self.__student_repository.find_by_id(student_id)
    
    def find_by_name(self, student_name):
        '''
        finds all students which name matches/partially or fully, the student_name string
        '''
        student_name = student_name.lower()
        result = []
        for e in self.__student_repository.get_all():
            name = e.name 
            name = name.lower() 
            if re.search(student_name, name):
                result.append(e)
        return result
    
    def get_all(self):
        '''
        calls the get_all method in repository which returns all students as objects
        '''
        return self.__student_repository.get_all()
    
    def remove_by_id(self, student_id):
        '''
        calls the remove_by_id in the repository 
        '''
        self.__student_repository.remove_by_id(student_id)
    
    def update(self, student_id, student_name):
        '''
        creates a student object with the given student_id and student_name
        and calls the update method in repository 
        '''
        student = Student(student_id, student_name)
        self.__student_repository.update(student_id, student)
        

        