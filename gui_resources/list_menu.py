# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_menu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
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
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.list_students_btn.setText(_translate("Form", "LIST all students", None))
        self.list_all_grades_btn.setText(_translate("Form", "LIST all grades for all students", None))
        self.list_grades_student_btn.setText(_translate("Form", "LIST all grades for a given student", None))
        self.list_grades_discipline_btn.setText(_translate("Form", "LIST all grades for a given discipline", None))
        self.list_disciplines_btn.setText(_translate("Form", "LIST disciplines", None))

