from repository.repository import Repository


class FileRepositoryException(Exception):
    pass


class FileRepository(Repository):
    def __init__(self, validatorClass, filename, entityClass ):
        super().__init__(validatorClass)
        self.__entityClass = entityClass
        self.__filename = filename
        self.__validatorClass = validatorClass
        self.__load()

    def __load(self):
        try:
            with open(self.__filename) as f:
                for line in f:
                    entity = self.__entityClass.create_from_csv(line)
                    super().add(entity)
        except IOError:
            raise FileRepositoryException("File : {0} is missing".format(self.__filename))

    def __write_to_file(self):
        try:
            with open(self.__filename, 'w') as f:
                for e in self.get_all():
                    f.write(self.__entityClass.to_csv(e))
                    f.write('\n')
        except IOError:
            raise FileRepositoryException("File : {0} is missing".format(self.__filename))

    def add(self, entity):
        super().add(entity)
        self.__write_to_file()

    def update(self, entity_id, entity):
        super().update(entity_id, entity)
        self.__write_to_file()

    def remove_by_id(self, entity_id):
        super().remove_by_id(entity_id)
        self.__write_to_file()

    def add(self, entity):
        super().add(entity)
        self.__write_to_file()
