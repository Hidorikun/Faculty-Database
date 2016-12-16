# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grade_update.ui'
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

class Ui_REMOVE_GRADE_INPUT(object):
    def setupUi(self, REMOVE_GRADE_INPUT):
        REMOVE_GRADE_INPUT.setObjectName(_fromUtf8("REMOVE_GRADE_INPUT"))
        REMOVE_GRADE_INPUT.resize(315, 290)
        self.student_label = QtGui.QLabel(REMOVE_GRADE_INPUT)
        self.student_label.setGeometry(QtCore.QRect(40, 50, 71, 21))
        self.student_label.setObjectName(_fromUtf8("student_label"))
        self.label_2 = QtGui.QLabel(REMOVE_GRADE_INPUT)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 61, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(REMOVE_GRADE_INPUT)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 81, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.student_line = QtGui.QLineEdit(REMOVE_GRADE_INPUT)
        self.student_line.setGeometry(QtCore.QRect(120, 50, 161, 21))
        self.student_line.setObjectName(_fromUtf8("student_line"))
        self.discipline_line = QtGui.QLineEdit(REMOVE_GRADE_INPUT)
        self.discipline_line.setGeometry(QtCore.QRect(120, 80, 161, 20))
        self.discipline_line.setObjectName(_fromUtf8("discipline_line"))
        self.old_line = QtGui.QLineEdit(REMOVE_GRADE_INPUT)
        self.old_line.setGeometry(QtCore.QRect(120, 120, 161, 20))
        self.old_line.setObjectName(_fromUtf8("old_line"))
        self.le_button = QtGui.QPushButton(REMOVE_GRADE_INPUT)
        self.le_button.setGeometry(QtCore.QRect(80, 200, 141, 61))
        self.le_button.setObjectName(_fromUtf8("le_button"))
        self.new_line = QtGui.QLineEdit(REMOVE_GRADE_INPUT)
        self.new_line.setGeometry(QtCore.QRect(120, 150, 161, 20))
        self.new_line.setObjectName(_fromUtf8("new_line"))
        self.label_4 = QtGui.QLabel(REMOVE_GRADE_INPUT)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 91, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(REMOVE_GRADE_INPUT)
        QtCore.QMetaObject.connectSlotsByName(REMOVE_GRADE_INPUT)

    def retranslateUi(self, REMOVE_GRADE_INPUT):
        REMOVE_GRADE_INPUT.setWindowTitle(_translate("REMOVE_GRADE_INPUT", "Form", None))
        self.student_label.setText(_translate("REMOVE_GRADE_INPUT", "Student ID:", None))
        self.label_2.setText(_translate("REMOVE_GRADE_INPUT", "Discipline ID:", None))
        self.label_3.setText(_translate("REMOVE_GRADE_INPUT", "Grade old Value:", None))
        self.le_button.setText(_translate("REMOVE_GRADE_INPUT", "UPDATE", None))
        self.label_4.setText(_translate("REMOVE_GRADE_INPUT", "Grade new Value:", None))

