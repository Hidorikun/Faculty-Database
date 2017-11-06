'''
Created on Nov 26, 2016

@author: George Vele
'''
from domain.entities import Link
from domain.validators import DatabaseException
from repository.repository import RepositoryException


class EnrollException(DatabaseException):
    pass 

class EnrolledController(object):
    def __init__(self, enroll_repository,  student_repository, discipline_repository):
        self.__enroll_repository = enroll_repository
        self.__student_repository = student_repository
        self.__discipline_repository = discipline_repository
        self.__keep_only_valid()

    def get_all(self):
        '''
        :return: the enrolled dictionary
        '''
        return self.__enroll_repository.get_all()
    
    def info(self):
        '''
        :return: a copy of the enrolled dictionary
        '''
        return self.__enroll_repository.info()

    def __get_student(self, student_id):
        '''
        Gets the student name for student_id
        :param student_id:
        :return: student name (string)
        :exception
            EnrollException - if the student_id is not found
        '''
        try:
            return self.__student_repository.find_by_id(student_id).name
        except AttributeError:
            raise EnrollException("Currently there is no student with id {0}".format(student_id))
        
    def __get_discipline(self, discipline_id):
        '''
        gets the discipline name for discipline_id
        :param discipline_id:
        :return: discipline name (string)
        :exception:
            EnrollException - if the grade_id is not found
        '''
        try:
            return self.__discipline_repository.find_by_id(discipline_id).name
        except AttributeError:
            raise EnrollException("Currently there is no discipline with id {0}".format(discipline_id))
         
    def find_by_id(self, entity_id):
        '''
        Finds and returns the link identified by entity_id in repository
        :param entity_id: tuple
        :return: link witn link.entity_id == entity_id
        '''
        what_is_found = self.__enroll_repository.find_by_id(entity_id)
        # if what_is_found is None:
        #     student_id = entity_id[0]
        #     discipline_id = entity_id[1]
        #     raise EnrollException('Student {} is not enrolled for discipline {}'.format(self.__get_student(student_id), self.__get_discipline(discipline_id)))
        return what_is_found

    def __validate(self, student_id, discipline_id):
        '''
        Checks if the student_id and discipline_id exist

        :param student_id:
        :param discipline_id:
        :return: None
        :exception:
            conrollerOperationException - if the discipline_id is not found
        '''
        if self.__student_repository.find_by_id(student_id) is None:
            raise EnrollException("There is no student with id {0}".format(student_id))
        if self.__discipline_repository.find_by_id(discipline_id) is None:
            raise EnrollException("There is no discipline with id {0}".format(discipline_id))

    def find_link(self, student_id, discipline_id):
        link_id = (student_id, discipline_id)
        return self.__enroll_repository.find_by_id(link_id)


    def enroll_student(self, student_id, discipline_id):
        '''
        Enrolles student to a ceertain discipline
        :param student_id:
        :param discipline_id:
        :return: None
        '''
        self.__validate(student_id, discipline_id)
        link = Link(student_id, discipline_id)
        try:
             self.__enroll_repository.add(link)
        except:
            raise EnrollException("Student {0} was already enrolled for {1}".format(self.__get_student(student_id),
                                                                                         self.__get_discipline(
                                                                                             discipline_id)))
    def disenroll_student(self, student_id, discipline_id):
        '''
        Disenroll student from a certain discipline
        :param student_id:
        :param discipline_id:
        :return: None
        '''
        self.__validate(student_id, discipline_id)
        link = Link(student_id, discipline_id)
        try:
            self.__enroll_repository.remove_by_id(link)
        except RepositoryException:
            raise EnrollException("Student {0} was already not enrolled for {1}".format(self.__get_student(student_id),
                                                                                        self.__get_discipline(
                                                                                            discipline_id)))
    def disenroll_student_all(self, student_id):
        '''
        Disenroll a certain student from all disciplines
        :param student_id:
        :return: None
        '''

        links = self.__enroll_repository.get_all()
        mark_for_deletion = [link.entity_id for link in links if link.student_id == student_id]
        for link_id in mark_for_deletion:
             self.__enroll_repository.remove_by_id(link_id)

    def disenroll_discipline_all(self, discipline_id):
        '''
        Dienroll all students from a certain discipline
        :param discipline_id:
        :return: None
        '''
        links = self.__enroll_repository.get_all()
        mark_for_deletion = [link.entity_id for link in links if link.discipline_id == discipline_id]
        for link_id in mark_for_deletion:
            self.__enroll_repository.remove_by_id(link_id)

    def get_enrolled_disciplines_for_student(self, student_id):
        '''
        Gets all the disciplines for which studnet with student_id is enrolled
        :param student_id:
        :return: list of discipline ids (ints)
        '''
        links = self.__enroll_repository.get_all()
        enrolled_disciplines = [link.discipline_id for link in links if link.student_id == student_id]
        return enrolled_disciplines

    def get_enrolled_students_for_discipline(self, discipline_id):
        '''
        Gets all the students that are enrolled for discipline with discipline_id
        :param discipline_id:
        :return: list of all student ids (ints)
        '''
        links = self.__enroll_repository.get_all()
        enrolled_students = [link.student_id for link in links if link.discipline_id == discipline_id]
        return enrolled_students

    def __keep_only_valid(self):
        links = self.__enroll_repository.get_all()
        mark_for_deletion = []
        for link in links:
            student_id = link.student_id
            discipline_id = link.discipline_id
            if self.__student_repository.find_by_id(student_id) is None or self.__discipline_repository.find_by_id(discipline_id) is None:
                mark_for_deletion.append(link)

        for link in mark_for_deletion:
            self.__enroll_repository.remove_by_id(link.entity_id)
