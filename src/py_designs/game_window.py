from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GameWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 773)
        MainWindow.setStyleSheet("background-color: rgb(62, 50, 61);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 50, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 110, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.possible_sum = QtWidgets.QListWidget(parent=self.centralwidget)
        self.possible_sum.setGeometry(QtCore.QRect(280, 140, 271, 491))
        self.possible_sum.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.possible_sum.setObjectName("possible_sum")
        self.sum_in_box = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.sum_in_box.setGeometry(QtCore.QRect(30, 680, 231, 31))
        self.sum_in_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sum_in_box.setObjectName("sum_in_box")
        self.labe = QtWidgets.QLabel(parent=self.centralwidget)
        self.labe.setGeometry(QtCore.QRect(30, 110, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labe.setFont(font)
        self.labe.setStyleSheet("color: rgb(255, 255, 255);")
        self.labe.setObjectName("labe")
        self.confirm_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.confirm_button.setGeometry(QtCore.QRect(600, 690, 191, 21))
        self.confirm_button.setStyleSheet("background-color: rgb(212, 224, 255);\n"
"color: rgb(0, 0, 0);")
        self.confirm_button.setObjectName("confirm_button")
        self.choice_for_offer = QtWidgets.QDialogButtonBox(parent=self.centralwidget)
        self.choice_for_offer.setGeometry(QtCore.QRect(570, 640, 221, 41))
        self.choice_for_offer.setStyleSheet("background-color: rgb(212, 224, 255);")
        self.choice_for_offer.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.choice_for_offer.setObjectName("choice_for_offer")
        self.next_turn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_turn.setGeometry(QtCore.QRect(550, 40, 261, 51))
        self.next_turn.setStyleSheet("background-color: rgb(212, 224, 255);\n"
"color: rgb(0, 0, 0);")
        self.next_turn.setObjectName("next_turn")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 640, 121, 51))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 150, 231, 508))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.box1 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box1.setStyleSheet("color: rgb(255, 255, 255);")
        self.box1.setText("")
        self.box1.setObjectName("box1")
        self.verticalLayout.addWidget(self.box1)
        self.box2 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box2.setStyleSheet("color: rgb(255, 255, 255);")
        self.box2.setText("")
        self.box2.setObjectName("box2")
        self.verticalLayout.addWidget(self.box2)
        self.box3 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box3.setStyleSheet("color: rgb(255, 255, 255);")
        self.box3.setText("")
        self.box3.setObjectName("box3")
        self.verticalLayout.addWidget(self.box3)
        self.box4 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box4.setStyleSheet("color: rgb(255, 255, 255);")
        self.box4.setText("")
        self.box4.setObjectName("box4")
        self.verticalLayout.addWidget(self.box4)
        self.box5 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box5.setStyleSheet("color: rgb(255, 255, 255);")
        self.box5.setText("")
        self.box5.setObjectName("box5")
        self.verticalLayout.addWidget(self.box5)
        self.box6 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box6.setStyleSheet("color: rgb(255, 255, 255);")
        self.box6.setText("")
        self.box6.setObjectName("box6")
        self.verticalLayout.addWidget(self.box6)
        self.box7 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box7.setStyleSheet("color: rgb(255, 255, 255);")
        self.box7.setText("")
        self.box7.setObjectName("box7")
        self.verticalLayout.addWidget(self.box7)
        self.box8 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box8.setStyleSheet("color: rgb(255, 255, 255);")
        self.box8.setText("")
        self.box8.setObjectName("box8")
        self.verticalLayout.addWidget(self.box8)
        self.box9 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box9.setStyleSheet("color: rgb(255, 255, 255);")
        self.box9.setText("")
        self.box9.setObjectName("box9")
        self.verticalLayout.addWidget(self.box9)
        self.box10 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box10.setStyleSheet("color: rgb(255, 255, 255);")
        self.box10.setText("")
        self.box10.setObjectName("box10")
        self.verticalLayout.addWidget(self.box10)
        self.box11 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box11.setStyleSheet("color: rgb(255, 255, 255);")
        self.box11.setText("")
        self.box11.setObjectName("box11")
        self.verticalLayout.addWidget(self.box11)
        self.box12 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box12.setStyleSheet("color: rgb(255, 255, 255);")
        self.box12.setText("")
        self.box12.setObjectName("box12")
        self.verticalLayout.addWidget(self.box12)
        self.box13 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box13.setStyleSheet("color: rgb(255, 255, 255);")
        self.box13.setText("")
        self.box13.setObjectName("box13")
        self.verticalLayout.addWidget(self.box13)
        self.box14 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box14.setStyleSheet("color: rgb(255, 255, 255);")
        self.box14.setText("")
        self.box14.setObjectName("box14")
        self.verticalLayout.addWidget(self.box14)
        self.box15 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box15.setStyleSheet("color: rgb(255, 255, 255);")
        self.box15.setText("")
        self.box15.setObjectName("box15")
        self.verticalLayout.addWidget(self.box15)
        self.box16 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box16.setStyleSheet("color: rgb(255, 255, 255);")
        self.box16.setText("")
        self.box16.setObjectName("box16")
        self.verticalLayout.addWidget(self.box16)
        self.box17 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box17.setStyleSheet("color: rgb(255, 255, 255);")
        self.box17.setText("")
        self.box17.setObjectName("box17")
        self.verticalLayout.addWidget(self.box17)
        self.box18 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box18.setStyleSheet("color: rgb(255, 255, 255);")
        self.box18.setText("")
        self.box18.setObjectName("box18")
        self.verticalLayout.addWidget(self.box18)
        self.box19 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.box19.setStyleSheet("color: rgb(255, 255, 255);")
        self.box19.setText("")
        self.box19.setObjectName("box19")
        self.verticalLayout.addWidget(self.box19)
        self.win_sum = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.win_sum.setGeometry(QtCore.QRect(320, 680, 231, 31))
        self.win_sum.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.win_sum.setObjectName("win_sum")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(660, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.num = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.num.setGeometry(QtCore.QRect(430, 40, 61, 51))
        self.num.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.num.setObjectName("num")
        self.give_number = QtWidgets.QPushButton(parent=self.centralwidget)
        self.give_number.setGeometry(QtCore.QRect(30, 10, 93, 91))
        self.give_number.setStyleSheet("background-color: rgb(212, 224, 255);\n"
"color: rgb(0, 0, 0);")
        self.give_number.setObjectName("give_number")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 660, 231, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.bank = QtWidgets.QListWidget(parent=self.centralwidget)
        self.bank.setGeometry(QtCore.QRect(570, 140, 271, 491))
        self.bank.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bank.setObjectName("bank")
        self.choice_for_change = QtWidgets.QDialogButtonBox(parent=self.centralwidget)
        self.choice_for_change.setGeometry(QtCore.QRect(570, 640, 221, 41))
        self.choice_for_change.setStyleSheet("background-color: rgb(221, 224, 255);\n"
"color: rgb(0, 0, 0);")
        self.choice_for_change.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.choice_for_change.setObjectName("choice_for_change")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", " Номер вашей коробки:"))
        self.label_3.setText(_translate("MainWindow", "Возможные суммы выигрыша"))
        self.labe.setText(_translate("MainWindow", "Номера оставшихся коробок"))
        self.confirm_button.setText(_translate("MainWindow", "Подтвердить"))
        self.next_turn.setText(_translate("MainWindow", "Следующий ход"))
        self.label_7.setText(_translate("MainWindow", "Cумма выигрыша:"))
        self.label_4.setText(_translate("MainWindow", "Банкир"))
        self.give_number.setText(_translate("MainWindow", "Выдать номер"))
        self.label_6.setText(_translate("MainWindow", "Сумма, которая выбывает:"))
