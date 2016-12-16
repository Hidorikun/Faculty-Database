# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistic.ui'
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
        STATISTICS_MENU.resize(615, 352)
        self.gridLayout = QtGui.QGridLayout(STATISTICS_MENU)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.print_all_enrolled = QtGui.QPushButton(STATISTICS_MENU)
        self.print_all_enrolled.setObjectName(_fromUtf8("print_all_enrolled"))
        self.gridLayout.addWidget(self.print_all_enrolled, 0, 0, 1, 1)
        self.print_all_failing = QtGui.QPushButton(STATISTICS_MENU)
        self.print_all_failing.setObjectName(_fromUtf8("print_all_failing"))
        self.gridLayout.addWidget(self.print_all_failing, 1, 0, 1, 1)
        self.prin_best_students = QtGui.QPushButton(STATISTICS_MENU)
        self.prin_best_students.setObjectName(_fromUtf8("prin_best_students"))
        self.gridLayout.addWidget(self.prin_best_students, 2, 0, 1, 1)
        self.print_best_disciplines = QtGui.QPushButton(STATISTICS_MENU)
        self.print_best_disciplines.setObjectName(_fromUtf8("print_best_disciplines"))
        self.gridLayout.addWidget(self.print_best_disciplines, 3, 0, 1, 1)

        self.retranslateUi(STATISTICS_MENU)
        QtCore.QMetaObject.connectSlotsByName(STATISTICS_MENU)

    def retranslateUi(self, STATISTICS_MENU):
        STATISTICS_MENU.setWindowTitle(_translate("STATISTICS_MENU", "Form", None))
        self.print_all_enrolled.setText(_translate("STATISTICS_MENU", "PRINT all students enrolled at a given discipline, alphabetically or by descending order of average grades", None))
        self.print_all_failing.setText(_translate("STATISTICS_MENU", "PRINT all students failing at one or more discipline", None))
        self.prin_best_students.setText(_translate("STATISTICS_MENU", "PRINT students with the best school situation, sorted in descending order of their aggregated average\n"
"", None))
        self.print_best_disciplines.setText(_translate("STATISTICS_MENU", "PRINT all disciplines sorted in descending order of the average grade received by all students enrolled at that discipline.", None))

