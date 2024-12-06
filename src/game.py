import sys
sys.path.append('./src.py.designs')
import random
from game_window import Ui_GameWindow
from dictionary_window import Ui_DictionaryWindow
from PyQt6.QtWidgets import QApplication, QMainWindow


class Game_window(QMainWindow, Ui_GameWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dict_with_sum = {}
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
        self.check_count_changes = 0
        self.confirm_button.hide()
        self.bankers_functions = [self.offer, self.change]
        self.turn_number = 0
        self.rejected_changes = 0
        self.choice_for_offer.setEnabled(False)
        self.choice_for_change.setEnabled(False)
        self.choice_for_change.hide()
        self.give_number.clicked.connect(self.random_number)
        self.next_turn.clicked.connect(self.turn)
        self.dicti_with_sum_for_statistics = {key: value for key, value in self.dict_with_sum.items()}

    def random_number(self):
        for i in self.sum:
            self.possible_sum.addItem(i)
        for i in self.lis_box:
            summ = random.choice(self.sum)
            self.dict_with_sum[i] = summ
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
        self.dicti_with_sum_for_statistics = {key: value for key, value in self.dict_with_sum.items()}

    def turn(self):
        check_box = 0
        self.possible_sum.clear()
        for i in self.buttons:
            if i.isChecked():
                self.lis_sum_possible.remove(self.dict_with_sum[i.text()])
                self.sum_in_box.setText(self.dict_with_sum[i.text()])
                del self.dict_with_sum[i.text()]
                i.deleteLater()
                self.buttons.remove(i)
                check_box += 1
        if check_box != 0:
            self.turn_number += 1
        if self.turn_number in self.bankers_turn:
            self.banker()
        for i in self.lis_sum_possible:
            self.possible_sum.addItem(i)
        if len(self.buttons) == 0:
            self.next_turn.setText('Словарь')
            self.next_turn.clicked.connect(self.go_dictionary)
            if self.turn_number < 100:
                self.game_over()
        
    def offer(self):
        self.choice_for_offer.setEnabled(True)
        self.bank.addItem('ПРЕДЛОЖЕНИЕ СУММЫ')
        sum_of_numbers = 0
        for i in self.lis_sum_possible:
            sum_of_numbers += int(''.join(i.split()))
        self.offer_sum = sum_of_numbers // len(self.lis_sum_possible)
        self.offer_sum -= self.offer_sum * 0.1
        self.offer_sum = self.offer_sum // 1
        self.bank.addItem(str(self.offer_sum))
        self.bank.addItem('ВЫ СОГЛАШАЕТЕСЬ?')
        self.choice_for_offer.accepted.connect(self.winning_sum)
        self.choice_for_offer.rejected.connect(self.rejected_sum)
        
    def rejected_sum(self):
        self.bank.clear()
        self.bank.addItem('ВЫ ОТКЛОНИЛИ ПРЕДЛОЖЕНИЕ')
        self.bank.addItem('ИГРА ПРОДОЛЖАЕТСЯ')
        for i in self.buttons:
            i.setEnabled(True)
        self.next_turn.setEnabled(True)
        self.choice_for_offer.setEnabled(False)

    def winning_sum(self):
        self.bank.clear()
        self.win_sum.setText(str(self.offer_sum))
        self.turn_number = 100
        self.bank.addItem(f'ВЫ ВЫИГРАЛИ {self.offer_sum}')
        self.bank.addItem('ИГРА ПРОДОЛЖАЕТСЯ НА ИНТЕРЕС')
        for i in self.buttons:
            i.setEnabled(True)
        self.next_turn.setEnabled(True)
        self.choice_for_offer.setEnabled(False)

    def banker(self):
        self.bank.clear()
        self.next_turn.setEnabled(False)
        for i in self.buttons:
            i.setEnabled(False)
        bankers_turn = random.choice(self.bankers_functions)
        if bankers_turn == self.offer or (bankers_turn == self.change and (self.check_count_changes >= 2 or self.rejected_changes > 1)):
            self.choice_for_offer.show()
            self.choice_for_change.hide()
            self.offer()
        elif bankers_turn == self.change:
            self.choice_for_offer.hide()
            self.choice_for_change.show()
            self.change()

    def change(self):
        self.check_count_changes += 1
        self.choice_for_change.setEnabled(True)
        self.bank.addItem('ПРЕДЛОЖЕНИЕ ОБМЕНА')
        self.bank.addItem(f'ПРЕДЛОЖЕНИЕ {self.check_count_changes} ИЗ 2')
        self.bank.addItem(f'ОТКЛОНЕНО {self.rejected_changes} ИЗ 1')
        self.bank.addItem('ГОТОВЫ ОБМЕНЯТЬСЯ?')
        self.choice_for_change.accepted.connect(self.accept_change)
        self.choice_for_change.rejected.connect(self.reject_change)

    def accept_change(self):
        self.bank.clear()
        self.confirm_button.show()
        self.bank.addItem('ВЫБЕРИТЕ НОМЕР КОРОБКИ:')
        for i in self.buttons:
            i.setEnabled(True)
        self.confirm_button.clicked.connect(self.confirm)

    def confirm(self):
        self.bank.clear()
        check = 0
        for i in self.buttons:
            if i.isChecked():
                text = i.text()
                self.bank.addItem(f'ВЫ ПОМЕНЯЛИ КОРОБКУ С {self.num.toPlainText()} НА {text}')
                i.setText(self.num.toPlainText())
                self.num.setText(text)
                check = 1
        if check == 0:
            self.accept_change()
        else:
            self.choice_for_change.setEnabled(False)
            self.next_turn.setEnabled(True)
            self.confirm_button.hide()

    def reject_change(self):
        self.bank.clear()
        self.bank.addItem("ПРЕДЛОЖЕНИЕ ОБМЕНА ОТКЛОНЕНО")
        self.bank.addItem('ПРЕДЛОЖЕНИЙ ОБМЕНА БОЛЬШЕ НЕ БУДЕТ')
        self.bank.addItem("ИГРА ПРОДОЛЖАЕТСЯ")
        self.next_turn.setEnabled(True)
        for i in self.buttons:
            i.setEnabled(True)
        self.choice_for_change.setEnabled(False)
        self.rejected_changes = 2

    def game_over(self):
        self.win_sum.setText(self.lis_sum_possible[0])

    def go_dictionary(self):
        self.dictionary = Dictionary(self.dicti_with_sum_for_statistics)
        self.dictionary.show()


class Dictionary(QMainWindow, Ui_DictionaryWindow):
    def __init__(self, dict_fron_game_window):
            super().__init__()
            self.dict_from_game_window = dict_fron_game_window
            self.setupUi(self)
            self.show_button.clicked.connect(self.show_dictionary)

    def show_dictionary(self):
        dict_from_game_window = self.dict_from_game_window
        for key in dict_from_game_window.keys():
            self.numbers.append(key)
        for value in dict_from_game_window.values():
            self.sums.append(value)
        self.show_button.setEnabled(False)
