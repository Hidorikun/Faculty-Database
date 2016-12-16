'''
Created on Nov 2, 2016

@author: Ok!
'''
import unittest

from controller.discipline_controller import DisciplineController
from controller.grade_controller import GradeController
from controller.student_controller import StudentController
from domain.validators import GradeValidator, StudentValidator, \
    DisciplineValidator
from repository.repository import Repository, GradesRepository


class TestGradeController(unittest.TestCase):

   
    def initialise(self):
        self.student_repository = Repository(StudentValidator)
        self.discipline_repository = Repository(DisciplineValidator)
        self.grade_repository = GradesRepository(GradeValidator)
        self.student_controller = StudentController(self.student_repository)
        self.discipline_controller = DisciplineController(self.discipline_repository)
        self.grade_controller = GradeController(self.grade_repository, self.student_repository, self.discipline_repository)

        self.student_controller.add_student(1, 'George')
        self.student_controller.add_student(2, 'Ada')
        self.student_controller.add_student(3, 'Ana')
        self.student_controller.add_student(4, 'Maria')
        self.student_controller.add_student(5, 'Vlad')
         
        self.discipline_controller.add_discipline(1, 'mate')
        self.discipline_controller.add_discipline(2, 'info')
                  
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.initialise()
        
    def test_enroll_student(self):
        self.grade_controller.enroll_student(3, 1)
        self.grade_controller.enroll_student(1, 2)
        self.grade_controller.enroll_student(1, 1)
        self.grade_controller.enroll_student(2, 1)
        self.grade_controller.enroll_student(2, 2)
        self.grade_controller.enroll_student(3, 2)
        print(len(self.grade_controller.GradeController__enrolled))
        self.assertEqual(len(self.grade_controller.GradeController__enrolled), 6, 'students not successfully enrolled')
        
        print('tested enrolling a student to a discipline')
        
    def test_add_grade(self):
        self.initialise()
        self.grade_controller.enroll_student(1, 2)
        print(self.student_controller.get_all())
        self.grade_controller.add_grade(1, 2, 10)
        self.assertEqual(len(self.grade_controller.get_all()), 1, ' grade not added')
        
        print('tested giving grades to students')
        
    def test_update_grade(self):
        self.grade_controller.update_grade(1, 2, 10, 9)
        #self.assertEqual(self.grade_repository.find_by_id(1, 2)
        
    def test_get_enrolled_disciplines_for_student(self):
        try:
            self.grade_controller.enroll_student(1, 2)
        except:
            pass
        self.assertEqual(len(self.grade_controller.get_enrolled_disciplines_for_student(1)), 1, 'incorrect enrolling for student')
        
        print('tested getting enrolled disciplines for student')
        
    def test_get_enrolled_students_for_discipline(self):
        self.grade_controller.enroll_student(1, 2)
        print(self.grade_controller.get_enrolled_students_for_discipline(2))
        self.assertEqual(len(self.grade_controller.get_enrolled_students_for_discipline(2)), 1, len(self.grade_controller.get_enrolled_students_for_discipline(2)))
        
        print('tested get enrolled students for discipline')
        
    def test_disenroll_studnet(self):
        self.grade_controller.disenroll_student(1, 2)
        self.assertEqual(len(self.grade_controller.get_enrolled_disciplines_for_student(1)), 0, 'dissenrolling student did not work')
        
        print('tested disenrolling student from discipline')

    def test_disenroll_student_all(self):
        
        print('tested disenrolling student from all disciplines')
        
    def test_disenroll_discipline_all(self):
        
        print('tested disenrolling discipline from all students')
        
    def test_get_all(self):
        
        print('tested getting all grades')
        
    def test_remove_by_student_id(self):
        
        print('tested removing by student id')
        
    def test_remove_by_value(self):
        
        print('tested removing by value')
        
    def test_remove_by_dicipline_id(self):
        
        print('tested removing by discipline id')
        
    def test_remove(self):
        
        print('tested removing by grade entity')
        
    def test_get_students_sorted_by_discipline(self):
        
        print('tested geting students sorted by discipline')
        
    def test_get_students_sorted_alphabetically(self):
        
        print('tested geting students sorted alphabetically')
        
    def test_aggregated_avg(self):
        
        print('tested computing aggregated average for student')
        
    def test_aggregated_avg_d(self):
        
        print('tested computing aggregated average for discipline')
        
    def test_get_best_students(self):
        
        print('tested getting best students')
        
    def test_get_best_disciplines(self):
        
        print('tested gettig best discipline')
        
    def test_get_failing_students(self):
        
        print('tested getting failing students')
        
    def test_get_grades_for_student(self):
        
        print('tested getting grades for student')
        
    def test_get_grades_for_discipline(self):
        
        print('tested getting grades for discipline')
        
        
        