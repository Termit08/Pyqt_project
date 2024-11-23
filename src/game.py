import sys

import random
from Game_window import Ui_GameWindow
from PyQt6.QtWidgets import QApplication, QMainWindow


class Game_window(QMainWindow, Ui_GameWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dicti = {}
        self.next_turn.setEnabled(False)
        self.lis_box = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                        '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
        self.sum = ['0', '1', '5', '10', '50',
                     '100', '500', '1 000','5 000', '10 000',
                       '50 000', '100 000', '250 000', '500 000', '750 000',
                         '1 000 000', '2 500 000', '5 000 000', '7 500 000', '10 000 000']
        self.lis_sum_possible = ['0', '1', '5', '10', '50',
                     '100', '500', '1 000','5 000', '10 000',
                       '50 000', '100 000', '250 000', '500 000', '750 000',
                         '1 000 000', '2 500 000', '5 000 000', '7 500 000', '10 000 000']
        self.buttons = [self.box1, self.box2, self.box3, self.box4, self.box5,
                         self.box6, self.box7, self.box8, self.box9, self.box10,
                         self.box11, self.box12, self.box13, self.box14, self.box15,
                         self.box16, self.box17, self.box18, self.box19]
        self.bankers_turn = [3, 7, 11, 14, 16, 18]
        self.confirm_button.hide()
        self.bankers_functions = [self.offer, self.change]
        self.turn_number = 0
        self.choice.setEnabled(False)
        self.give_number.clicked.connect(self.random_number)
        self.next_turn.clicked.connect(self.turn)


    def random_number(self):
        for i in self.sum:
            self.possible_sum.addItem(i)
        for i in self.lis_box:
            summ = random.choice(self.sum)
            self.dicti[i] = summ
            self.sum.remove(summ)
        player_number = random.choice(self.lis_box)
        self.num.setText(player_number)
        self.lis_box.remove(player_number)
        for i in range(19):
            number = self.lis_box[0]
            self.buttons[i].setText(number)
            self.lis_box.remove(number)
        self.give_number.setEnabled(False)
        self.next_turn.setEnabled(True)

    def turn(self):
        check_box = 0
        self.possible_sum.clear()
        for i in self.buttons:
            if i.isChecked():
                self.lis_sum_possible.remove(self.dicti[i.text()])
                self.sum_in_box.setText(self.dicti[i.text()])
                del self.dicti[i.text()]
                i.deleteLater()
                self.buttons.remove(i)
                check_box += 1
        if check_box != 0:
            self.turn_number += 1
        if self.turn_number in self.bankers_turn:
            self.banker()
        for i in self.lis_sum_possible:
            self.possible_sum.addItem(i)
        if len(self.buttons) == 0 and self.turn_number < 100:
            self.game_over() 

    def offer(self):
        self.bank.append('ПРЕДЛОЖЕНИЕ СУММЫ')
        sum_of_numbers = 0
        for i in self.lis_sum_possible:
            sum_of_numbers += int(''.join(i.split()))
        self.offer_sum = sum_of_numbers // len(self.lis_sum_possible)
        self.offer_sum += sum_of_numbers * 0.05
        self.bank.append(str(self.offer_sum))
        self.bank.append('ВЫ СОГЛАШАЕТЕСЬ?')
        self.choice.accepted.connect(self.winning_sum)
        self.choice.rejected.connect(self.rejected_sum)
        
    def rejected_sum(self):
        self.bank.clear()
        self.bank.append('ВЫ ОТКЛОНИЛИ ПРЕДЛОЖЕНИЕ')
        self.bank.append('ИГРА ПРОДОЛЖАЕТСЯ')
        for i in self.buttons:
            i.setEnabled(True)
        self.next_turn.setEnabled(True)
        self.choice.setEnabled(False)

    def winning_sum(self):
        self.win_sum.setText(str(self.offer_sum))
        self.turn_number = 100
        self.bank.append(f'ВЫ ВЫИГРАЛИ {self.offer_sum}')
        self.bank.append('ИГРА ПРОДОЛЖАЕТСЯ НА ИНТЕРЕС')
        for i in self.buttons:
            i.setEnabled(True)
        self.next_turn.setEnabled(True)
        self.choice.setEnabled(False)

    def banker(self):
        self.choice.setEnabled(True)
        self.next_turn.setEnabled(False)
        for i in self.buttons:
            i.setEnabled(False)
        bankers_turn = random.choice(self.bankers_functions)
        if bankers_turn == self.offer:
            self.offer()
        elif bankers_turn == self.change:
            self.change()

    def change(self):
        self.bank.append('ПРЕДЛОЖЕНИЕ ОБМЕНА')
        self.bank.append('ГОТОВЫ ОБМЕНЯТЬСЯ?')
        self.choice.accepted.connect(self.accept_change)
        self.choice.rejected.connect(self.reject_change)

    def accept_change(self):
        self.confirm_button.show()
        self.bank.append('ВЫБЕРИТЕ НОМЕР КОРОБКИ:')
        for i in self.buttons:
            i.setEnabled(True)
        self.confirm_button.clicked.connect(self.confirm)
        self.choice.setEnabled(False)
        self.confirm_button.hide()
        self.next_turn.setEnabled(True)

    def confirm(self):
        check = 0
        for i in self.buttons:
            if i.isChecked():
                text = i.text()
                i.setText(self.num.toPlainText())
                self.num.setText(text)
                check = 1
        if check == 0:
            self.confirm()
        self.confirm_button.hide()

    def reject_change(self):
        self.bank.setText("ПРЕДЛОЖЕНИЕ ОБМЕНА ОТКЛОНЕНО")
        self.bank.setText("ИГРА ПРОДОЛЖАЕТСЯ")
        self.next_turn.setEnabled(True)
        self.choice.setEnabled(False)
        for i in self.buttons:
            i.setEnabled(True)

    def game_over(self):
        self.win_sum.setText(self.lis_sum_possible[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game_window()
    ex.show()
    sys.exit(app.exec())
