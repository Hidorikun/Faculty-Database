
import re
from domain.entities import Discipline


class DisciplineController(object):
    def __init__(self, discipline_repository):
        self.__discipline_repository = discipline_repository 
        
    def add_discipline(self, discipline_id, discipline_name):
        '''
        Adds a discipline entity to the given discipline repository
        :param discipline_id:
        :param discipline_name:
        :return: None
        '''
        discipline = Discipline(discipline_id, discipline_name)
        self.__discipline_repository.add(discipline)
        
    def find_by_id(self, discipline_id):
        '''
        Finds a discipline entity by its id
        :param discipline_id:
        :return: discipline entity with given id
        '''
        return self.__discipline_repository.find_by_id(discipline_id)
    
    def find_by_name(self, discipline_name):
        '''
        Finds all disciplines which name matches/partially or fully, the discipline_name string
        :param discipline_name:
        :return: list of entities that match partially the discipline_name
        '''
        discipline_name = discipline_name.lower()
        result = []
        for e in self.__discipline_repository.get_all():
            name = e.name 
            name = name.lower() 
            if re.search(discipline_name, name):
                result.append(e)
        return result
    
    def get_all(self):
        '''
        :return: list of all disciplines in the given repository
        '''
        return self.__discipline_repository.get_all()
    
    def remove_by_id(self, discipline_id):
        '''
        Removes the entity with discipine_id in repository
        :param discipline_id:
        :return: None
        '''
        self.__discipline_repository.remove_by_id(discipline_id)
    
    def update(self, discipline_id, discipline_name):
        '''
        Updates the discipline that has a given id to have the given name
        :param discipline_id:
        :param discipline_name:
        :return:None
        '''
        discipline = Discipline(discipline_id, discipline_name)
        self.__discipline_repository.update(discipline_id, discipline)
        

        