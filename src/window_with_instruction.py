import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

SCREEN_SIZE = [600, 700]


class Inst(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')

        self.pixmap = QPixmap('photo_instruction.jpg')
        self.image = QLabel(self)
        self.image.move(60, 0)
        self.image.resize(800, 800)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Inst()
    ex.show()
    sys.exit(app.exec())