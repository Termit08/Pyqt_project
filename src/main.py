import sys
from main_menu import Ui_MainMenu
from window_with_instruction import Instruction
from game import Game_window
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class Main(QMainWindow, Ui_MainMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pixmap = QPixmap('main_menu.jpg')
        self.image = QLabel(self)
        self.image.resize(764, 756)
        self.image.move(0, 0)
        self.image.setPixmap(self.pixmap)
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
    ex = Main()
    ex.show()
    sys.exit(app.exec())
