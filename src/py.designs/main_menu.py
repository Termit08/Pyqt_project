import io
import sys
from PyQt6 import uic 
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(992, 818)
        Form.setStyleSheet("")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1011, 821))
        self.label.setStyleSheet("border-image: url(:/pictures/main_menu.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 290, 531, 101))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"font: 26pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 410, 531, 101))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 26pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(270, 140, 521, 71))
        self.label_2.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Начать игру"))
        self.pushButton_2.setText(_translate("Form", "Инструкция"))
        self.label_2.setText(_translate("Form", "ГЛАВНОЕ МЕНЮ"))


