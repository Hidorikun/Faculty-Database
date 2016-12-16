# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searching.ui'
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
        Form.resize(400, 179)
        self.by_id_btn = QtGui.QPushButton(Form)
        self.by_id_btn.setGeometry(QtCore.QRect(30, 30, 151, 111))
        self.by_id_btn.setObjectName(_fromUtf8("by_id_btn"))
        self.by_name_btn = QtGui.QPushButton(Form)
        self.by_name_btn.setGeometry(QtCore.QRect(220, 30, 161, 111))
        self.by_name_btn.setObjectName(_fromUtf8("by_name_btn"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.by_id_btn.setText(_translate("Form", "Sreach by ID", None))
        self.by_name_btn.setText(_translate("Form", "Search by name", None))

