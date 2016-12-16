from domain.validators import StudentValidatorException,\
    DisciplineValidatorException, GradeValidatorException


class LinkValidatorException(Exception):
    pass

class Student(object):
    '''
    class that defines student entities:
    constructor:
        Student(studentID, name)
        
    properties:
        entity_id
        name
    '''
    def __init__(self, studentID, name):
        try:
            self.__studentID = int(studentID)
        except ValueError:
            raise StudentValidatorException("Student ID must be integer")
        
        self.__name = name

    @property
    def entity_id(self):
        return self.__studentID

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return ("{0}: {1}".format(self.__studentID, self.__name))

    @staticmethod
    def create_from_csv(line):
        args = line.split(',')
        id = args[0].strip()
        name = args[1].strip()
        return Student(id, name)

    @staticmethod
    def to_csv(student):
        return "{},{}".format(student.entity_id, student.name)

class Discipline(object):
    '''
    class that defines Dsicipline entities.
    constructor:
        Discipline(disciplineID, name)
    properties:
        entity_id
        name
    '''
    def __init__(self, disciplineID, name):
        try:
            self.__disciplineID = int(disciplineID)
        except ValueError:
            raise DisciplineValidatorException("Discipline ID must be integer")

        self.__name = name

    @property
    def entity_id(self):
        return self.__disciplineID

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    def __str__(self):
        return ("{0}: {1}".format(self.__disciplineID, self.__name))

    @staticmethod
    def create_from_csv(line):

        args = line.split(',')
        id = args[0].strip()
        name = args[1].strip()
        return Discipline(id, name)

    @staticmethod
    def to_csv(discipline):
        return "{},{}".format(discipline.entity_id, discipline.name)

class Grade(object):
    '''
    Class that defines Grade entities.
    constructor:
        Grade(studentID, disicplineID, grade_value)
    properties:
        discipline_id
        student_id
        value
    setters:
        value
    '''
    def __init__(self, studentID, disciplineID, grade_value):
        try:
            self.__disciplineID = int(disciplineID)
        except ValueError:
            raise GradeValidatorException("Discipline ID must be integer")

        try:
            self.__studentID = int(studentID)
        except ValueError:
            raise GradeValidatorException("Student ID must be integer")

        try:
            self.__grade_value = int(grade_value)
        except ValueError:
            raise GradeValidatorException("Grade value must be integer")

        self.__id  = id(self)


    @property
    def entity_id(self):
        return self.__id

    @property
    def discipline_id(self):
        return self.__disciplineID

    @property
    def student_id(self):
        return self.__studentID

    @property
    def value(self):
        return self.__grade_value

    @value.setter
    def value(self, value):
        self.__grade_value = value

    def __str__(self):
        return ("{0}: {1} at {2}".format(self.__studentID, self.__grade_value, self.__disciplineID))

    @staticmethod
    def create_from_csv(line):
        args = line.split(',')
        student_id = args[0].strip()
        discipline_id = args[1].strip()
        value = args[2].strip()

        return Grade(student_id, discipline_id, value)

    @staticmethod
    def to_csv(grade):
        return "{},{},{}".format(grade.student_id, grade.discipline_id, grade.value)


class Link(object):
    def __init__(self, student_id, discipline_id):
        try:
            self.__discipline_id = int(discipline_id)
            self.__student_id = int(student_id)
        except ValueError:
            raise LinkValidatorException('student id and discipline id must be integer')
        self.__entity_id = (student_id, discipline_id)

    @property
    def student_id(self):
        return self.__student_id

    @property
    def discipline_id(self):
        return self.__discipline_id

    @property
    def entity_id(self):
        return self.__entity_id


    @staticmethod
    def create_from_csv(line):
        args = line.split(',')
        student_id = args[0].strip()
        discipline_id = args[1].strip()

        return Link(int(student_id), int(discipline_id))

    @staticmethod
    def to_csv(link):
        return "{},{}".format(link.student_id, link.discipline_id)