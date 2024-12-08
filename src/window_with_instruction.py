from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QMainWindow

SCREEN_SIZE = [600, 700]


class Instruction(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.pixmap = QPixmap('./data/designs_picture/instruction.jpg')
        self.image = QLabel(self)
        self.image.move(60, 0)
        self.image.resize(800, 800)
        self.image.setPixmap(self.pixmap)
