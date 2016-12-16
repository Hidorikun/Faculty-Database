# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_menu.ui'
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

class Ui_ADD_MENU(object):
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
        ADD_MENU.setWindowTitle(_translate("ADD_MENU", "Form", None))
        self.add_student_btn.setText(_translate("ADD_MENU", "ADD student", None))
        self.add_discipline_btn.setText(_translate("ADD_MENU", "ADD discipline", None))
        self.add_grade_btn.setText(_translate("ADD_MENU", "ADD grade ", None))

