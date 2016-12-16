from domain.entities import Grade
from domain.validators import DatabaseException


class RepositoryException(DatabaseException):
    pass
# 
# The repository is more like a container (vector of sorts as in C++)
# That can store our wanted entities and perform operations on them 
# A repository for student stores for example in our problem our students Database
# we of course can have more repositories, just like we can have more vector<int> in C++

class Repository(object):
    '''
    class that stores and performs operations on objects that have id and name
    '''
    def __init__(self, validator_class):
        self.__validator_class = validator_class
        self.__entities = {} 

    def __contains__(self, entity_id):
        return entity_id in self.__entities

    def __getitem__(self, item):
        return self.__entities[item]

    def __delitem__(self, key):
        del self.__entities[key]

    def __setitem__(self, key, entity):
        self.__entities[key] = entity


    def find_by_id(self, entity_id):
        '''
        returns the object identified by entity_id 
        args:
            entity_id - the id by which to search 
        returns
            object stored with id = entity_id
            None if not found
        '''
        if entity_id in self.__entities.keys():
            return self[entity_id]
        return None
    
    def add(self, entity):
        '''
        *adds entity object to the dictionary at key = entity.entity_i
        args:
            entity - object to be added to repository
        exception:
            RepositoryException if entity.entity_id is taken
        '''
        self.__validator_class.validate(entity)
        if self.find_by_id(entity.entity_id) is not None:
            raise RepositoryException("duplicate id {0}".format(entity.entity_id))
        self[entity.entity_id] = entity
        
    def update(self, entity_id, entity):
        '''
        replaces the entity at key = entity_id with entity
        '''
        self[entity_id] = entity
    
    def info(self):
        '''
        :return: a copy of the repository information
        '''
        return self.__entities.copy()
    
    def load_state(self, state):
        self.__entities = state.copy()
    
    def copy(self):
        cpy = Repository(self.__validator_class)
        for key in self:
            cpy.add(self[key])
        return cpy
    
    def remove_by_id(self, entity_id):
        '''
        deletes the entity at key = entity_id 
        exception:
            RepositoryException - if there is no element with entity_id
        '''
        if self.find_by_id(entity_id) is None:
            raise RepositoryException("deletion error : id {0} does not exist".format(entity_id))
        del self[entity_id]
        
    def get_all(self):
        '''
        returns all entities in repository as objects
        '''
        return self.__entities.values() #which are objects of type entity