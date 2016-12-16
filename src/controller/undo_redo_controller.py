'''
Created on Dec 3, 2016

@author: Ok!
'''
from domain.validators import DatabaseException

class UndoRedoException(DatabaseException):
    pass

class UndoRedoController(object):
    
    def __init__(self, student_repository, discipline_repositiry, grade_repository, enroll_controller):
        self.__student_repo = student_repository
        self.__discipline_repo= discipline_repositiry
        self.__grade_repo = grade_repository
        self.__enroll_controller = enroll_controller
        self.__memorator = []
        self.__index = -1
        self.memorise()
          
    def memorise(self):
        '''
        memorise the state of the program
        '''
        self.__index += 1
        self.__memorator = self.__memorator[:self.__index]
        state = self.__create_state()
        self.__memorator.append(state)
       
    
    def undo(self):
        '''
        decreases the index of the undo stack to the previous state of the program
        '''
        if self.__index == 0:
            raise UndoRedoException("No more operations to undo")
        
        self.__index -= 1
        state = self.__memorator[self.__index]
        self.__load_state(state)
        
    def redo(self):
        '''
        increases the index of the undo stack to a more current state of the program
        '''
        if self.__index + 1 == len(self.__memorator):
            raise UndoRedoException("No more operations to redo")
        
        self.__index += 1
        state = self.__memorator[self.__index]
        self.__load_state(state)
        
    def __load_state(self, state):
        '''
        Brings the program to a given state
        :param state:
        '''
        self.__student_repo.load_state(state[0])
        self.__discipline_repo.load_state(state[1])
        self.__grade_repo.load_state(state[2])
        self.__enroll_controller.load_state(state[3])
        
    def __create_state(self):
        '''
        Creates a state
        :return: a tuple consisting of copies for all repositories information in the program
        '''
        return (self.__student_repo.info(), self.__discipline_repo.info(), self.__grade_repo.info(), self.__enroll_controller.info())
    
    