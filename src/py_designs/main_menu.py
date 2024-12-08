from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 756)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.pixmap = QtGui.QPixmap("./data/phones/main_menu.jpg")
        if self.pixmap.isNull():
                print("Изображение не загружено!")
        self.label.resize(764, 756)
        self.label.move(0, 0)
        self.label.setPixmap(self.pixmap)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 160, 521, 71))
        self.label_2.setStyleSheet("font: 36pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.starting = QtWidgets.QPushButton(self.centralwidget)
        self.starting.setGeometry(QtCore.QRect(100, 300, 531, 101))
        self.starting.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "\n"
        "font: 26pt \"Arial\";\n"
        "border-color: rgb(0, 0, 0);\n"
        "")
        self.starting.setObjectName("starting")
        self.instructions = QtWidgets.QPushButton(self.centralwidget)
        self.instructions.setGeometry(QtCore.QRect(100, 430, 531, 101))
        self.instructions.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 26pt \"Arial\";\n"
        "border-color: rgb(0, 0, 0);")
        self.instructions.setObjectName("instructions")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "ГЛАВНОЕ МЕНЮ"))
        self.starting.setText(_translate("MainWindow", "Начать игру"))
        self.instructions.setText(_translate("MainWindow", "Инструкция"))
