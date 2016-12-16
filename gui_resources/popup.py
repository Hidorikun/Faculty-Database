# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
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

class Popup(object):
    def setupUi(self, Popup):
        Popup.setObjectName(_fromUtf8("Popup"))
        Popup.resize(487, 384)
        self.gridLayout = QtGui.QGridLayout(Popup)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.error_lb = QtGui.QLabel(Popup)
        self.error_lb.setObjectName(_fromUtf8("error_lb"))
        self.gridLayout.addWidget(self.error_lb, 1, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.image = QtGui.QLabel(Popup)
        self.image.setText(_fromUtf8(""))
        self.image.setPixmap(QtGui.QPixmap(_fromUtf8("../../data/error-icon-3.png")))
        self.image.setObjectName(_fromUtf8("image"))
        self.gridLayout.addWidget(self.image, 0, 1, 1, 1)

        self.retranslateUi(Popup)
        QtCore.QMetaObject.connectSlotsByName(Popup)

    def retranslateUi(self, Popup):
        Popup.setWindowTitle(_translate("Popup", "Dialog", None))
        self.error_lb.setText(_translate("Popup", "TextLabel", None))

