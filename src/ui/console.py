
import random

from domain.validators import DatabaseException


class ReadingException(DatabaseException):
    pass

class DomainException(DatabaseException):
    pass

class FindException(DatabaseException):
    pass

class StatisticException(DatabaseException):
    pass

class EasterError(DatabaseException):
    pass

class Console(object):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
    
    def read_nr(self, prompt = ''):
        try:
            return int(input(prompt))
        except ValueError:
            raise ReadingException("You must give an integer value.")
        
    def read_pint(self, prompt = ''):
            nr = self.read_nr(prompt)
            if nr < 0:
                raise ReadingException("You must give a positive value")
            return nr
          
    def __get_student(self, student_id):
        try:
            return self.__student_controller.find_by_id(student_id).name
        except AttributeError:
            raise DomainException("Currently there is no student with id {0}".format(student_id))

    def __get_discipline(self, discipline_id):
        try:
            return self.__discipline_controller.find_by_id(discipline_id).name
        except AttributeError:
            raise DomainException("Currently there is no discipline with id {0}".format(discipline_id))
        
#---------------------------------------student----------------------------------------------------------
    def add_student(self):
        student_id = self.read_pint("student id: ")
        student_name = input("student name: ")
        self.__student_controller.add_student(student_id, student_name)
        self.__undo_redo_controller.memorise()

    def remove_student(self):
        student_id = self.read_pint("student id: ")
        self.__student_controller.remove_by_id(student_id)
        self.__grade_controller.remove_by_student_id(student_id)
        self.__enroll_controller.disenroll_student_all(student_id)
        self.__undo_redo_controller.memorise()

    def update_student(self):
        student_id = self.read_pint("student id: ")
        student_name = input("student new name: ")
        self.__student_controller.update(student_id, student_name)
        self.__undo_redo_controller.memorise()

    def list_students(self):
        student_list = self.__student_controller.get_all()
        if len(student_list) == 0:
            print("Currently there are no students.")
        else:
            for student in self.__student_controller.get_all():
                print('id {id}: {student}'.format(id=student.entity_id, student=student.name))

#--------------------------------discipline---------------------------------------------------------------
    def add_discipline(self):
        discipline_id = self.read_pint("discipline id: ")
        discipline_name = input("discipline name: ")
        self.__discipline_controller.add_discipline(discipline_id, discipline_name)
        self.__undo_redo_controller.memorise()

    def remove_discipline(self):
        discipline_id = self.read_pint("discipline id: ")
        self.__discipline_controller.remove_by_id(discipline_id)
        self.__grade_controller.remove_by_discipline_id(discipline_id)
        self.__enroll_controller.disenroll_discipline_all(discipline_id)
        self.__undo_redo_controller.memorise()

    def update_discipline(self):
        discipline_id = self.read_pint("discipline id: ")
        discipline_name = input("discipline new name: ")
        self.__discipline_controller.update(discipline_id, discipline_name)
        self.__undo_redo_controller.memorise()

    def list_discipline(self):

        discipline_list = self.__discipline_controller.get_all()

        if len(discipline_list) == 0:
            print("Currently there are no disciplines")
        else:
            for discipline in discipline_list:
                print('id {id} : {discipline}'.format(id=discipline.entity_id, discipline=discipline.name))

#----------------------------------enrolled------------------------------------------

    def list_enrolled_disciplines_for_student(self, student_id):
        res = self.__enroll_controller.get_enrolled_disciplines_for_student(student_id)
        if len(res) == 0:
            print("currently {0} is not enrolled for any discipline".format(self.__get_student(student_id)))
        else:
            for discipline_id in res:
                print(self.__get_discipline(discipline_id))

    def list_enrolled_students_for_discipline(self, discipline_id):
        res = self.__enroll_controller.get_enrolled_students_for_discipline(discipline_id)
        if len(res) == 0:
            print(
                "Currently there are no students enrolled for {0}".format(self.__get_discipline(discipline_id)))
        else:
            for student_id in res:
                print("id {0}: {1}".format(student_id, self.__get_student(student_id)))


#----------------------------------grades--------------------------------------------
    def enroll_student(self):
        student_id =self.read_pint("student id:")
        discipline_id = self.read_pint("discipline id: ")
        self.__enroll_controller.enroll_student(student_id, discipline_id)
        self.__undo_redo_controller.memorise()

    def enrolled_disciplines_for_student(self):
        student_id = self.read_pint("student id: ")
        self.list_enrolled_disciplines_for_student(student_id)

    def enrolled_students_for_discipline(self):
        discipline_id = self.read_pint("discipline id:")
        self.list_enrolled_students_for_discipline(discipline_id)

    def add_grade(self):
        student_id = self.read_pint("student id: ")
        discipline_id = self.read_pint("discipline id: ")

        grade_value = self.read_grade("grade: ")

        self.__grade_controller.add_grade(student_id, discipline_id, grade_value)
        self.__undo_redo_controller.memorise()

    def read_grade(self, prompt = ''):
        nr = self.read_pint(prompt)
        if nr < 1 or nr > 10:
            raise ReadingException("Grade must be between 1 and 10")
        return nr

    def remove_grade(self):
        student_id = self.read_pint("student id: ")
        discipline_id = self.read_pint("discipline id: ")
        grade_value  = self.read_grade("grade: ")
        self.__grade_controller.remove(student_id, discipline_id, grade_value)
        self.__undo_redo_controller.memorise()

    def update_grade(self):
        student_id = self.read_pint("student id: ")
        discipline_id = self.read_pint("discipline id: ")
        old_grade  = self.read_grade("old grade: ")
        new_grade = self.read_grade("new grade: ")
        self.__grade_controller.update_grade(student_id, discipline_id, old_grade, new_grade)
        self.__undo_redo_controller.memorise()

#-----------------------------------command---------------------------------------------------------

    def read_command(self):
        try:
            s = input("command:")
            return int(s)
        except ValueError:
            raise KeyError

    def greet_user(self):
        print('Faculty Database version 1.0.0')
        print("To perform an operation, type its corresponding number as a command.")


    def list_grades_all(self):
        printed = False
        for student in self.__student_controller.get_all():
            student_id = student.entity_id
            portfolio = self.__grade_controller.get_grades_for_student(student_id)
            if len(portfolio) == 0:
                continue
            printed = True
            print("id {id}: {student}".format(id = student_id, student = self.__get_student(student_id)))
            for discipline_id in portfolio:
                print("    {discipline}: {grades}".format(discipline = self.__get_discipline(discipline_id),grades = portfolio[discipline_id]))
        if not printed:
            print ("Currently no-one has received any grades")

    def list_grades_for_student(self):
        student_id = self.read_pint("student_id: ")
        portfolio = self.__grade_controller.get_grades_for_student(student_id)
        if len(portfolio) == 0:
            print("{student} has not received yet any grades".format(student = self.__get_student(student_id)))
            return
        for discipline_id in portfolio:
            print("{discipline}: {grades}".format(discipline = self.__get_discipline(discipline_id),grades = portfolio[discipline_id]))

    def list_grades_for_discipline(self):
        discipline_id = self.read_pint("discipline_id: ")
        portfolio = self.__grade_controller.get_grades_for_discipline(discipline_id)
        if len(portfolio) == 0:
            print("No student has yet received any grade at {discipline}".format(discipline = self.__get_discipline(discipline_id)))
            return
        for student_id in portfolio:
            print("{student}: {grades}".format(student = self.__get_student(student_id), grades = portfolio[student_id]))

    def search_student_by_id(self):
        student_id = self.read_pint("student id: ")
        student = self.__student_controller.find_by_id(student_id)
        if student is None:
            raise FindException("Could not find any student with that ID")

        print("id {id}: {student}".format(id = student_id, student = self.__get_student(student_id)))

    def search_student_by_name(self):
        student_name = input("student name: ")
        result = self.__student_controller.find_by_name(student_name)
        if len(result) == 0:
            raise FindException("Could not find any student with matching name")

        for e in result:
            print("id {id}: {student}".format(id = e.entity_id, student = self.__get_student(e.entity_id)))

    def search_discipline_by_id(self):
        discipline_id = self.read_pint("discipline id: ")
        discipline = self.__discipline_controller.find_by_id(discipline_id)
        if discipline is None:
            raise FindException("Could not find any discipline with that ID")

        print("id {id}: {discipline}".format(id = discipline_id, discipline = self.__get_discipline(discipline_id)))

    def search_discipline_by_name(self):
        discipline_name = input("discipline name: ")
        result = self.__discipline_controller.find_by_name(discipline_name)
        if len(result) == 0:
            raise FindException("Could not find any discipline with matching name")

        for e in result:
            print("id {id}: {discipline}".format(id = e.entity_id, discipline = self.__get_discipline(e.entity_id)))

    def search_student(self):
        print('1. search student by id')
        print('2. search student by name')
        answer = self.read_pint('command: ')
        if answer == 1:
            self.search_student_by_id()
        elif answer == 2:
            self.search_student_by_name()
        else:
            raise KeyError

    def search_discipline(self):
        print('1. search discipline by id')
        print('2. search discipline by name')
        answer = self.read_pint('command: ')
        if answer == 1:
            self.search_discipline_by_id()
        elif answer == 2:
            self.search_discipline_by_name()
        else:
            raise KeyError

    def sort_students_by_discipline(self):
        discipline_id = self.read_pint('discipline id :')
        print("--Students sorted by their grades at {discipline}--".format(discipline = self.__get_discipline(discipline_id)))

        student_list = self.__grade_controller.get_students_sorted_by_discipline(discipline_id)
        if len(student_list) == 0:
            raise StatisticException("There are no students enrolled at this discipline")

        for i in range(len(student_list)):
            #student_list is a list of touples with form (Student student, float average)
            print("{rank} : average {average:.2f} id {id} {name}".format(rank = i+1, id = student_list[i][0].entity_id, name = student_list[i][0].name, average = student_list[i][1]))


    def sort_students_alphabetically(self):
        discipline_id = self.read_pint('discipline id: ')
        print("--Students that study {discipline}, sorted alphabetically--".format(discipline = self.__get_discipline(discipline_id)))

        student_list = self.__grade_controller.get_students_sorted_alphabetically(discipline_id)
        if len(student_list) == 0:
            raise StatisticException("There are no students enrolled at this discipline")
        for e in student_list:
            print('id {id}: {name}'.format(id = e.entity_id, name = e.name))

    def sort_students_enrolled_at_discipline(self):
        cmds ={1: self.sort_students_by_discipline,
               2: self.sort_students_alphabetically
               }

        menu = {1: 'order descending based on average grades',
                2: 'order alphabetically'
                }

        for key in menu:
            print("{0}: {1}".format(key, menu[key]))

        cmd = self.read_pint('command: ')
        cmds[cmd]()

    def print_failing_students(self):
        failing_students = self.__grade_controller.get_failing_students()
        print("---Students failing at some disciplines----")
        if len(failing_students) == 0:
            raise StatisticException("There are no students failing at this time")
        for student_id in failing_students:
            disciplines = []
            for discipline_id in failing_students[student_id]:
                disciplines.append(self.__get_discipline(discipline_id))

            print("id {id}: {name} is failing at: {discip}".format(id = student_id, name = self.__get_student(student_id), discip = disciplines))


    def print_best_students_overall(self):
        best_students = self.__grade_controller.get_best_students()
        #tuple (Student object, aggregated_average)
        if len(best_students) == 0:
            raise StatisticException("No student is enrolled for any subject yet")
        printed = False
        for e in best_students:
            if e[1] > 0:
                print('id {id}: {name} - {average}'.format(id = e[0].entity_id, name =e[0].name, average = e[1]))
                printed = True
        if not printed:
            raise StatisticException('Currently no-one has received any grades ')

    def print_best_disciplines(self):
        best_disciplines = self.__grade_controller.get_best_disciplines()
        #tuple (Discipline object, aggregated _average of students
        if len(best_disciplines) == 0:
            raise StatisticException("No students are enrolled for any subject yet")
        printed = True
        for e in best_disciplines:
            if e[1] > 0:
                print('id {id}: {name} - {average}'.format(id = e[0].entity_id, name =e[0].name, average = e[1]))
                printed = True
        if not printed:
            raise StatisticException('Currently no-one has received any grades ')
        
       
    def generate_statistics(self):
        cmds = {1: self.sort_students_enrolled_at_discipline,
                2: self.print_failing_students,
                3: self.print_best_students_overall,
                4: self.print_best_disciplines
                }
        
        menu = {1: 'print all students enrolled at a given discipline, alphabetically or by descending order of average grades',
                2: 'print all students failing at one or more discipline',
                3: 'print students with the best school situation, sorted in descending order of their aggregated average',
                4: 'print all disciplines at which there is at least one grade, sorted in descending order of the average grade received by all students enrolled at that discipline.'
                }
        
        for key in menu:
            print("{0}: {1}".format(key, menu[key]))
                        
        cmd = self.read_pint('command: ')
        cmds[cmd]()
                
    def undo(self):
        self.__undo_redo_controller.undo()

    def redo(self):
        self.__undo_redo_controller.redo()
        
    def run_console(self):
        self.greet_user()
        while True:
            print('')
            cmds = {1: self.add_student,
                    2: self.add_discipline,
                    3: self.add_grade,
                    4: self.remove_student,
                    5: self.remove_discipline,
                    6: self.remove_grade,
                    7: self.list_students,
                    8: self.list_discipline,
                    9: self.enroll_student,
                    10: self.enrolled_disciplines_for_student,
                    11: self.enrolled_students_for_discipline,
                    12: self.list_grades_all,
                    13: self.list_grades_for_student,
                    14: self.list_grades_for_discipline,
                    15: self.update_discipline,
                    16: self.update_student,
                    17: self.update_grade,
                    18: self.search_student,
                    19: self.search_discipline,
                    20: self.generate_statistics,
                    21: self.undo,
                    22: self.redo
                    }
            
            menu = {1: 'add student',
                    2: 'add discipline',
                    3: 'add grade',
                    4: 'remove student',
                    5: 'remove discipline',
                    6: 'remove grade',
                    7: 'list students',
                    8: 'list disciplines',
                    9: 'enroll student at a certain disciplines',
                    10: 'show enrolled disciplines for certain student',
                    11: 'show enrolled students for certain discipline',
                    12: 'list all grades for all students',
                    13: 'list all grades for a given student',
                    14: 'list all grades for a given discipline',
                    15: 'update discipline',
                    16: 'update student',
                    17: 'update grades',
                    18: 'search student based on id/name',
                    19: 'search discipline based on id/name',
                    20: 'generate statistics',
                    21: 'undo LPO (last performed operation)',
                    22: 'redo LPO',
                    0: 'exit application'
                    }                
            
            for e in menu:
                print ("{0}. {1}".format(e, menu[e]))
            
            try:
                cmd = self.read_command()
                if cmd == 0:
                    return
                
                cmds[cmd]()
             
            except DatabaseException as ex:
                print(ex)
            except KeyError:
                print("There is no such command")
                
               
               
               
               
               
               
               
            