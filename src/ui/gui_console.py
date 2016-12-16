
import sys 

from PyQt4 import QtCore, QtGui

from ui.console import DomainException, FindException, StatisticException


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def errorProne(f):
    def f_wrapper(self, *args):
        try:
            f(self)
        except Exception as error_message:
            ex.popup_exception(str(error_message))
    return f_wrapper




class Ui_GRADE_INPUT(QtGui.QWidget):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, GRADE_INPUT):
        GRADE_INPUT.setObjectName(_fromUtf8("GRADE_INPUT"))
        GRADE_INPUT.resize(388, 219)
        self.id_label = QtGui.QLabel(GRADE_INPUT)
        self.id_label.setGeometry(QtCore.QRect(10, 20, 81, 41))
        self.id_label.setObjectName(_fromUtf8("id_label"))
        self.name_label = QtGui.QLabel(GRADE_INPUT)
        self.name_label.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.add_btn = QtGui.QPushButton(GRADE_INPUT)
        self.add_btn.setGeometry(QtCore.QRect(100, 150, 151, 51))
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.id_input_line = QtGui.QLineEdit(GRADE_INPUT)
        self.id_input_line.setGeometry(QtCore.QRect(80, 20, 281, 31))
        self.id_input_line.setObjectName(_fromUtf8("id_input_line"))
        self.name_input_line = QtGui.QLineEdit(GRADE_INPUT)
        self.name_input_line.setGeometry(QtCore.QRect(80, 60, 281, 31))
        self.name_input_line.setObjectName(_fromUtf8("name_input_line"))
        self.name_input_line_2 = QtGui.QLineEdit(GRADE_INPUT)
        self.name_input_line_2.setGeometry(QtCore.QRect(80, 100, 281, 31))
        self.name_input_line_2.setText(_fromUtf8(""))
        self.name_input_line_2.setObjectName(_fromUtf8("name_input_line_2"))
        self.name_label_2 = QtGui.QLabel(GRADE_INPUT)
        self.name_label_2.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.name_label_2.setObjectName(_fromUtf8("name_label_2"))

        self.retranslateUi(GRADE_INPUT)
        QtCore.QMetaObject.connectSlotsByName(GRADE_INPUT)
    
    def retranslateUi(self, GRADE_INPUT):
        GRADE_INPUT.setWindowTitle(_translate("GRADE_INPUT", "Add Grade", None))
        self.id_label.setText(_translate("GRADE_INPUT", "Student ID:", None))
        self.name_label.setText(_translate("GRADE_INPUT", "Discipline ID:", None))
        self.add_btn.setText(_translate("GRADE_INPUT", "Add Grade", None))
        self.name_label_2.setText(_translate("GRADE_INPUT", "Grade value:", None))
        self.add_btn.clicked.connect(self.add_grade)
    @errorProne
    def add_grade(self):
        student_id = int(self.id_input_line.text())
        discipline_id = int(self.name_input_line.text())
        grade_value = int(self.name_input_line_2.text())
        
        self.__grade_controller.add_grade(student_id, discipline_id, grade_value)
        self.__undo_redo_controller.memorise()

class Ui_DISCIPLINE_INPUT(QtGui.QWidget):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, DISCIPLINE_INPUT):
        DISCIPLINE_INPUT.setObjectName(_fromUtf8("DISCIPLINE_INPUT"))
        DISCIPLINE_INPUT.resize(388, 170)
        self.id_label = QtGui.QLabel(DISCIPLINE_INPUT)
        self.id_label.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.id_label.setObjectName(_fromUtf8("id_label"))
        self.name_label = QtGui.QLabel(DISCIPLINE_INPUT)
        self.name_label.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.add_btn = QtGui.QPushButton(DISCIPLINE_INPUT)
        self.add_btn.setGeometry(QtCore.QRect(110, 100, 151, 51))
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.id_input_line = QtGui.QLineEdit(DISCIPLINE_INPUT)
        self.id_input_line.setGeometry(QtCore.QRect(50, 19, 311, 31))
        self.id_input_line.setObjectName(_fromUtf8("id_input_line"))
        self.name_input_line = QtGui.QLineEdit(DISCIPLINE_INPUT)
        self.name_input_line.setGeometry(QtCore.QRect(50, 60, 311, 31))
        self.name_input_line.setObjectName(_fromUtf8("name_input_line"))

        self.retranslateUi(DISCIPLINE_INPUT)
        QtCore.QMetaObject.connectSlotsByName(DISCIPLINE_INPUT)

    def retranslateUi(self, DISCIPLINE_INPUT):
        DISCIPLINE_INPUT.setWindowTitle(_translate("DISCIPLINE_INPUT", "Add discipline", None))
        self.id_label.setText(_translate("DISCIPLINE_INPUT", "ID:", None))
        self.name_label.setText(_translate("DISCIPLINE_INPUT", "Name:", None))
        self.add_btn.setText(_translate("DISCIPLINE_INPUT", "Add Discipline", None))
        self.add_btn.clicked.connect(self.add_discipline)
    @errorProne
    def add_discipline(self):
        discipline_id = int(self.id_input_line.text())
        discipline_name = self.name_input_line.text()
        self.__discipline_controller.add_discipline(discipline_id, discipline_name)
        self.__undo_redo_controller.memorise()

class Ui_STUDENT_INPUT(QtGui.QWidget):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, STUDENT_INPUT):
        STUDENT_INPUT.setObjectName(_fromUtf8("STUDENT_INPUT"))
        STUDENT_INPUT.resize(388, 170)
        self.id_label = QtGui.QLabel(STUDENT_INPUT)
        self.id_label.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.id_label.setObjectName(_fromUtf8("id_label"))
        self.name_label = QtGui.QLabel(STUDENT_INPUT)
        self.name_label.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.add_btn = QtGui.QPushButton(STUDENT_INPUT)
        self.add_btn.setGeometry(QtCore.QRect(110, 100, 151, 51))
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.id_input_line = QtGui.QLineEdit(STUDENT_INPUT)
        self.id_input_line.setGeometry(QtCore.QRect(50, 19, 311, 31))
        self.id_input_line.setObjectName(_fromUtf8("id_input_line"))
        self.name_input_line = QtGui.QLineEdit(STUDENT_INPUT)
        self.name_input_line.setGeometry(QtCore.QRect(50, 60, 311, 31))
        self.name_input_line.setObjectName(_fromUtf8("name_input_line"))

        self.retranslateUi(STUDENT_INPUT)
        QtCore.QMetaObject.connectSlotsByName(STUDENT_INPUT)

    def retranslateUi(self, STUDENT_INPUT):
        STUDENT_INPUT.setWindowTitle(_translate("STUDENT_INPUT", "Add student", None))
        self.id_label.setText(_translate("STUDENT_INPUT", "ID:", None))
        self.name_label.setText(_translate("STUDENT_INPUT", "Name:", None))
        self.add_btn.setText(_translate("STUDENT_INPUT", "Add Student", None))
        self.add_btn.clicked.connect(self.add_student)
    @errorProne
    def add_student(self):
        student_id = int(self.id_input_line.text())
        student_name = self.name_input_line.text()
        self.__student_controller.add_student(student_id, student_name)
        self.__undo_redo_controller.memorise()
        


class Ui_DESCENDING(QtGui.QWidget):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, REMOVE_GRADE_INPUT):
        REMOVE_GRADE_INPUT.setObjectName(_fromUtf8("REMOVE_GRADE_INPUT"))
        REMOVE_GRADE_INPUT.resize(376, 222)
        self.le_button = QtGui.QPushButton(REMOVE_GRADE_INPUT)
        self.le_button.setGeometry(QtCore.QRect(90, 120, 171, 61))
        self.le_button.setObjectName(_fromUtf8("le_button"))
        self.id_line = QtGui.QLineEdit(REMOVE_GRADE_INPUT)
        self.id_line.setGeometry(QtCore.QRect(110, 40, 241, 31))
        self.id_line.setObjectName(_fromUtf8("id_line"))
        self.label = QtGui.QLabel(REMOVE_GRADE_INPUT)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(REMOVE_GRADE_INPUT)
        QtCore.QMetaObject.connectSlotsByName(REMOVE_GRADE_INPUT)

    def retranslateUi(self, REMOVE_GRADE_INPUT):
        REMOVE_GRADE_INPUT.setWindowTitle(_translate("REMOVE_GRADE_INPUT", "Sort students based on grades", None))
        self.le_button.setText(_translate("REMOVE_GRADE_INPUT", "SORT", None))
        self.label.setText(_translate("REMOVE_GRADE_INPUT", "Discipline ID:", None))
        self.le_button.clicked.connect(self.gen_descending) 
    
    
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
    @errorProne    
    def gen_descending(self):
        ex.listView.clear()
        discipline_id = int(self.id_line.text())
        ex.listView.addItem("--Students sorted by their grades at {discipline}--".format(discipline = self.__get_discipline(discipline_id)))
       
        student_list = self.__grade_controller.get_students_sorted_by_discipline(discipline_id)
        if len(student_list) == 0:
            raise StatisticException("There are no students enrolled at this discipline")
        
        for i in range(len(student_list)):
            #student_list is a list of touples with form (Student student, float average)
            ex.listView.addItem("{rank}, average {average:.2f} id {id} {name}".format(rank = i, id = student_list[i][0].entity_id, name = student_list[i][0].name, average = student_list[i][1]))


class Ui_ALPHABETICALLY(QtGui.QWidget):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, REMOVE_GRADE_INPUT):
        REMOVE_GRADE_INPUT.setObjectName(_fromUtf8("REMOVE_GRADE_INPUT"))
        REMOVE_GRADE_INPUT.resize(376, 222)
        self.le_button = QtGui.QPushButton(REMOVE_GRADE_INPUT)
        self.le_button.setGeometry(QtCore.QRect(90, 120, 171, 61))
        self.le_button.setObjectName(_fromUtf8("le_button"))
        self.id_line = QtGui.QLineEdit(REMOVE_GRADE_INPUT)
        self.id_line.setGeometry(QtCore.QRect(110, 40, 241, 31))
        self.id_line.setObjectName(_fromUtf8("id_line"))
        self.label = QtGui.QLabel(REMOVE_GRADE_INPUT)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(REMOVE_GRADE_INPUT)
        QtCore.QMetaObject.connectSlotsByName(REMOVE_GRADE_INPUT)

    def retranslateUi(self, REMOVE_GRADE_INPUT):
        REMOVE_GRADE_INPUT.setWindowTitle(_translate("REMOVE_GRADE_INPUT", "Sort students alphabetically", None))
        self.le_button.setText(_translate("REMOVE_GRADE_INPUT", "SORT", None))
        self.label.setText(_translate("REMOVE_GRADE_INPUT", "Discipline ID:", None))
        self.le_button.clicked.connect(self.gen_alphabetically)
    
    
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
    @errorProne    
    def gen_alphabetically(self): 
        ex.listView.clear()
        discipline_id = int(self.id_line.text())
        ex.listView.addItem("--Students that study {discipline}, sorted alphabetically--".format(discipline = self.__get_discipline(discipline_id)))
        
        student_list = self.__grade_controller.get_students_sorted_alphabetically(discipline_id)
        if len(student_list) == 0:
            raise StatisticException("There are no students enrolled at this discipline")
        for e in student_list:
            ex.listView.addItem('id {id}: {name}'.format(id = e.entity_id, name = e.name))
            

class Ui_STATISTICS_MENU(QtGui.QWidget):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, STATISTICS_MENU):
        STATISTICS_MENU.setObjectName(_fromUtf8("STATISTICS_MENU"))
        STATISTICS_MENU.resize(529, 391)
        self.verticalLayout = QtGui.QVBoxLayout(STATISTICS_MENU)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.alpha_btn = QtGui.QPushButton(STATISTICS_MENU)
        self.alpha_btn.setObjectName(_fromUtf8("alpha_btn"))
        self.verticalLayout.addWidget(self.alpha_btn)
        self.descending_btn = QtGui.QPushButton(STATISTICS_MENU)
        self.descending_btn.setObjectName(_fromUtf8("descending_btn"))
        self.verticalLayout.addWidget(self.descending_btn)
        self.failing_btn = QtGui.QPushButton(STATISTICS_MENU)
        self.failing_btn.setObjectName(_fromUtf8("failing_btn"))
        self.verticalLayout.addWidget(self.failing_btn)
        self.best_students_btn = QtGui.QPushButton(STATISTICS_MENU)
        self.best_students_btn.setObjectName(_fromUtf8("best_students_btn"))
        self.verticalLayout.addWidget(self.best_students_btn)
        self.best_disciplines = QtGui.QPushButton(STATISTICS_MENU)
        self.best_disciplines.setObjectName(_fromUtf8("best_disciplines"))
        self.verticalLayout.addWidget(self.best_disciplines)

        self.retranslateUi(STATISTICS_MENU)
        QtCore.QMetaObject.connectSlotsByName(STATISTICS_MENU)

    def retranslateUi(self, STATISTICS_MENU):
        STATISTICS_MENU.setWindowTitle(_translate("STATISTICS_MENU", "Statistics menu", None))
        self.alpha_btn.setText(_translate("STATISTICS_MENU", "PRINT all students enrolled at a given discipline, alphabetically", None))
        self.descending_btn.setText(_translate("STATISTICS_MENU", "PRINT all students enrolled at a given discipline, sorded in descending order ", None))
        self.failing_btn.setText(_translate("STATISTICS_MENU", "PRINT all studend failing at one or more disciplines", None))
        self.best_students_btn.setText(_translate("STATISTICS_MENU", "PRINT students with best situations, sorted in descending order o their aggregated avarage", None))
        self.best_disciplines.setText(_translate("STATISTICS_MENU", "PRINT all disciplines sorted in descending order of the average grade received by all enrolled students", None))
        self.alpha_btn.clicked.connect(self.call_alpha)
        self.descending_btn.clicked.connect(self.call_descending) 
        self.best_students_btn.clicked.connect(self.print_best_students)
        self.best_disciplines.clicked.connect(self.print_best_disciplines)
        self.failing_btn.clicked.connect(self.print_failing_students)
        
    
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
        
    @errorProne    
    def print_failing_students(self):
        ex.listView.clear()
        failing_students = self.__grade_controller.get_failing_students()
        ex.listView.addItem("---Students failing at some disciplines----")
        if len(failing_students) == 0:
            raise StatisticException("There are no students failing at this time")
        for student_id in failing_students:
            disciplines = []
            for discipline_id in failing_students[student_id]:
                disciplines.append(self.__get_discipline(discipline_id))
        
            ex.listView.addItem("id {id}: {name} is failing at: {discip}".format(id = student_id, name = self.__get_student(student_id), discip = disciplines))
        
    def call_alpha(self):
        global alpha
        alpha =  Ui_ALPHABETICALLY(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        alpha.show() 
        
    def call_descending(self):
        global descending
        descending =  Ui_DESCENDING(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        descending.show() 
    @errorProne    
    def print_best_students(self):
        ex.listView.clear()
        best_students = self.__grade_controller.get_best_students()
        #tuple (Student object, aggregated_average)
        if len(best_students) == 0:
            raise StatisticException("No student is enrolled for any subject yet")
        printed = False
        for e in best_students:
            if e[1] > 0:
                ex.listView.addItem('id {id}: {name} - {average}'.format(id = e[0].entity_id, name =e[0].name, average = e[1]))
                printed = True
        if not printed:
            raise StatisticException('Currently no-one has received any grades ')
    @errorProne    
    def print_best_disciplines(self):
        ex.listView.clear()
        best_disciplines = self.__grade_controller.get_best_disciplines()
        #tuple (Discipline object, aggregated _average of students
        if len(best_disciplines) == 0:
            raise StatisticException("No students are enrolled for any subject yet")
        printed = True
        for e in best_disciplines:
            if e[1] > 0:
                ex.listView.addItem('id {id}: {name} - {average}'.format(id = e[0].entity_id, name =e[0].name, average = e[1]))
                printed = True
        if not printed:
            raise StatisticException('Currently no-one has received any grades ')
        
class Ui_id_serach_MENU(QtGui.QWidget):
      
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, id_serach_MENU):
        id_serach_MENU.setObjectName(_fromUtf8("id_serach_MENU"))
        id_serach_MENU.resize(400, 211)
        self.textEdit = QtGui.QTextEdit(id_serach_MENU)
        self.textEdit.setGeometry(QtCore.QRect(30, 30, 331, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.id_serach_student_btn = QtGui.QPushButton(id_serach_MENU)
        self.id_serach_student_btn.setGeometry(QtCore.QRect(30, 70, 161, 101))
        self.id_serach_student_btn.setObjectName(_fromUtf8("id_serach_student_btn"))
        self.id_serach_discipline_btn = QtGui.QPushButton(id_serach_MENU)
        self.id_serach_discipline_btn.setGeometry(QtCore.QRect(200, 70, 161, 101))
        self.id_serach_discipline_btn.setObjectName(_fromUtf8("id_serach_discipline_btn"))

        self.retranslateUi(id_serach_MENU)
        QtCore.QMetaObject.connectSlotsByName(id_serach_MENU)

    def retranslateUi(self, id_serach_MENU):
        id_serach_MENU.setWindowTitle(_translate("id_serach_MENU", "Search students/disciplines by ID", None))
        self.textEdit.setHtml(_translate("id_serach_MENU", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta id=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Enter student/discipline id here...</span></p></body></html>", None))
        self.id_serach_student_btn.setText(_translate("id_serach_MENU", "Search student by ID", None))
        self.id_serach_discipline_btn.setText(_translate("id_serach_MENU", "Search discipline by ID", None))
        self.id_serach_student_btn.clicked.connect(self.search_student)
        self.id_serach_discipline_btn.clicked.connect(self.search_discipline)
        
        
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
    @errorProne    
    def search_student(self):
        ex.listView.clear()
        student_id = int(self.textEdit.toPlainText())
        student = self.__student_controller.find_by_id(student_id)
        if student is None:
            raise FindException("Could not find any student with that ID")
        
        ex.listView.addItem("id {id}: {student}".format(id = student_id, student = self.__get_student(student_id)))
    @errorProne    
    def search_discipline(self):
        ex.listView.clear()
        discipline_id = int(self.textEdit.toPlainText())
        discipline = self.__discipline_controller.find_by_id(discipline_id)
        if discipline is None:
            raise FindException("Could not find any discipline with that ID")
        
        ex.listView.addItem("id {id}: {discipline}".format(id = discipline_id, discipline = self.__get_discipline(discipline_id)))
        
class Ui_name_serach_MENU(QtGui.QWidget):
      
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, name_serach_MENU):
        name_serach_MENU.setObjectName(_fromUtf8("name_serach_MENU"))
        name_serach_MENU.resize(400, 211)
        self.textEdit = QtGui.QTextEdit(name_serach_MENU)
        self.textEdit.setGeometry(QtCore.QRect(30, 30, 331, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.name_serach_student_btn = QtGui.QPushButton(name_serach_MENU)
        self.name_serach_student_btn.setGeometry(QtCore.QRect(30, 70, 161, 101))
        self.name_serach_student_btn.setObjectName(_fromUtf8("name_serach_student_btn"))
        self.name_serach_discipline_btn = QtGui.QPushButton(name_serach_MENU)
        self.name_serach_discipline_btn.setGeometry(QtCore.QRect(200, 70, 161, 101))
        self.name_serach_discipline_btn.setObjectName(_fromUtf8("name_serach_discipline_btn"))

        self.retranslateUi(name_serach_MENU)
        QtCore.QMetaObject.connectSlotsByName(name_serach_MENU)

    def retranslateUi(self, name_serach_MENU):
        name_serach_MENU.setWindowTitle(_translate("name_serach_MENU", "Search students/disciplines by name", None))
        self.textEdit.setHtml(_translate("name_serach_MENU", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Enter student/discipline name here...</span></p></body></html>", None))
        self.name_serach_student_btn.setText(_translate("name_serach_MENU", "Search students by name", None))
        self.name_serach_discipline_btn.setText(_translate("name_serach_MENU", "Search disciplines by name", None))
        self.name_serach_student_btn.clicked.connect(self.search_student) 
        self.name_serach_discipline_btn.clicked.connect(self.search_discipline)
    
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
    @errorProne    
    def search_student(self):
        ex.listView.clear()
        student_name = self.textEdit.toPlainText()
        result = self.__student_controller.find_by_name(student_name)
        if len(result) == 0:
            raise FindException("Could not find any student with matching name")
        
        for e in result:
            ex.listView.addItem("id {id}: {student}".format(id = e.entity_id, student = self.__get_student(e.entity_id)))
        
    @errorProne
    def search_discipline(self):
        ex.listView.clear()
        discipline_name = self.textEdit.toPlainText()
        result = self.__discipline_controller.find_by_name(discipline_name)
        if len(result) == 0:
            raise FindException("Could not find any discipline with matching name")
        
        for e in result:
            ex.listView.addItem("id {id}: {discipline}".format(id = e.entity_id, discipline = self.__get_discipline(e.entity_id)))
        
class Ui_SEARCH_MENU(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, SEARCH_MENU):
        SEARCH_MENU.setObjectName(_fromUtf8("SEARCH_MENU"))
        SEARCH_MENU.resize(400, 179)
        self.by_id_btn = QtGui.QPushButton(SEARCH_MENU)
        self.by_id_btn.setGeometry(QtCore.QRect(30, 30, 151, 111))
        self.by_id_btn.setObjectName(_fromUtf8("by_id_btn"))
        self.by_name_btn = QtGui.QPushButton(SEARCH_MENU)
        self.by_name_btn.setGeometry(QtCore.QRect(220, 30, 161, 111))
        self.by_name_btn.setObjectName(_fromUtf8("by_name_btn"))

        self.retranslateUi(SEARCH_MENU)
        QtCore.QMetaObject.connectSlotsByName(SEARCH_MENU)

    def retranslateUi(self, SEARCH_MENU):
        SEARCH_MENU.setWindowTitle(_translate("SEARCH_MENU", "Search menu", None))
        self.by_id_btn.setText(_translate("SEARCH_MENU", "Sreach by ID", None))
        self.by_name_btn.setText(_translate("SEARCH_MENU", "Search by name", None))
        self.by_name_btn.clicked.connect(self.call_by_name_input)
        self.by_id_btn.clicked.connect(self.call_by_id_input)
        
        
    def call_by_name_input(self):
        global by_name_input
        by_name_input = Ui_name_serach_MENU(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        by_name_input.show() 
    
    def call_by_id_input(self):
        global by_id_input
        by_id_input = Ui_id_serach_MENU(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        by_id_input.show() 
    

class Ui_ENROLL_INPUT(QtGui.QWidget):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, ENROLL_INPUT):
        ENROLL_INPUT.setObjectName(_fromUtf8("ENROLL_INPUT"))
        ENROLL_INPUT.resize(376, 191)
        self.student_id_label = QtGui.QLabel(ENROLL_INPUT)
        self.student_id_label.setGeometry(QtCore.QRect(10, 20, 81, 41))
        self.student_id_label.setObjectName(_fromUtf8("student_id_label"))
        self.discipline_id_label = QtGui.QLabel(ENROLL_INPUT)
        self.discipline_id_label.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.discipline_id_label.setObjectName(_fromUtf8("discipline_id_label"))
        self.add_btn = QtGui.QPushButton(ENROLL_INPUT)
        self.add_btn.setGeometry(QtCore.QRect(110, 110, 151, 51))
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.student_id_line = QtGui.QLineEdit(ENROLL_INPUT)
        self.student_id_line.setGeometry(QtCore.QRect(80, 20, 281, 31))
        self.student_id_line.setObjectName(_fromUtf8("student_id_line"))
        self.discipline_id_line = QtGui.QLineEdit(ENROLL_INPUT)
        self.discipline_id_line.setGeometry(QtCore.QRect(80, 60, 281, 31))
        self.discipline_id_line.setObjectName(_fromUtf8("discipline_id_line"))

        self.retranslateUi(ENROLL_INPUT)
        QtCore.QMetaObject.connectSlotsByName(ENROLL_INPUT)

    def retranslateUi(self, ENROLL_INPUT):
        ENROLL_INPUT.setWindowTitle(_translate("ENROLL_INPUT", "Enroll Student", None))
        self.student_id_label.setText(_translate("ENROLL_INPUT", "Student ID:", None))
        self.discipline_id_label.setText(_translate("ENROLL_INPUT", "Discipline ID:", None))
        self.add_btn.setText(_translate("ENROLL_INPUT", "Enroll student", None))
        self.add_btn.clicked.connect(self.enroll_student)
    @errorProne    
    def enroll_student(self):
        student_id = int(self.student_id_line.text())
        discipline_id = int(self.discipline_id_line.text())
        
        self.__enroll_controller.enroll_student(student_id, discipline_id)
        self.__undo_redo_controller.memorise()
        
class Ui_SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT(QtGui.QWidget):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT):
        SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT.setObjectName(_fromUtf8("SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT"))
        SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT.resize(376, 222)
        self.le_button = QtGui.QPushButton(SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT)
        self.le_button.setGeometry(QtCore.QRect(90, 120, 171, 61))
        self.le_button.setObjectName(_fromUtf8("le_button"))
        self.id_line = QtGui.QLineEdit(SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT)
        self.id_line.setGeometry(QtCore.QRect(110, 40, 241, 31))
        self.id_line.setObjectName(_fromUtf8("id_line"))
        self.label = QtGui.QLabel(SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.retranslateUi(SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT)
        QtCore.QMetaObject.connectSlotsByName(SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT)

    def retranslateUi(self, SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT):
        SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT.setWindowTitle(_translate("SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT", "Show enrolled students for discipline id", None))
        self.le_button.setText(_translate("SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT", "SHOW", None))
        self.label.setText(_translate("SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT", "Discipline ID:", None))
        self.le_button.clicked.connect(self.show_enrolled_students_for_discipline)
    
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
        
    @errorProne    
    def show_enrolled_students_for_discipline(self):
        ex.listView.clear()
        discipline_id = int(self.id_line.text())
        res = self.__enroll_controller.get_enrolled_students_for_discipline(discipline_id)
        if len(res) == 0:
            ex.listView.addItem("Currently there are no students enrolled for {0}".format(self.__get_discipline(discipline_id)))
        else:
            for student_id in res:
                ex.listView.addItem("id {0}: {1}".format(student_id, self.__get_student(student_id)))
                
class Ui_SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT(QtGui.QWidget):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT):
        SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT.setObjectName(_fromUtf8("SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT"))
        SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT.resize(376, 222)
        self.le_button = QtGui.QPushButton(SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT)
        self.le_button.setGeometry(QtCore.QRect(90, 120, 171, 61))
        self.le_button.setObjectName(_fromUtf8("le_button"))
        self.id_line = QtGui.QLineEdit(SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT)
        self.id_line.setGeometry(QtCore.QRect(110, 40, 241, 31))
        self.id_line.setObjectName(_fromUtf8("id_line"))
        self.label = QtGui.QLabel(SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT)
        QtCore.QMetaObject.connectSlotsByName(SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT)

    def retranslateUi(self, SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT):
        SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT.setWindowTitle(_translate("SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT", "Show enrolled disciplines for student id", None))
        self.le_button.setText(_translate("SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT", "SHOW", None))
        self.label.setText(_translate("SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT", "Student ID:", None))
        self.le_button.clicked.connect(self.show_enrolled_disciplines_for_student)
        
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
    @errorProne    
    def show_enrolled_disciplines_for_student(self):
        ex.listView.clear()
        student_id = int(self.id_line.text())
        res = self.__enroll_controller.get_enrolled_disciplines_for_student(student_id)
        if len(res) == 0:
            ex.listView.addItem("currently {0} is not enrolled for any discipline".format(self.__get_student(student_id)))
        else:
            for discipline_id in res:
                ex.listView.addItem(self.__get_discipline(discipline_id))
        
class Ui_ENRROLL_MENU(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, ENRROLL_MENU):
        ENRROLL_MENU.setObjectName(_fromUtf8("ENRROLL_MENU"))
        ENRROLL_MENU.resize(499, 85)
        self.horizontalLayout = QtGui.QHBoxLayout(ENRROLL_MENU)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.enroll_student_btn = QtGui.QPushButton(ENRROLL_MENU)
        self.enroll_student_btn.setObjectName(_fromUtf8("enroll_student_btn"))
        self.horizontalLayout.addWidget(self.enroll_student_btn)
        self.enroll_discipline_btn = QtGui.QPushButton(ENRROLL_MENU)
        self.enroll_discipline_btn.setObjectName(_fromUtf8("enroll_discipline_btn"))
        self.horizontalLayout.addWidget(self.enroll_discipline_btn)
        self.enroll_grade_btn = QtGui.QPushButton(ENRROLL_MENU)
        self.enroll_grade_btn.setObjectName(_fromUtf8("enroll_grade_btn"))
        self.horizontalLayout.addWidget(self.enroll_grade_btn)

        self.retranslateUi(ENRROLL_MENU)
        QtCore.QMetaObject.connectSlotsByName(ENRROLL_MENU)

    def retranslateUi(self, ENRROLL_MENU):
        ENRROLL_MENU.setWindowTitle(_translate("ENRROLL_MENU", "Enroll Menu", None))
        self.enroll_student_btn.setText(_translate("ENRROLL_MENU", "ENRROLL student", None))
        self.enroll_discipline_btn.setText(_translate("ENRROLL_MENU", "SHOW enrolled students for discipline", None))
        self.enroll_grade_btn.setText(_translate("ENRROLL_MENU", "SHOW enrolled disciplines for student", None))
        self.enroll_student_btn.clicked.connect(self.enroll_input)
        self.enroll_discipline_btn.clicked.connect(self.show_enrolled_students_for_discipline_input)
        self.enroll_grade_btn.clicked.connect(self.show_enrolled_disciplines_for_student_input)
        
    def enroll_input(self):
        global enroll_input
        enroll_input = Ui_ENROLL_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        enroll_input.show() 
    
    def show_enrolled_students_for_discipline_input(self):
        global show_enrolled_students_for_discipline_input
        show_enrolled_students_for_discipline_input = Ui_SHOW_ENROLLED_STUDENTS_FOR_DISCIPLINE_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        show_enrolled_students_for_discipline_input.show() 
    
    def show_enrolled_disciplines_for_student_input(self):
        global show_enrolled_disciplines_for_student_input
        show_enrolled_disciplines_for_student_input = Ui_SHOW_ENROLLED_DISCIPLINES_FOR_STUDENT_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        show_enrolled_disciplines_for_student_input.show() 

class Ui_REMOVE_STUDENT_INPUT(QtGui.QWidget):
    
     
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
        
    def setupUi(self, REMOVE_STUDENT_INPUT):
        REMOVE_STUDENT_INPUT.setObjectName(_fromUtf8("REMOVE_STUDENT_INPUT"))
        REMOVE_STUDENT_INPUT.resize(376, 222)
        self.le_button = QtGui.QPushButton(REMOVE_STUDENT_INPUT)
        self.le_button.setGeometry(QtCore.QRect(90, 120, 171, 61))
        self.le_button.setObjectName(_fromUtf8("le_button"))
        self.id_line = QtGui.QLineEdit(REMOVE_STUDENT_INPUT)
        self.id_line.setGeometry(QtCore.QRect(110, 40, 241, 31))
        self.id_line.setObjectName(_fromUtf8("id_line"))
        self.label = QtGui.QLabel(REMOVE_STUDENT_INPUT)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(REMOVE_STUDENT_INPUT)
        QtCore.QMetaObject.connectSlotsByName(REMOVE_STUDENT_INPUT)

    def retranslateUi(self, REMOVE_STUDENT_INPUT):
        REMOVE_STUDENT_INPUT.setWindowTitle(_translate("REMOVE_STUDENT_INPUT", "Remove student", None))
        self.le_button.setText(_translate("REMOVE_STUDENT_INPUT", "REMOVE", None))
        self.label.setText(_translate("REMOVE_STUDENT_INPUT", "Student ID:", None))
        self.le_button.clicked.connect(self.remove_student)
    @errorProne    
    def remove_student(self):
        student_id = int(self.id_line.text())
        self.__student_controller.remove_by_id(student_id)
        self.__grade_controller.remove_by_student_id(student_id)
        self.__enroll_controller.disenroll_student_all(student_id)
        self.__undo_redo_controller.memorise()

class Ui_REMOVE_DISCIPLINE_INPUT(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, REMOVE_DISCIPLINE_INPUT):
        REMOVE_DISCIPLINE_INPUT.setObjectName(_fromUtf8("REMOVE_DISCIPLINE_INPUT"))
        REMOVE_DISCIPLINE_INPUT.resize(376, 222)
        self.le_button = QtGui.QPushButton(REMOVE_DISCIPLINE_INPUT)
        self.le_button.setGeometry(QtCore.QRect(90, 120, 171, 61))
        self.le_button.setObjectName(_fromUtf8("le_button"))
        self.id_line = QtGui.QLineEdit(REMOVE_DISCIPLINE_INPUT)
        self.id_line.setGeometry(QtCore.QRect(110, 40, 241, 31))
        self.id_line.setObjectName(_fromUtf8("id_line"))
        self.label = QtGui.QLabel(REMOVE_DISCIPLINE_INPUT)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(REMOVE_DISCIPLINE_INPUT)
        QtCore.QMetaObject.connectSlotsByName(REMOVE_DISCIPLINE_INPUT)

    def retranslateUi(self, REMOVE_DISCIPLINE_INPUT):
        REMOVE_DISCIPLINE_INPUT.setWindowTitle(_translate("REMOVE_DISCIPLINE_INPUT", "Remove discipline", None))
        self.le_button.setText(_translate("REMOVE_DISCIPLINE_INPUT", "REMOVE", None))
        self.label.setText(_translate("REMOVE_DISCIPLINE_INPUT", "Discipline ID:", None))
        self.le_button.clicked.connect(self.remove_discipline)
    @errorProne
    def remove_discipline(self):
        discipline_id = int(self.id_line.text())
        self.__discipline_controller.remove_by_id(discipline_id)
        self.__grade_controller.remove_by_discipline_id(discipline_id)
        self.__enroll_controller.disenroll_discipline_all(discipline_id)
        self.__undo_redo_controller.memorise()
    
class Ui_REMOVE_GRADE_INPUT(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, REMOVE_GRADE_INPUT):
        REMOVE_GRADE_INPUT.setObjectName(_fromUtf8("REMOVE_GRADE_INPUT"))
        REMOVE_GRADE_INPUT.resize(291, 260)
        self.student_label = QtGui.QLabel(REMOVE_GRADE_INPUT)
        self.student_label.setGeometry(QtCore.QRect(30, 50, 71, 21))
        self.student_label.setObjectName(_fromUtf8("student_label"))
        self.label_2 = QtGui.QLabel(REMOVE_GRADE_INPUT)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 61, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(REMOVE_GRADE_INPUT)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 71, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.student_line = QtGui.QLineEdit(REMOVE_GRADE_INPUT)
        self.student_line.setGeometry(QtCore.QRect(110, 49, 161, 21))
        self.student_line.setObjectName(_fromUtf8("student_line"))
        self.discipline_line = QtGui.QLineEdit(REMOVE_GRADE_INPUT)
        self.discipline_line.setGeometry(QtCore.QRect(110, 80, 161, 20))
        self.discipline_line.setObjectName(_fromUtf8("discipline_line"))
        self.grade_line = QtGui.QLineEdit(REMOVE_GRADE_INPUT)
        self.grade_line.setGeometry(QtCore.QRect(110, 110, 161, 20))
        self.grade_line.setObjectName(_fromUtf8("grade_line"))
        self.le_button = QtGui.QPushButton(REMOVE_GRADE_INPUT)
        self.le_button.setGeometry(QtCore.QRect(70, 170, 141, 61))
        self.le_button.setObjectName(_fromUtf8("le_button"))

        self.retranslateUi(REMOVE_GRADE_INPUT)
        QtCore.QMetaObject.connectSlotsByName(REMOVE_GRADE_INPUT)

    def retranslateUi(self, REMOVE_GRADE_INPUT):
        REMOVE_GRADE_INPUT.setWindowTitle(_translate("REMOVE_GRADE_INPUT", "Remove grade", None))
        self.student_label.setText(_translate("REMOVE_GRADE_INPUT", "Student ID:", None))
        self.label_2.setText(_translate("REMOVE_GRADE_INPUT", "Discipline ID:", None))
        self.label_3.setText(_translate("REMOVE_GRADE_INPUT", "Grade Value:", None))
        self.le_button.setText(_translate("REMOVE_GRADE_INPUT", "REMOVE", None))
        self.le_button.clicked.connect(self.remove_grade)
    @errorProne    
    def remove_grade(self):
        student_id = int(self.student_line.text())
        discipline_id = int(self.discipline_line.text())
        grade_value  = int(self.grade_line.text())
        self.__grade_controller.remove(student_id, discipline_id, grade_value)
        self.__undo_redo_controller.memorise()
        
class Ui_REMOVE_MENU(QtGui.QWidget):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, REMOVE_MENU):
        REMOVE_MENU.setObjectName(_fromUtf8("REMOVE_MENU"))
        REMOVE_MENU.resize(573, 150)
        self.gridLayout = QtGui.QGridLayout(REMOVE_MENU)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.warning = QtGui.QLabel(REMOVE_MENU)
        self.warning.setObjectName(_fromUtf8("warning"))
        self.gridLayout.addWidget(self.warning, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.remove_student_btn = QtGui.QPushButton(REMOVE_MENU)
        self.remove_student_btn.setObjectName(_fromUtf8("remove_student_btn"))
        self.horizontalLayout.addWidget(self.remove_student_btn)
        self.remove_discipline_btn = QtGui.QPushButton(REMOVE_MENU)
        self.remove_discipline_btn.setObjectName(_fromUtf8("remove_discipline_btn"))
        self.horizontalLayout.addWidget(self.remove_discipline_btn)
        self.remove_grad_btn = QtGui.QPushButton(REMOVE_MENU)
        self.remove_grad_btn.setObjectName(_fromUtf8("remove_grad_btn"))
        self.horizontalLayout.addWidget(self.remove_grad_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(REMOVE_MENU)
        QtCore.QMetaObject.connectSlotsByName(REMOVE_MENU)

    def retranslateUi(self, REMOVE_MENU):
        REMOVE_MENU.setWindowTitle(_translate("REMOVE_MENU", "Remove Menu", None))
        self.warning.setText(_translate("REMOVE_MENU", "NOTE! If you remove a student or a discipline, all their corresponding data are lost !", None))
        self.remove_student_btn.setText(_translate("REMOVE_MENU", "REMOVE student", None))
        self.remove_discipline_btn.setText(_translate("REMOVE_MENU", "REMOVE discipline", None))
        self.remove_grad_btn.setText(_translate("REMOVE_MENU", "REMOVE grade", None))
        self.remove_student_btn.clicked.connect(self.remove_student_input)
        self.remove_discipline_btn.clicked.connect(self.remove_discipline_input)
        self.remove_grad_btn.clicked.connect(self.remove_grade_input)
        
        
    def remove_student_input(self):
        global remove_student_input
        remove_student_input = Ui_REMOVE_STUDENT_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        remove_student_input.show()   
    
    def remove_discipline_input(self):
        global remove_discipline_input
        remove_discipline_input = Ui_REMOVE_DISCIPLINE_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        remove_discipline_input.show()  
    
    def remove_grade_input(self):
        global remove_grade_input
        remove_grade_input = Ui_REMOVE_GRADE_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        remove_grade_input.show()  
    
class Ui_list_grades_for_student_input(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, list_grades_for_student_input):
        list_grades_for_student_input.setObjectName(_fromUtf8("list_grades_for_student_input"))
        list_grades_for_student_input.resize(376, 222)
        self.le_button = QtGui.QPushButton(list_grades_for_student_input)
        self.le_button.setGeometry(QtCore.QRect(90, 120, 171, 61))
        self.le_button.setObjectName(_fromUtf8("le_button"))
        self.id_line = QtGui.QLineEdit(list_grades_for_student_input)
        self.id_line.setGeometry(QtCore.QRect(110, 40, 241, 31))
        self.id_line.setObjectName(_fromUtf8("id_line"))
        self.label = QtGui.QLabel(list_grades_for_student_input)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(list_grades_for_student_input)
        QtCore.QMetaObject.connectSlotsByName(list_grades_for_student_input)

    def retranslateUi(self, list_grades_for_student_input):
        list_grades_for_student_input.setWindowTitle(_translate("list_grades_for_student_input", "List all grades of a student", None))
        self.le_button.setText(_translate("list_grades_for_student_input", "LIST", None))
        self.label.setText(_translate("list_grades_for_student_input", "Student ID:", None))
        self.le_button.clicked.connect(self.list_grades_student)
        
    
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
        
    @errorProne    
    def list_grades_student(self):
        ex.listView.clear()
        student_id = int(self.id_line.text())
        portfolio = self.__grade_controller.get_grades_for_student(student_id)
        if len(portfolio) == 0:
            ex.listView.addItem("{student} has not received yet any grades".format(student = self.__get_student(student_id)))
            return
        ex.listView.addItem('{0}'.format(self.__get_student(student_id)))
        for discipline_id in portfolio:
            ex.listView.addItem("        {discipline}: {grades}".format(discipline = self.__get_discipline(discipline_id),grades = portfolio[discipline_id]))
             
class Ui_list_grades_for_discipline_input(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, list_grades_for_discipline_input):
        list_grades_for_discipline_input.setObjectName(_fromUtf8("list_grades_for_discipline_input"))
        list_grades_for_discipline_input.resize(376, 222)
        self.le_button = QtGui.QPushButton(list_grades_for_discipline_input)
        self.le_button.setGeometry(QtCore.QRect(90, 120, 171, 61))
        self.le_button.setObjectName(_fromUtf8("le_button"))
        self.id_line = QtGui.QLineEdit(list_grades_for_discipline_input)
        self.id_line.setGeometry(QtCore.QRect(110, 40, 241, 31))
        self.id_line.setObjectName(_fromUtf8("id_line"))
        self.label = QtGui.QLabel(list_grades_for_discipline_input)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(list_grades_for_discipline_input)
        QtCore.QMetaObject.connectSlotsByName(list_grades_for_discipline_input)

    def retranslateUi(self, list_grades_for_discipline_input):
        list_grades_for_discipline_input.setWindowTitle(_translate("list_grades_for_discipline_input", "List all grades for a discipline", None))
        self.le_button.setText(_translate("list_grades_for_discipline_input", "LIST", None))
        self.label.setText(_translate("list_grades_for_discipline_input", "Discipline ID:", None))
        self.le_button.clicked.connect(self.list_grades_for_disciplines)
        
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
        
    @errorProne    
    def list_grades_for_disciplines(self):
        ex.listView.clear()
        discipline_id = int(self.id_line.text())
        portfolio = self.__grade_controller.get_grades_for_discipline(discipline_id)
        if len(portfolio) == 0:
            ex.listView.addItem("No student has yet received any grade at {discipline}".format(discipline = self.__get_discipline(discipline_id)))
            return
        ex.listView.addItem("{0}".format(self.__get_discipline(discipline_id)))
        for student_id in portfolio:
            ex.listView.addItem("        {student}: {grades}".format(student = self.__get_student(student_id), grades = portfolio[student_id]))
        
class Ui_LIST_MENU(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(569, 166)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.list_students_btn = QtGui.QPushButton(Form)
        self.list_students_btn.setObjectName(_fromUtf8("list_students_btn"))
        self.gridLayout.addWidget(self.list_students_btn, 0, 0, 1, 1)
        self.list_all_grades_btn = QtGui.QPushButton(Form)
        self.list_all_grades_btn.setObjectName(_fromUtf8("list_all_grades_btn"))
        self.gridLayout.addWidget(self.list_all_grades_btn, 1, 0, 1, 1)
        self.list_grades_student_btn = QtGui.QPushButton(Form)
        self.list_grades_student_btn.setObjectName(_fromUtf8("list_grades_student_btn"))
        self.gridLayout.addWidget(self.list_grades_student_btn, 1, 1, 1, 1)
        self.list_grades_discipline_btn = QtGui.QPushButton(Form)
        self.list_grades_discipline_btn.setObjectName(_fromUtf8("list_grades_discipline_btn"))
        self.gridLayout.addWidget(self.list_grades_discipline_btn, 1, 2, 1, 1)
        self.list_disciplines_btn = QtGui.QPushButton(Form)
        self.list_disciplines_btn.setObjectName(_fromUtf8("list_disciplines_btn"))
        self.gridLayout.addWidget(self.list_disciplines_btn, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "List menu", None))
        self.list_students_btn.setText(_translate("Form", "LIST all students", None))
        self.list_all_grades_btn.setText(_translate("Form", "LIST all grades for all students", None))
        self.list_grades_student_btn.setText(_translate("Form", "LIST all grades for a given student", None))
        self.list_grades_discipline_btn.setText(_translate("Form", "LIST all grades for a given discipline", None))
        self.list_disciplines_btn.setText(_translate("Form", "LIST disciplines", None))
        self.list_students_btn.clicked.connect(self.list_students)
        self.list_disciplines_btn.clicked.connect(self.list_disciplines) 
        self.list_grades_student_btn.clicked.connect(self.list_grades_student_input)
        self.list_grades_discipline_btn.clicked.connect(self.list_grades_discipline_input)
        self.list_all_grades_btn.clicked.connect(self.list_grades_all)
    
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
    @errorProne    
    def list_grades_all(self):
        ex.listView.clear()
        printed = False
        for student in self.__student_controller.get_all():
            student_id = student.entity_id
            portfolio = self.__grade_controller.get_grades_for_student(student_id)
            if len(portfolio) == 0:
                continue
            printed = True
            ex.listView.addItem("id {id}: {student}".format(id = student_id, student = self.__get_student(student_id)))
            for discipline_id in portfolio:
                ex.listView.addItem("        {discipline}: {grades}".format(discipline = self.__get_discipline(discipline_id),grades = portfolio[discipline_id]))
        if not printed:
            ex.listView.addItem("Currently no-one has received any grades")
    @errorProne
    def list_students(self):
        ex.listView.clear()
        student_list = self.__student_controller.get_all()
        if len(student_list) == 0:
            ex.listView.addItem("Currently there are no students.")
        else:
            for student in student_list:
                ex.listView.addItem('id {id}: {student}'.format(id = student.entity_id, student = student.name))
    @errorProne
    def list_disciplines(self):
        ex.listView.clear()
        discipline_list = self.__discipline_controller.get_all()
        if len(discipline_list) == 0:
            ex.listView.addItem("Currently there are no students.")
        else:
            for discipline in discipline_list:
                ex.listView.addItem('id {id}: {discipline}'.format(id = discipline.entity_id, discipline = discipline.name))
    
    
    def list_grades_student_input(self):
        global grades_student_input
        grades_student_input = Ui_list_grades_for_student_input(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        grades_student_input.show() 
    
    def list_grades_discipline_input(self):
        global grades_discipline_input
        grades_discipline_input = Ui_list_grades_for_discipline_input(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        grades_discipline_input.show() 
     
class Ui_ADD_MENU(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, ADD_MENU):
        ADD_MENU.setObjectName(_fromUtf8("ADD_MENU"))
        ADD_MENU.resize(499, 85)
        self.horizontalLayout = QtGui.QHBoxLayout(ADD_MENU)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.add_student_btn = QtGui.QPushButton(ADD_MENU)
        self.add_student_btn.setObjectName(_fromUtf8("add_student_btn"))
        self.horizontalLayout.addWidget(self.add_student_btn)
        self.add_discipline_btn = QtGui.QPushButton(ADD_MENU)
        self.add_discipline_btn.setObjectName(_fromUtf8("add_discipline_btn"))
        self.horizontalLayout.addWidget(self.add_discipline_btn)
        self.add_grade_btn = QtGui.QPushButton(ADD_MENU)
        self.add_grade_btn.setObjectName(_fromUtf8("add_grade_btn"))
        self.horizontalLayout.addWidget(self.add_grade_btn)

        self.retranslateUi(ADD_MENU)
        QtCore.QMetaObject.connectSlotsByName(ADD_MENU)

    def retranslateUi(self, ADD_MENU):
        ADD_MENU.setWindowTitle(_translate("ADD_MENU", "Add Menu", None))
        self.add_student_btn.setText(_translate("ADD_MENU", "ADD student", None))
        self.add_discipline_btn.setText(_translate("ADD_MENU", "ADD discipline", None))
        self.add_grade_btn.setText(_translate("ADD_MENU", "ADD grade ", None))
        self.add_student_btn.clicked.connect(self.call_add_student_input)
        self.add_discipline_btn.clicked.connect(self.call_add_discipline_input)
        self.add_grade_btn.clicked.connect(self.call_add_grade_input)
        
    def call_add_student_input(self):
        global add_student_input
        add_student_input = Ui_STUDENT_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        add_student_input.show() 
        
    def call_add_discipline_input(self):
        global add_discipline_input
        add_discipline_input = Ui_DISCIPLINE_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        add_discipline_input.show() 
        
    def call_add_grade_input(self):
        global add_grade_input
        add_grade_input = Ui_GRADE_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        add_grade_input.show() 
        
class Ui_UPDATE_STUDENT_INPUT(QtGui.QWidget):
    
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, STUDENT_INPUT):
        STUDENT_INPUT.setObjectName(_fromUtf8("STUDENT_INPUT"))
        STUDENT_INPUT.resize(388, 170)
        self.id_label = QtGui.QLabel(STUDENT_INPUT)
        self.id_label.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.id_label.setObjectName(_fromUtf8("id_label"))
        self.name_label = QtGui.QLabel(STUDENT_INPUT)
        self.name_label.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.add_btn = QtGui.QPushButton(STUDENT_INPUT)
        self.add_btn.setGeometry(QtCore.QRect(110, 100, 151, 51))
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.id_input_line = QtGui.QLineEdit(STUDENT_INPUT)
        self.id_input_line.setGeometry(QtCore.QRect(50, 19, 311, 31))
        self.id_input_line.setObjectName(_fromUtf8("id_input_line"))
        self.name_input_line = QtGui.QLineEdit(STUDENT_INPUT)
        self.name_input_line.setGeometry(QtCore.QRect(50, 60, 311, 31))
        self.name_input_line.setObjectName(_fromUtf8("name_input_line"))

        self.retranslateUi(STUDENT_INPUT)
        QtCore.QMetaObject.connectSlotsByName(STUDENT_INPUT)

    def retranslateUi(self, STUDENT_INPUT):
        STUDENT_INPUT.setWindowTitle(_translate("STUDENT_INPUT", "Update student", None))
        self.id_label.setText(_translate("STUDENT_INPUT", "ID:", None))
        self.name_label.setText(_translate("STUDENT_INPUT", "Name:", None))
        self.add_btn.setText(_translate("STUDENT_INPUT", "Update", None))
        self.add_btn.clicked.connect(self.update_student)
    @errorProne    
    def update_student(self):
        student_id = int(self.id_input_line.text())
        student_name = self.name_input_line.text()
        self.__student_controller.update(student_id, student_name)
        self.__undo_redo_controller.memorise()

class Ui_UPDATE_DISCIPLINE_INPUT(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, DISCIPLINE_INPUT):
        DISCIPLINE_INPUT.setObjectName(_fromUtf8("DISCIPLINE_INPUT"))
        DISCIPLINE_INPUT.resize(388, 170)
        self.id_label = QtGui.QLabel(DISCIPLINE_INPUT)
        self.id_label.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.id_label.setObjectName(_fromUtf8("id_label"))
        self.name_label = QtGui.QLabel(DISCIPLINE_INPUT)
        self.name_label.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.add_btn = QtGui.QPushButton(DISCIPLINE_INPUT)
        self.add_btn.setGeometry(QtCore.QRect(110, 100, 151, 51))
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.id_input_line = QtGui.QLineEdit(DISCIPLINE_INPUT)
        self.id_input_line.setGeometry(QtCore.QRect(50, 19, 311, 31))
        self.id_input_line.setObjectName(_fromUtf8("id_input_line"))
        self.name_input_line = QtGui.QLineEdit(DISCIPLINE_INPUT)
        self.name_input_line.setGeometry(QtCore.QRect(50, 60, 311, 31))
        self.name_input_line.setObjectName(_fromUtf8("name_input_line"))

        self.retranslateUi(DISCIPLINE_INPUT)
        QtCore.QMetaObject.connectSlotsByName(DISCIPLINE_INPUT)

    def retranslateUi(self, DISCIPLINE_INPUT):
        DISCIPLINE_INPUT.setWindowTitle(_translate("DISCIPLINE_INPUT", "Update discipline", None))
        self.id_label.setText(_translate("DISCIPLINE_INPUT", "ID:", None))
        self.name_label.setText(_translate("DISCIPLINE_INPUT", "Name:", None))
        self.add_btn.setText(_translate("DISCIPLINE_INPUT", "Update", None))
        self.add_btn.clicked.connect(self.update_discipline)
    @errorProne    
    def update_discipline(self):
        discipline_id = int(self.id_input_line.text())
        discipline_name = self.name_input_line.text()
        self.__discipline_controller.update(discipline_id, discipline_name)
        self.__undo_redo_controller.memorise()
        
class Ui_UPDATE_GRADE_INPUT(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, UPDATE_GRADE_INPUT):
        UPDATE_GRADE_INPUT.setObjectName(_fromUtf8("UPDATE_GRADE_INPUT"))
        UPDATE_GRADE_INPUT.resize(315, 290)
        self.student_label = QtGui.QLabel(UPDATE_GRADE_INPUT)
        self.student_label.setGeometry(QtCore.QRect(40, 50, 71, 21))
        self.student_label.setObjectName(_fromUtf8("student_label"))
        self.label_2 = QtGui.QLabel(UPDATE_GRADE_INPUT)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 61, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(UPDATE_GRADE_INPUT)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 81, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.student_line = QtGui.QLineEdit(UPDATE_GRADE_INPUT)
        self.student_line.setGeometry(QtCore.QRect(120, 50, 161, 21))
        self.student_line.setObjectName(_fromUtf8("student_line"))
        self.discipline_line = QtGui.QLineEdit(UPDATE_GRADE_INPUT)
        self.discipline_line.setGeometry(QtCore.QRect(120, 80, 161, 20))
        self.discipline_line.setObjectName(_fromUtf8("discipline_line"))
        self.old_line = QtGui.QLineEdit(UPDATE_GRADE_INPUT)
        self.old_line.setGeometry(QtCore.QRect(120, 120, 161, 20))
        self.old_line.setObjectName(_fromUtf8("old_line"))
        self.le_button = QtGui.QPushButton(UPDATE_GRADE_INPUT)
        self.le_button.setGeometry(QtCore.QRect(80, 200, 141, 61))
        self.le_button.setObjectName(_fromUtf8("le_button"))
        self.new_line = QtGui.QLineEdit(UPDATE_GRADE_INPUT)
        self.new_line.setGeometry(QtCore.QRect(120, 150, 161, 20))
        self.new_line.setObjectName(_fromUtf8("new_line"))
        self.label_4 = QtGui.QLabel(UPDATE_GRADE_INPUT)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 91, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(UPDATE_GRADE_INPUT)
        QtCore.QMetaObject.connectSlotsByName(UPDATE_GRADE_INPUT)

    def retranslateUi(self, UPDATE_GRADE_INPUT):
        UPDATE_GRADE_INPUT.setWindowTitle(_translate("UPDATE_GRADE_INPUT", "Update grade", None))
        self.student_label.setText(_translate("UPDATE_GRADE_INPUT", "Student ID:", None))
        self.label_2.setText(_translate("UPDATE_GRADE_INPUT", "Discipline ID:", None))
        self.label_3.setText(_translate("UPDATE_GRADE_INPUT", "Grade old Value:", None))
        self.le_button.setText(_translate("UPDATE_GRADE_INPUT", "UPDATE", None))
        self.label_4.setText(_translate("UPDATE_GRADE_INPUT", "Grade new Value:", None))
        self.le_button.clicked.connect(self.update_grade)
    
    @errorProne    
    def update_grade(self):
        student_id = int(self.student_line.text())
        discipline_id = int(self.discipline_line.text())
        old_grade  = int(self.old_line.text())
        new_grade = int(self.new_line.text())
        self.__grade_controller.update_grade(student_id, discipline_id, old_grade, new_grade)
        self.__undo_redo_controller.memorise()

class Ui_UPDATE_MENU(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, UPDATE_MENU):
        UPDATE_MENU.setObjectName(_fromUtf8("UPDATE_MENU"))
        UPDATE_MENU.resize(499, 85)
        self.horizontalLayout = QtGui.QHBoxLayout(UPDATE_MENU)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.UPDATE_student_btn = QtGui.QPushButton(UPDATE_MENU)
        self.UPDATE_student_btn.setObjectName(_fromUtf8("UPDATE_student_btn"))
        self.horizontalLayout.addWidget(self.UPDATE_student_btn)
        self.UPDATE_discipline_btn = QtGui.QPushButton(UPDATE_MENU)
        self.UPDATE_discipline_btn.setObjectName(_fromUtf8("UPDATE_discipline_btn"))
        self.horizontalLayout.addWidget(self.UPDATE_discipline_btn)
        self.UPDATE_grade_btn = QtGui.QPushButton(UPDATE_MENU)
        self.UPDATE_grade_btn.setObjectName(_fromUtf8("UPDATE_grade_btn"))
        self.horizontalLayout.addWidget(self.UPDATE_grade_btn)

        self.retranslateUi(UPDATE_MENU)
        QtCore.QMetaObject.connectSlotsByName(UPDATE_MENU)

    def retranslateUi(self, UPDATE_MENU):
        UPDATE_MENU.setWindowTitle(_translate("UPDATE_MENU", "Update Menu", None))
        self.UPDATE_student_btn.setText(_translate("UPDATE_MENU", "UPDATE student", None))
        self.UPDATE_discipline_btn.setText(_translate("UPDATE_MENU", "UPDATE discipline", None))
        self.UPDATE_grade_btn.setText(_translate("UPDATE_MENU", "UPDATE grade ", None))
        self.UPDATE_student_btn.clicked.connect(self.call_update_student_input)
        self.UPDATE_discipline_btn.clicked.connect(self.call_update_discipline_input)
        self.UPDATE_grade_btn.clicked.connect(self.call_update_grade_input)
        
        
    def call_update_student_input(self):
        global update_student_input
        update_student_input = Ui_UPDATE_STUDENT_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        update_student_input.show() 
    
    def call_update_discipline_input(self):
        global update_discipline_input
        update_discipline_input = Ui_UPDATE_DISCIPLINE_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        update_discipline_input.show() 
    
    def call_update_grade_input(self):
        global update_grade_input
        update_grade_input = Ui_UPDATE_GRADE_INPUT(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        update_grade_input.show() 
              
class Ui_main_form(QtGui.QWidget):
    
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, main_form):
        main_form.setObjectName(_fromUtf8("main_form"))
        main_form.resize(758, 567)
        self.verticalLayout = QtGui.QVBoxLayout(main_form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.ubb_logo = QtGui.QLabel(main_form)
        self.ubb_logo.setPixmap(QtGui.QPixmap(_fromUtf8("../../data/logo_ubb_albastru.png")))
        self.ubb_logo.setObjectName(_fromUtf8("ubb_logo"))
        
        self.verticalLayout.addWidget(self.ubb_logo)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.add_menu_btn = QtGui.QPushButton(main_form)
        self.add_menu_btn.setObjectName(_fromUtf8("add_menu_btn"))
        self.verticalLayout_3.addWidget(self.add_menu_btn)
        self.enroll_menu_btn = QtGui.QPushButton(main_form)
        self.enroll_menu_btn.setObjectName(_fromUtf8("enroll_menu_btn"))
        self.verticalLayout_3.addWidget(self.enroll_menu_btn)
        self.remove_menu_btn = QtGui.QPushButton(main_form)
        self.remove_menu_btn.setObjectName(_fromUtf8("remove_menu_btn"))
        self.verticalLayout_3.addWidget(self.remove_menu_btn)
        self.update_menu_btn = QtGui.QPushButton(main_form)
        self.update_menu_btn.setObjectName(_fromUtf8("update_menu_btn"))
        self.verticalLayout_3.addWidget(self.update_menu_btn)
        self.list_menu_btn = QtGui.QPushButton(main_form)
        self.list_menu_btn.setObjectName(_fromUtf8("list_menu_btn"))
        self.verticalLayout_3.addWidget(self.list_menu_btn)
        self.statistics_menu_btn = QtGui.QPushButton(main_form)
        self.statistics_menu_btn.setObjectName(_fromUtf8("statistics_menu_btn"))
        self.verticalLayout_3.addWidget(self.statistics_menu_btn)
        self.search_menu_btn = QtGui.QPushButton(main_form)
        self.search_menu_btn.setObjectName(_fromUtf8("search_menu_btn"))
        self.verticalLayout_3.addWidget(self.search_menu_btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.redo_btn = QtGui.QPushButton(main_form)
        self.redo_btn.setObjectName(_fromUtf8("redo_btn"))
        self.verticalLayout_3.addWidget(self.redo_btn)
        self.gridLayout.addLayout(self.verticalLayout_3, 5, 2, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label = QtGui.QLabel(main_form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 5, 1, 1)
        self.listView = QtGui.QListWidget(main_form)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 5, 5, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtGui.QLabel(main_form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 5, 1, 1)
        self.undo_btn = QtGui.QPushButton(main_form)
        self.undo_btn.setObjectName(_fromUtf8("undo_btn"))
        self.gridLayout.addWidget(self.undo_btn, 6, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(main_form)
        QtCore.QMetaObject.connectSlotsByName(main_form)

    def retranslateUi(self, main_form):
        main_form.setWindowTitle(_translate("main_form", "Faculty Database version 1.1.0", None))
        self.add_menu_btn.setText(_translate("main_form", "Add Menu", None))
        self.enroll_menu_btn.setText(_translate("main_form", "Enroll Menu", None))
        self.remove_menu_btn.setText(_translate("main_form", "Remove Menu", None))
        self.update_menu_btn.setText(_translate("main_form", "Update Menu", None))
        self.list_menu_btn.setText(_translate("main_form", "List Menu", None))
        self.statistics_menu_btn.setText(_translate("main_form", "Statistics Menu", None))
        self.search_menu_btn.setText(_translate("main_form", "Search Menu", None))
        self.redo_btn.setText(_translate("main_form", "Redo", None))
        self.label.setText(_translate("main_form", "@Created by George Vele - 2016", None))
        self.label_2.setText(_translate("main_form", "Faculty Database version 1.1.0", None))
        self.undo_btn.setText(_translate("main_form", "Undo", None))
        self.add_menu_btn.clicked.connect(self.call_add_menu)
        self.list_menu_btn.clicked.connect(self.call_list_menu)
        self.remove_menu_btn.clicked.connect(self.call_remove_menu)
        self.update_menu_btn.clicked.connect(self.call_update_menu)
        self.enroll_menu_btn.clicked.connect(self.call_enroll_menu)
        self.search_menu_btn.clicked.connect(self.call_search_menu)
        self.statistics_menu_btn.clicked.connect(self.call_statistics_menu)
        self.undo_btn.clicked.connect(self.undo)
        self.redo_btn.clicked.connect(self.redo)
        
        
    def call_add_menu(self):
        global add_menu
        add_menu = Ui_ADD_MENU(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        add_menu.show() 
        
    def call_list_menu(self):
        global list_menu
        list_menu = Ui_LIST_MENU(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        list_menu.show() 
        
    def call_remove_menu(self):
        global remove_menu
        remove_menu = Ui_REMOVE_MENU(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        remove_menu.show() 
        
    def call_enroll_menu(self):
        global enroll_menu
        enroll_menu = Ui_ENRROLL_MENU(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        enroll_menu.show() 
    
    def call_statistics_menu(self):
        global statistic_menu
        statistic_menu = Ui_STATISTICS_MENU(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        statistic_menu.show() 
     

    def call_search_menu(self):
        global search_menu
        search_menu = Ui_SEARCH_MENU(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        search_menu.show() 
     
    
    def call_update_menu(self):
        global update_menu
        update_menu = Ui_UPDATE_MENU(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        update_menu.show() 
    @errorProne   
    def undo(self):
        self.__undo_redo_controller.undo()
    @errorProne   
    def redo(self):
        self.__undo_redo_controller.redo()

    def popup_exception(self, message):
        global popup
        popup = PopupMessage(message)
        popup.show()

class PopupMessage(QtGui.QWidget):
    
    def __init__(self,message):
        QtGui.QWidget.__init__(self) 
        self.message = message
        self.setupUi(self) 
         
        
    def setupUi(self, Popup):
        Popup.setObjectName(_fromUtf8("Popup"))
        Popup.resize(300, 150)
        self.gridLayout = QtGui.QGridLayout(Popup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.error_lb = QtGui.QLabel(Popup)
        self.error_lb.setObjectName(_fromUtf8("error_lb"))
        self.gridLayout.addWidget(self.error_lb, 1, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.image = QtGui.QLabel(Popup)
        self.image.setText(_fromUtf8(""))
        self.image.setPixmap(QtGui.QPixmap(_fromUtf8("../../data/error-icon-3.png")))
        self.image.setObjectName(_fromUtf8("image"))
        self.gridLayout.addWidget(self.image, 0, 1, 1, 1)

        self.retranslateUi(Popup)
        QtCore.QMetaObject.connectSlotsByName(Popup)

    def retranslateUi(self, Popup):
        Popup.setWindowTitle(_translate("Popup", "oops, something went wrong", None))
        self.error_lb.setText(_translate("Popup", Popup.message, None))


class GUIConsole(object):
    def __init__(self, student_controller, grade_controller, discipline_controller, enroll_controller, undo_redo_controller):
        self.__student_controller  = student_controller 
        self.__grade_controller = grade_controller 
        self.__discipline_controller = discipline_controller 
        self.__enroll_controller = enroll_controller
        self.__undo_redo_controller = undo_redo_controller
        
    def run_console(self):
        app = QtGui.QApplication(sys.argv)
        global ex
        ex = Ui_main_form(self.__student_controller, self.__grade_controller, self.__discipline_controller, self.__enroll_controller, self.__undo_redo_controller)
        ex.show()
        sys.exit(app.exec_())


