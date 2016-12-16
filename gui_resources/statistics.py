# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics.ui'
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

class Ui_STATISTICS_MENU(object):
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
        STATISTICS_MENU.setWindowTitle(_translate("STATISTICS_MENU", "Form", None))
        self.alpha_btn.setText(_translate("STATISTICS_MENU", "PRINT all students enrolled at a given discipline, alphabetically", None))
        self.descending_btn.setText(_translate("STATISTICS_MENU", "PRINT all students enrolled at a given discipline, sorded in descending order ", None))
        self.failing_btn.setText(_translate("STATISTICS_MENU", "PRINT all studend failing at one or more disciplines", None))
        self.best_students_btn.setText(_translate("STATISTICS_MENU", "PRINT students with best situations, sorted in descending order o their aggregated avarage", None))
        self.best_disciplines.setText(_translate("STATISTICS_MENU", "PRINT all disciplines sorted in descending order of the average grade received by all enrolled students", None))

