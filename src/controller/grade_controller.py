import copy
from _functools import reduce

from domain.entities import Grade
from domain.validators import DatabaseException


class ControllerOperationException(DatabaseException):
    pass

class GradeController(object):


    def __init__(self, grade_repository, student_repository, discipline_repository, enroll_controller):
        self.__grade_repository = grade_repository
        self.__student_repository = student_repository
        self.__discipline_repository = discipline_repository
        self.__enroll_controller = enroll_controller

    def find_by_value(self, value):
        '''
        returns all grades that have value 'value'
        returns empty list if there are no grades with value 'value'
        '''
        return [g for g in self.__grade_repository.get_all() if g.value == value]

    def find_specific(self, student_id, discipline_id, grade_value):
        '''
        :return
            first found grade object with certain student_id, discipline_id, grade_value
            none if such grade is not found
        '''

        for g in self.__grade_repository.get_all():
            if g.student_id == student_id and g.discipline_id == discipline_id and g.value == grade_value:
                return g
        return None

    def update(self, student_id, discipline_id, grade_value, new_grade):
        '''
        :args:
            student_id - the student id of the old grade
            discipline_id - the discipline id of the old grade
            grade_value - the grade value of the old grade
            new_grade - the entity of the grade that will replace the old one
        :effect:
            replace the old grade with the new_grade if it exists
            add new_grade to the repository otherwise
        '''
        grades = self.__grade_repository.get_all()
        old_grade = None
        for i in range(len(grades)):
            if grades[i].student_id == student_id and grades[i].discipline_id == discipline_id and \
                            grades[i].value == grade_value:
                old_grade = grades[i]

        if old_grade is None:
            raise ControllerOperationException("you can't update something that does not exist")

        new_grade = Grade(student_id, discipline_id, new_grade)
        self.remove(old_grade.student_id, old_grade.discipline_id, old_grade.grade_value)
        self.add_grade(new_grade)

    def remove_by_student_id(self, student_id):
        '''
        removes all grades for certain student_id
        '''

        grades = list(self.__grade_repository.get_all())
        mark_for_deletion = [g.entity_id for g in grades if g.student_id == student_id]
        for grade_id in mark_for_deletion:
            self.__grade_repository.remove_by_id(grade_id)

    def remove_by_value(self, grade_value):
        '''
        removes all grades for certain grade_value
        '''
        grades = self.__grade_repository.get_all()
        mark_for_deletion = [g.entity_id for g in grades if g.value == grade_value]
        for grade_id in mark_for_deletion:
            self.__grade_repository.remove_by_id(grade_id)

    def remove_by_discipline_id(self, discipline_id):
        '''
        removes all grades for certain discipline
        '''
        grades = self.__grade_repository.get_all()
        marked_for_deletion = [g.entity_id for g in grades if g.discipline_id == discipline_id]
        for grade_id in marked_for_deletion:
            self.__grade_repository.remove_by_id(grade_id)

    def remove(self, student_id, discipline_id, grade_value):
        '''
        removes a grade for student_id at discipline_id with grade_value
        '''

        grades  = list(self.__grade_repository.get_all())
        found = False
        for g in grades:
            if g.student_id == student_id and g.discipline_id == discipline_id and g.value == grade_value:
                grade_id = g.entity_id
                self.__grade_repository.remove_by_id(grade_id)
                found = True
                break

        if not found:
            raise ControllerOperationException('Student {} does not have {} at {}'.format(self.__get_student(student_id), grade_value, self.__get_discipline(discipline_id)))

    def __get_student(self, student_id):
        '''
        gets the student name for student_id 
        except 
            ControllerOperationException - if the student_id is not found 
        '''
        try:
            return self.__student_repository.find_by_id(student_id).name
        except AttributeError:
            raise ControllerOperationException("Currently there is no student with id {0}".format(student_id))
        
    def __get_discipline(self, discipline_id):
        '''
        gets the discipline name for discipline_id
        except:
            ControllerOperationException - if the grade_id is not found
        '''
        try:
            return self.__discipline_repository.find_by_id(discipline_id).name
        except AttributeError:
            raise ControllerOperationException("Currently there is no discipline with id {0}".format(discipline_id))
         
    def __validate(self, student_id, discipline_id):
        '''
        checks if the student_id and discipline_id exist
        exception:
            conrollerOperationException - if the discipline_id is not found 
        '''
        if self.__student_repository.find_by_id(student_id) is None:
            raise ControllerOperationException("There is no student with id {0}".format(student_id))
        if self.__discipline_repository.find_by_id(discipline_id) is None:
            raise ControllerOperationException("There is no discipline with id {0}".format(discipline_id))
        
    def update_grade(self, student_id, discipline_id, old_value, new_value):
        '''
        Updates a the grade identified by student_id, discipline_id and the old_value, and replaces its value with
        a new_value
        :param student_id:
        :param discipline_id:
        :param old_value:
        :param new_value:
        :return: None
        '''
        old_grade = self.find_specific(student_id, discipline_id, old_value)
        new_grade = Grade(student_id, discipline_id, new_value)
        if old_grade is None:
            old_grade = Grade(student_id, discipline_id, old_value)

        self.__grade_repository.update(old_grade.entity_id, new_grade)
        
    
    def add_grade(self, student_id, discipline_id, grade_value):
        '''
        Adds a grde to the repository
        :param student_id:
        :param discipline_id:
        :param grade_value:
        :return: None
        :exception: ControllerOperationExcption if the student with student_id is not enrolled for discipline with \
        discipline_id
        '''
        self.__validate(student_id, discipline_id)
        link_id = (student_id, discipline_id)
        if self.__enroll_controller.find_by_id(link_id) is None:
            raise ControllerOperationException('student was not enrolled for given discipline')

        grade = Grade(student_id, discipline_id, grade_value)
        self.__grade_repository.add(grade)

    def get_all(self):
        '''
        Gets all grades
        :return: list of all grade objects in given repository
        '''
        return list(self.__grade_repository.get_all())

    def average(self, student_id, discipline_id):
        '''
        Computes the average grade of a student for a certain discipline
        :param student_id:
        :param discipline_id:
        :return: average(int)
        '''
        self.__validate(student_id, discipline_id)
        grades_list = self.get_grades_for_student(student_id)
        if discipline_id not in grades_list:
            return 0
        
        a_sum = 0.0
        for e in grades_list[discipline_id]:
            a_sum += e
        return a_sum/len(grades_list[discipline_id])
        
    def avg(self, a_list):
        '''
        :param a_list
        :returns the average between the elements of the list a_list
        '''
        a_sum = float(reduce(lambda x, y: x+y, a_list))
        return a_sum / len(a_list)
        
        
    def get_students_sorted_by_discipline(self, discipline_id):
        '''
        Returns a sorted list of students based on their average for a certain discipline
        :param discipline_id:
        :return: List of student objects
        '''
        student_list = self.__student_repository.get_all()
        student_list = [e for e in student_list if self.__enroll_controller.find_by_id((e.entity_id, discipline_id)) is not None]
        student_list = [(e, self.average(e.entity_id, discipline_id)) for e in student_list]
        student_list = sorted(student_list, key = lambda student: student[1], reverse = True)
        return student_list
    
    def get_students_sorted_alphabetically(self,discipline_id):
        '''
        Returns a list of students enrolled for a certain dicipline sorted alphabetically
        :param discipline_id:
        :return: List of student objects
        '''
        student_list = self.__student_repository.get_all()
        student_list = [e for e in student_list if self.__enroll_controller.find_by_id((e.entity_id, discipline_id)) is not None]
        student_list = sorted(student_list, key = lambda student: student.name)
        return student_list
    
    def aggregated_avg(self,student_id):
        '''
        Computes the aggregated average of a student ( average of all discipline averages)
        :param student_id: the positive integer id of a student
        :return: the aggregated average (int)
        '''
        grades = self.get_grades_for_student(student_id)
        disciplines = [discipline for discipline in grades]
        grades = [self.average(student_id, discipline_id) for discipline_id in disciplines]
        if len(grades) == 0:
            return 0
        
        a_sum = float(reduce(lambda x, y: x+y, grades))
        return a_sum / len(disciplines)
        
        
    def aggregated_avg_d(self, discipline_id):
        '''
        Computes the aggregated average of a discipline
        :param discipline_id:
        :return: the aggregated average (int)
        '''
        students = self.get_grades_for_discipline(discipline_id)
        grades = [self.average(student_id, discipline_id) for student_id in students]
        if len(grades) == 0:
            return 0
        
        a_sum = float(reduce(lambda x, y: x+y, grades))
        return a_sum / len(students)
    
    def get_best_students(self):
        '''
        Gets a list of all students ordered descendingly their aggregated average
        :return: list of student objects
        '''
        student_list = self.__student_repository.get_all()
        best_students = []
        
        for student in student_list:
            best_students.append((student, self.aggregated_avg(student.entity_id)))
        if len(best_students) != 0:
            best_students = sorted(best_students, key = lambda x : x[1], reverse = True)
        else:
            best_students = []
            
        return best_students
    
    def get_best_disciplines(self):
        '''
        Gets a list of all students ordered descendingly their aggregated average
        :return: list of student objects
        '''
        discipline_list = self.__discipline_repository.get_all() 
        best_disciplines = []
        
        
        for discipline in discipline_list:
            best_disciplines.append((discipline, self.aggregated_avg_d(discipline.entity_id)))
        if len(best_disciplines) != 0:
            best_disciplines =sorted(best_disciplines, key = lambda x: x[1], reverse = True)
        else:
            best_disciplines = []
            
        return best_disciplines
            
    def get_failing_students(self):
        '''
        Get a list of failing students ( a student is failing if his/hers average at a discipline is  lower than 5
        :return: list of student objects
        '''
        student_list = self.__student_repository.get_all()
        failing_students = {}
        for e in student_list:
            disciplines = self.__enroll_controller.get_enrolled_disciplines_for_student(e.entity_id)
            for discipline_id in disciplines:
                average = self.average(e.entity_id, discipline_id)
                if average > 0 and average < 5:
                    if e.entity_id not in failing_students:
                        failing_students[e.entity_id] = [discipline_id]
                    else:
                        failing_students[e.entity_id].append(discipline_id)
        return failing_students
                    
                    
    def get_grades_for_student(self, student_id):
        '''
        get a portfolio of all grades for a certain student x
        :param student_id: the id of the student
        :return: dictionary with keys = the disciplines that student x is enrolled for and values = lists of integer \
        values representing the grades for that discipline
        '''
        portfolio = {}
        for g in self.__grade_repository.get_all():
            if g.student_id == student_id:
                if g.discipline_id not in portfolio:
                    portfolio[g.discipline_id] = [g.value]  
                else:
                    portfolio[g.discipline_id].append(g.value)
        return portfolio
    
    def get_grades_for_discipline(self, discipline_id):
        '''
        Get a portfolio of all grades for a certain discipline x
        :param discipline_id: the id of the discipline
        :return: dictionary with keys = the students that are enrolled for discipline x and values = lists of integer \
        values representing the student grades at discipline x
        '''
        portfolio = {}
        for g in self.__grade_repository.get_all():
            if g.discipline_id == discipline_id:
                if g.student_id not in portfolio:
                    portfolio[g.student_id] = [g.value]  
                else:
                    portfolio[g.student_id].append(g.value)
        return portfolio
        