# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/otakulabs/PycharmProjects/TestGround/pyqt5/form.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 240)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnMin = QtWidgets.QPushButton(Form)
        self.btnMin.setFlat(True)
        self.btnMin.setObjectName("btnMin")
        self.horizontalLayout.addWidget(self.btnMin)
        self.btnMax = QtWidgets.QPushButton(Form)
        self.btnMax.setFlat(True)
        self.btnMax.setObjectName("btnMax")
        self.horizontalLayout.addWidget(self.btnMax)
        self.btnExit = QtWidgets.QPushButton(Form)
        self.btnExit.setFlat(True)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout.addWidget(self.btnExit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inputInfo = QtWidgets.QLineEdit(Form)
        self.inputInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.inputInfo.setObjectName("inputInfo")
        self.horizontalLayout_2.addWidget(self.inputInfo)
        self.btnSubmit = QtWidgets.QPushButton(Form)
        self.btnSubmit.setFlat(True)
        self.btnSubmit.setObjectName("btnSubmit")
        self.horizontalLayout_2.addWidget(self.btnSubmit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnMin.setText(_translate("Form", "Min"))
        self.btnMax.setText(_translate("Form", "Max"))
        self.btnExit.setText(_translate("Form", "Exit"))
        self.btnSubmit.setText(_translate("Form", "Submit"))

