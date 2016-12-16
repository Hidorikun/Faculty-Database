import pickle
import warnings

from repository.repository import Repository


class PickleRepositoryException(Exception):
    pass

class PickleRepository(Repository):

    def __init__(self, ValidatorClass, filename):
        super().__init__(ValidatorClass)
        self.__ValidatorClass = ValidatorClass
        self.__filename = filename
        self.__load()

    def __load(self):
        try:
            with open(self.__filename, 'rb') as f:
                entities = pickle.load(f)
                for e in entities:
                    self.add(e)
        except IOError:
            raise PickleRepositoryException("File : {0} is missing".format(self.__filename))

        except EOFError:
            warnings.warn('The file {0} is empty! There is nothing to load from it.'.format(self.__filename))

    def __write(self):
        try:
            with open(self.__filename, 'wb') as f:
                pickle.dump(list(self.get_all()), f)
        except IOError:
            raise PickleRepositoryException("File : {} is missing".format(self.__filename))

    def update(self, entity_id, entity):
        super().update(entity_id, entity)
        self.__write()

    def remove_by_id(self, entity_id):
        super().remove_by_id(entity_id)
        self.__write()

    def add(self, entity):
        super().add(entity)
        self.__write()


