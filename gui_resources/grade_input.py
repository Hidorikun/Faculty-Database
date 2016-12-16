# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stu_inp.ui'
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

class Ui_GRADE_INPUT(object):
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
        GRADE_INPUT.setWindowTitle(_translate("GRADE_INPUT", "Form", None))
        self.id_label.setText(_translate("GRADE_INPUT", "Student ID:", None))
        self.name_label.setText(_translate("GRADE_INPUT", "Discipline ID:", None))
        self.add_btn.setText(_translate("GRADE_INPUT", "Add Grade", None))
        self.name_label_2.setText(_translate("GRADE_INPUT", "Grade value:", None))

