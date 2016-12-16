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

class Ui_DISCIPLINE_INPUT(object):
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
        DISCIPLINE_INPUT.setWindowTitle(_translate("DISCIPLINE_INPUT", "Form", None))
        self.id_label.setText(_translate("DISCIPLINE_INPUT", "ID:", None))
        self.name_label.setText(_translate("DISCIPLINE_INPUT", "Name:", None))
        self.add_btn.setText(_translate("DISCIPLINE_INPUT", "Add Discipline", None))

