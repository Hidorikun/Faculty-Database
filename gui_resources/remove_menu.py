# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remove_menu.ui'
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

class Ui_REMOVE_MENU(object):
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
        REMOVE_MENU.setWindowTitle(_translate("REMOVE_MENU", "Form", None))
        self.warning.setText(_translate("REMOVE_MENU", "NOTE! If you remove a student or a discipline, all their corresponding data are lost !", None))
        self.remove_student_btn.setText(_translate("REMOVE_MENU", "REMOVE student", None))
        self.remove_discipline_btn.setText(_translate("REMOVE_MENU", "REMOVE discipline", None))
        self.remove_grad_btn.setText(_translate("REMOVE_MENU", "REMOVE grade", None))

