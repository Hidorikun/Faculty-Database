import unittest

from controller.student_controller import StudentController
from domain.entities import Student
from domain.validators import StudentValidator
from repository.repository import Repository, RepositoryException


class TeststudentController(unittest.TestCase):
    
    validator = StudentValidator
    repository = Repository(validator)
    controller = StudentController(repository)
    
    
    def test_add_student(self):
        
        self.controller.add_student(1, 'mate')
        self.assertGreater(len(self.repository.get_all()), 0, 'The item was not appended')
        print('Tested adding a student')
        
    def test_find_by_id(self):
        
        self.assertEqual(type(self.controller.find_by_id(1)), Student, 'item should have been found')
        self.assertNotEqual(type(self.controller.find_by_id(2)), Student, 'item should have not been found')
        print('Tested finding a student by id')
        
    def test_find_by_name(self):
    
        self.assertEqual(len(self.controller.find_by_name('mate')), 1, 'item should have been found')
        self.assertEqual(len(self.controller.find_by_name('fp')), 0, 'item should have not been found')
        print('Tested finding a student by name')
        
    
    def test_get_all(self):
        
        self.assertEqual(len(self.controller.get_all()), 1, 'wrong number of objects returned')
        print('Tested getting all students')
        
    def test_remove_by_id(self):
        try:
            self.controller.remove_by_id(2)
            assert False
        except RepositoryException:
            pass
        
        self.controller.remove_by_id(1)
        self.assertEqual(len(self.controller.get_all()), 0, 'item should have been deleted')
        
    def test_update(self):
        self.controller.add_student(2,'fp')
        self.controller.update(2, 'mate')
        self.assertEqual(len(self.controller.find_by_name('mate')), 1, 'item was not succesfuly updated')
        print('Tested updating a student')
    
            
        