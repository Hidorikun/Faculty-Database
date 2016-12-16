# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'le_input.ui'
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

class Ui_REMOVE_DISCIPLINE_INPUT(object):
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
        REMOVE_DISCIPLINE_INPUT.setWindowTitle(_translate("REMOVE_DISCIPLINE_INPUT", "Form", None))
        self.le_button.setText(_translate("REMOVE_DISCIPLINE_INPUT", "REMOVE", None))
        self.label.setText(_translate("REMOVE_DISCIPLINE_INPUT", "Discipline ID:", None))

