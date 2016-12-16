# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mm.ui'
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

class Ui_main_form(object):
    def setupUi(self, main_form):
        main_form.setObjectName(_fromUtf8("main_form"))
        main_form.resize(758, 567)
        self.verticalLayout = QtGui.QVBoxLayout(main_form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ubb_logo = QtGui.QLabel(main_form)
        self.ubb_logo.setText(_fromUtf8(""))
        self.ubb_logo.setPixmap(QtGui.QPixmap(_fromUtf8("logo_ubb_albastru.png")))
        self.ubb_logo.setObjectName(_fromUtf8("ubb_logo"))
        self.verticalLayout.addWidget(self.ubb_logo)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.add_menu_btn = QtGui.QPushButton(main_form)
        self.add_menu_btn.setObjectName(_fromUtf8("add_menu_btn"))
        self.verticalLayout_3.addWidget(self.add_menu_btn)
        self.enroll_menu_btn = QtGui.QPushButton(main_form)
        self.enroll_menu_btn.setObjectName(_fromUtf8("enroll_menu_btn"))
        self.verticalLayout_3.addWidget(self.enroll_menu_btn)
        self.remove_menu_btn = QtGui.QPushButton(main_form)
        self.remove_menu_btn.setObjectName(_fromUtf8("remove_menu_btn"))
        self.verticalLayout_3.addWidget(self.remove_menu_btn)
        self.update_menu_btn = QtGui.QPushButton(main_form)
        self.update_menu_btn.setObjectName(_fromUtf8("update_menu_btn"))
        self.verticalLayout_3.addWidget(self.update_menu_btn)
        self.list_menu_btn = QtGui.QPushButton(main_form)
        self.list_menu_btn.setObjectName(_fromUtf8("list_menu_btn"))
        self.verticalLayout_3.addWidget(self.list_menu_btn)
        self.statistics_menu_btn = QtGui.QPushButton(main_form)
        self.statistics_menu_btn.setObjectName(_fromUtf8("statistics_menu_btn"))
        self.verticalLayout_3.addWidget(self.statistics_menu_btn)
        self.search_menu_btn = QtGui.QPushButton(main_form)
        self.search_menu_btn.setObjectName(_fromUtf8("search_menu_btn"))
        self.verticalLayout_3.addWidget(self.search_menu_btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.redo_btn = QtGui.QPushButton(main_form)
        self.redo_btn.setObjectName(_fromUtf8("redo_btn"))
        self.verticalLayout_3.addWidget(self.redo_btn)
        self.gridLayout.addLayout(self.verticalLayout_3, 5, 2, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label = QtGui.QLabel(main_form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 5, 1, 1)
        self.undo_btn = QtGui.QPushButton(main_form)
        self.undo_btn.setObjectName(_fromUtf8("undo_btn"))
        self.gridLayout.addWidget(self.undo_btn, 6, 2, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtGui.QLabel(main_form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 5, 1, 1)
        self.listWidget = QtGui.QListWidget(main_form)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 5, 5, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(main_form)
        QtCore.QMetaObject.connectSlotsByName(main_form)

    def retranslateUi(self, main_form):
        main_form.setWindowTitle(_translate("main_form", "Form", None))
        self.add_menu_btn.setText(_translate("main_form", "Add Menu", None))
        self.enroll_menu_btn.setText(_translate("main_form", "Enroll Menu", None))
        self.remove_menu_btn.setText(_translate("main_form", "Remove Menu", None))
        self.update_menu_btn.setText(_translate("main_form", "Update Menu", None))
        self.list_menu_btn.setText(_translate("main_form", "List Menu", None))
        self.statistics_menu_btn.setText(_translate("main_form", "Statistics Menu", None))
        self.search_menu_btn.setText(_translate("main_form", "Search Menu", None))
        self.redo_btn.setText(_translate("main_form", "Redo", None))
        self.label.setText(_translate("main_form", "@Created by George Vele - 2016", None))
        self.undo_btn.setText(_translate("main_form", "Undo", None))
        self.label_2.setText(_translate("main_form", "Information", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("main_form", "dasdf", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

