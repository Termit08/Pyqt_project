import sys

from game import Game_window
from PyQt6 import uic
from Window_with_instructions import Instruction
import io
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>764</width>
    <height>756</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>-10</x>
      <y>-50</y>
      <width>781</width>
      <height>761</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>../data/phones/main_menu.jpg</pixmap>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>160</y>
      <width>521</width>
      <height>71</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 36pt &quot;MS Shell Dlg 2&quot;;
color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string>ГЛАВНОЕ МЕНЮ</string>
    </property>
   </widget>
   <widget class="QPushButton" name="starting">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>300</y>
      <width>531</width>
      <height>101</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);

font: 26pt &quot;MS Shell Dlg 2&quot;;
border-color: rgb(0, 0, 0);
</string>
    </property>
    <property name="text">
     <string>Начать игру</string>
    </property>
   </widget>
   <widget class="QPushButton" name="instructions">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>430</y>
      <width>531</width>
      <height>101</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 26pt &quot;MS Shell Dlg 2&quot;;
border-color: rgb(0, 0, 0);</string>
    </property>
    <property name="text">
     <string>Инструкция</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>764</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
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