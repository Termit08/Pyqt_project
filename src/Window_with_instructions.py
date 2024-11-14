import sys
import io

from PyQt6 import uic 
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow


inst =  '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>776</width>
    <height>805</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>0</y>
      <width>681</width>
      <height>761</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>../data/list_with_instruction/instruction.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>776</width>
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

class Instruction(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(inst)
        uic.loadUi(f, self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Instruction()
    ex.show()
    sys.exit(app.exec())