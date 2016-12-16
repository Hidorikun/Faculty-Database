'''
Created on Nov 3, 2016

@author: Ok!
'''
import traceback

from Settings.SettingsClass import Settings
from controller.discipline_controller import DisciplineController
from controller.enrolled_controller import EnrolledController
from controller.grade_controller import GradeController
from controller.student_controller import StudentController
from controller.undo_redo_controller import UndoRedoController
from domain.entities import Student, Discipline, Grade, Link
from domain.validators import GradeValidator, StudentValidator, \
    DisciplineValidator, EnrollValidator
from repository.file_repositories import FileRepository
from repository.pickle_repository import PickleRepository
from ui.console import Console
from ui.gui_console import GUIConsole

if __name__ == "__main__":
    try:
        settings = Settings('../../data/settings.property')

        if settings['repository']  == 'file':
            student_repository = FileRepository(StudentValidator, settings['students'], Student)
            discipline_repository = FileRepository(DisciplineValidator, settings['disciplines'], Discipline)
            grade_repository = FileRepository(GradeValidator, settings['grades'], Grade )
            enroll_repository = FileRepository(EnrollValidator, settings['enroll'], Link)

        if settings['repository'] == 'binary':
            student_repository = PickleRepository(StudentValidator, settings['students'], Student)
            discipline_repository = PickleRepository(DisciplineValidator, settings['disciplines'], Discipline)
            grade_repository = PickleRepository(GradeValidator, settings['grades'], Grade)
            enroll_repository = PickleRepository(EnrollValidator, settings['enroll'], Link)

        enroll_controller = EnrolledController(enroll_repository, student_repository, discipline_repository)
        student_controller = StudentController(student_repository)
        discipline_controller = DisciplineController(discipline_repository)
        grade_controller = GradeController(grade_repository, student_repository, discipline_repository, enroll_controller)

        undo_redo_controller = UndoRedoController(student_repository, discipline_repository, grade_repository, enroll_controller)

        if settings['ui'] == 'command':
            console = Console(student_controller, grade_controller, discipline_controller, enroll_controller,
                              undo_redo_controller)

        if settings['ui'] == 'GUI':
            console = GUIConsole(student_controller, grade_controller, discipline_controller, enroll_controller,
                                 undo_redo_controller)

        console.run_console()

    except Exception as ex:
        print(ex)
        traceback.print_exc()

    print("bye")
