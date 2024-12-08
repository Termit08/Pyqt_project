import sys

from py_designs.main_menu import Ui_MainMenu
from window_with_instruction import Instruction
from game import Game_window
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.starting.clicked.connect(self.go_game)
        self.instructions.clicked.connect(self.go_instruction)

    def go_game(self):
        self.game = Game_window()
        self.game.show()

    def go_instruction(self):
        self.instruction = Instruction()
        self.instruction.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
