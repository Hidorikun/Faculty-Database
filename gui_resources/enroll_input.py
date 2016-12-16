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

class Ui_ENROLL_INPUT(object):
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
        ENROLL_INPUT.setWindowTitle(_translate("ENROLL_INPUT", "Form", None))
        self.student_id_label.setText(_translate("ENROLL_INPUT", "Student ID:", None))
        self.discipline_id_label.setText(_translate("ENROLL_INPUT", "Discipline ID:", None))
        self.add_btn.setText(_translate("ENROLL_INPUT", "Enroll student", None))

