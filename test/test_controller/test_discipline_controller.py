import unittest

from controller.discipline_controller import DisciplineController
from domain.validators import DisciplineValidator
from repository.repository import Repository, RepositoryException


class TestDisciplineController(unittest.TestCase):
    
    validator = DisciplineValidator
    repository = Repository(validator)
    controller = DisciplineController(repository)
    
    
    def test_add_discipline(self):
        
        self.controller.add_discipline(1, 'mate')
        self.assertGreater(len(self.repository.get_all()), 0, 'The item was not appended')
        print('Tested adding a discipline')
        
    def test_find_by_name(self):
    
        self.assertEqual(len(self.controller.find_by_name('mate')), 1, 'item should have been found')
        self.assertEqual(len(self.controller.find_by_name('fp')), 0, 'item should have not been found')
        print('Tested finding a discipline by name')
        
    
    def test_get_all(self):
        
        self.assertEqual(len(self.controller.get_all()), 1, 'wrong number of objects returned')
        print('Tested getting all disciplines')
        
    def test_remove_by_id(self):
        try:
            self.controller.remove_by_id(2)
            assert False
        except RepositoryException:
            assert True
        
        self.controller.remove_by_id(1)
        self.assertEqual(len(self.controller.get_all()), 0, 'item should have been deleted')
        
    def test_update(self):
        self.controller.add_discipline(2,'fp')
        self.controller.update(2, 'mate')
        self.assertEqual(len(self.controller.find_by_name('mate')), 1, 'item was not succesfuly updated')
        print('Tested updating a discipline')
    
            
        